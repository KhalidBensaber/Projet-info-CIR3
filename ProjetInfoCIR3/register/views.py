from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from .forms import CustomUserCreationForm
from ProjetInfoCIR3.BDD.Fonction_db import Add_utilisateur
import json


@csrf_protect
def register(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            form = CustomUserCreationForm({
                'username': data.get('username'),
                'password1': data.get('password1'),
                'password2': data.get('password2'),
            })
            print("Validation du formulaire...")  # Log avant validation
            if form.is_valid():
                user = form.save()
                # Sauvegarde dans MongoDB
                Add_utilisateur(
                    nom=data.get('first_name'),
                    prenom=data.get('last_name'),
                    pseudo=user.username,
                    mot_de_pass=user.password,
                    email=data.get('email'),
                    status=data.get('status'),
                )
                return JsonResponse({'success': True, 'message': 'Account created successfully!'})
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
        except Exception as e:
            print("Erreur lors du traitement :", str(e))  # Log des exceptions
            return JsonResponse({'success': False, 'message': str(e)}, status=500)
    return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)



