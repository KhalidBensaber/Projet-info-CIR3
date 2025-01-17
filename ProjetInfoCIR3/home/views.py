from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import logout
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from ProjetInfoCIR3.BDD.Fonction_db import Get_Utilisateur, Add_Match, Get_Match, Get_Equipe, Get_Utilisateur, Set_Match, Get_Event, Add_Event, Set_Event, Add_Equipe, Get_Equipe_password, Set_Equipe_tab_joueur, Set_Utilisateur_status, Set_Event_cash_price, Set_Event_inscrit, Set_Event_places_min
import qrcode
from io import BytesIO
from django.http import HttpResponse
from PIL import Image

from django.http import HttpResponse
from django.conf import settings
import os

def react_app(request):
    # Chemin complet vers le fichier index.html
    index_path = os.path.join(settings.BASE_DIR, 'static/react/dist/index.html')
    
    # Vérifiez si le fichier existe
    if os.path.exists(index_path):
        with open(index_path, 'r') as file:
            return HttpResponse(file.read(), content_type='text/html')
    return HttpResponse("index.html not found", status=404)



@login_required
def home(request):
    user_name = request.user.username  # Get the current user's name
    user_list = Get_Utilisateur()
    current_user = next((user for user in user_list if user['pseudo'] == user_name), None)
    user_role = current_user['status'] if current_user else None
    return render(request, 'home.html', {'user_role': user_role})

@login_required
def manage_matches(request):
    if request.method == 'POST':
        equipe1 = request.POST['equipe1']
        equipe2 = request.POST['equipe2']
        date = request.POST['date']
        score1 = request.POST.get('score1')
        score2 = request.POST.get('score2')
        winner = request.POST.get('winner')
        referee = request.POST['referee']
        event = request.POST['event']
        if 'edit_match' in request.POST:
            match = next((match for match in Get_Match() if match['equipe1'] == equipe1 and match['equipe2'] == equipe2 and match['_event'] == event), None)
            print(equipe1, equipe2, event)
            #print(match[equipe1], match[equipe2], match[event])
            if (match != None) :
                message = "Match updated successfully!"
                Set_Match(equipe1, equipe2, date, score1, score2, winner, referee, event)
            else:
                message = "ERROR: Match not found."
        else:
            Add_Match(equipe1, equipe2, date, score1, score2, winner, referee, event)
            message = "Match added successfully!"
        return render(request, 'manager/manage_matches.html', {'message': message})
    
    matches = Get_Match()
    squads = Get_Equipe()
    referees = [user for user in Get_Utilisateur() if user['status'] == 'referee']
    events = Get_Event()
    return render(request, 'manager/manage_matches.html', {'matches': matches, 'squads': squads, 'referees': referees, 'events': events})

@login_required
def manage_events(request):
    if request.method == 'POST':
        nom = request.POST['nom']
        date_debut = request.POST['date_debut']
        date_fin = request.POST['date_fin']
        places_max = request.POST['places_max']
        cash_price = request.POST['cash_price']
        status = request.POST['status']
        prix = request.POST['prix']
        if 'edit_event' in request.POST:
            event = next((event for event in Get_Event() if event['nom'] == nom), None)
            places_libres = int(places_max) - len(event['inscrit'])
            tab_inscrit = event['inscrit']
            Set_Event(nom, date_debut, date_fin, places_max, places_libres, cash_price, status, prix, tab_inscrit)
        else:
            places_libres = places_max
            Add_Event(nom, date_debut, date_fin, places_max, places_libres, cash_price, status, prix)
        return redirect('manage_events')
    
    events = Get_Event()
    return render(request, 'manager/manage_events.html', {'events': events})

@login_required
def manage_team(request):
    message = ""
    if request.method == 'POST':
        if 'create_team' in request.POST:
            team_name = request.POST['team_name']
            password = request.POST['password']
            Add_Equipe(team_name, [request.user.username], password)
            return redirect('manage_team')
        elif 'join_team' in request.POST:
            team_name = request.POST['team_name']
            password = request.POST['password']
            team = next((team for team in Get_Equipe() if team['nom'] == team_name), None)
            if team and team['password'] == password:
                # don't add the player if he's already in the team
                if request.user.username in team['tab_joueur']:
                    message = "You are already in this team."
                    return render(request, 'player/manage_team.html', {'teams': Get_Equipe(), 'message': message})
                # Remove user from previous team
                for t in Get_Equipe():
                    if request.user.username in t['tab_joueur']:
                        t['tab_joueur'].remove(request.user.username)
                        Set_Equipe_tab_joueur(t['_id'], t['tab_joueur'])
                # Add user to new team
                team['tab_joueur'].append(request.user.username)
                Set_Equipe_tab_joueur(team['_id'], team['tab_joueur'])
                return redirect('manage_team')
            else:
                message = "Incorrect password. Please try again."
    
    teams = Get_Equipe()
    return render(request, 'player/manage_team.html', {'teams': teams, 'message': message})

@login_required
def donate(request):
    if request.method == 'POST':
        event_id = request.POST['event']
        amount = float(request.POST['amount'])
        event = next((event for event in Get_Event() if event['nom'] == event_id), None)
        print(event_id, "----------", Get_Event())
        if event:
            new_cash_price = str(int(event['cash_price']) + amount)
            Set_Event_cash_price(event_id, new_cash_price)
        return redirect('donate')
    
    events = Get_Event()
    return render(request, 'spectator/donate.html', {'events': events})

@login_required
def buy_ticket(request):
    message = ""
    user_role = next((user['status'] for user in Get_Utilisateur() if user['pseudo'] == request.user.username), None)
    if request.method == 'POST':
        event_id = request.POST['event']
        event = next((event for event in Get_Event() if event['nom'] == event_id), None)
        if event:
            if request.user.username in event['inscrit']:
                message = "You already have a ticket for this event."
            elif int(event['place_libre']) > 0:
                event['inscrit'].append(request.user.username)
                event['place_libre'] = str(int(event['place_libre']) - 1)
                Set_Event_inscrit(event['_id'], event['inscrit'])
                Set_Event_places_min(event['_id'], event['place_libre'])
                # Add half of the ticket price to the cash prize if not free
                if user_role not in ['streamer', 'commentator']:
                    new_cash_price = str(int(event['cash_price']) + (int(event['prix']) / 2))
                    Set_Event_cash_price(event_id, new_cash_price)
                message = "Ticket purchased successfully!"
            else:
                message = "No available spots for this event."
        return render(request, 'spectator/buy_ticket.html', {'events': Get_Event(), 'message': message, 'user_role': user_role})
    
    events = Get_Event()
    return render(request, 'spectator/buy_ticket.html', {'events': events, 'message': message, 'user_role': user_role})

@login_required
def view_tickets(request):
    user_pseudonym = request.user.username
    user_firstname = next((user['prenom'] for user in Get_Utilisateur() if user['pseudo'] == user_pseudonym), None)
    user_lastname = next((user['nom'] for user in Get_Utilisateur() if user['pseudo'] == user_pseudonym), None)
    events = [event for event in Get_Event() if user_pseudonym in event['inscrit']]
    if request.method == 'POST':
        event_name = request.POST['event']
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=20,
            border=4,
        )
        qr.add_data("event: "+event_name+", name: "+user_firstname+" \""+user_pseudonym+"\" "+user_lastname)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)
        return HttpResponse(buffer, content_type="image/png")
    
    return render(request, 'spectator/view_tickets.html', {'events': events})

@login_required
def view_team_history(request):
    user_name = request.user.username
    team = next((team for team in Get_Equipe() if user_name in team['tab_joueur']), None)
    if team:
        team_name = team['nom']
        matches = [match for match in Get_Match() if match['equipe1'] == team_name or match['equipe2'] == team_name]
        event_wins = {}
        event_losses = {}
        for match in matches:
            match['status'] = 'completed' if match['score1'] is not None and match['score2'] is not None else 'pending'
            if match['status'] == 'completed':
                if match['wineur'] == team_name:
                    match['result'] = 'win'
                    event_wins[match['_event']] = event_wins.get(match['_event'], 0) + 1
                else:
                    match['result'] = 'defeat'
                    event_losses[match['_event']] = event_losses.get(match['_event'], 0) + 1
            else:
                match['result'] = 'pending'
        overall_wins = sum(event_wins.values())
        overall_losses = sum(event_losses.values())
        tournaments = []
        for event_name, wins in event_wins.items():
            event = next((event for event in Get_Event() if event['nom'] == event_name), None)
            event_matches = [match for match in matches if match['_event'] == event_name]
            tournament_result = 'win' if wins == max(event_wins.values()) else 'lose'
            tournaments.append({'event': event, 'matches': event_matches, 'result': tournament_result})
        for event_name, losses in event_losses.items():
            event = next((event for event in Get_Event() if event['nom'] == event_name), None)
            event_matches = [match for match in matches if match['_event'] == event_name]
            tournament_result = 'lose' if losses == max(event_losses.values()) else 'win'
            tournaments.append({'event': event, 'matches': event_matches, 'result': tournament_result})
    else:
        matches = []
        overall_wins = 0
        tournaments = []
    return render(request, 'player/view_team_history.html', {'matches': matches, 'overall_wins': overall_wins, 'tournaments': tournaments})

@login_required
def view_user_history(request):
    user_name = request.user.username
    user_events = [event for event in Get_Event() if user_name in event['inscrit']]
    user_history = []
    for event in user_events:
        event_matches = [match for match in Get_Match() if match['_event'] == event['nom']]
        team_wins = {}
        for match in event_matches:
            match['status'] = 'completed' if match['score1'] is not None and match['score2'] is not None else 'pending'
            if match['status'] == 'completed':
                winner = match['wineur']
                team_wins[winner] = team_wins.get(winner, 0) + 1
            else:
                winner = 'pending'
            match['winner'] = winner
        overall_winner = max(team_wins, key=team_wins.get) if team_wins else 'pending'
        user_history.append({'event': event, 'matches': event_matches, 'overall_winner': overall_winner})
    return render(request, 'spectator/view_user_history.html', {'user_history': user_history})




@csrf_protect
def custom_logout(request):
    if request.method == "POST":
        logout(request)
        return JsonResponse({"success": True, "message": "Déconnexion réussie"})
    return JsonResponse({"success": False, "message": "Méthode non autorisée"}, status=405)


def role_management(request):
    # Page that allows the user to manage other users' roles. Managers and admin can set the role of other users (except admin, which can only be set by another admin)
    return render(request, 'role_management.html')

@login_required
def manage_accounts(request):
    if request.method == 'POST':
        username = request.POST['username']
        status = request.POST['status']
        user = next((user for user in Get_Utilisateur() if user['pseudo'] == username), None)
        if user:
            user_id = user['_id']
            if Set_Utilisateur_status(user_id, status):
                return redirect('manage_accounts')
            else:
                return render(request, 'manager/manage_accounts.html', {'error': 'Failed to update status'})
        else:
            return render(request, 'manager/manage_accounts.html', {'error': 'User not found'})
    print("quoicoubeh")
    return render(request, 'manager/manage_accounts.html')