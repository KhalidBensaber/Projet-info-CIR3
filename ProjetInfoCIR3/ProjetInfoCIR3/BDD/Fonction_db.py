from pymongo import MongoClient
client = MongoClient('mongodb+srv://theomeilliez:Gv1ZmorY2lczag99@projetcir3full.apni4.mongodb.net/?retryWrites=true&w=majority&appName=projetCIR3full')
db = client["projetcir3"]
# utilisateur
def Add_utilisateur(nom,prenom,pseudo,mot_de_pass,email,status,winstreak=0,win=0,lose=0): #qrcode
    return db.utilisateur.insert_one({"nom": nom,"prenom" : prenom , "pseudo": pseudo, "mdp": mot_de_pass, "email": email, "status" : status, "winstreak": winstreak, "win" : win , "lose" : lose })  

def Sup_utilisateur(id):
    return db.utilisateur.delete_one({"_id" : id})

# getteur de la table utilisateur 
def Get_Utilisateur(): 
    return list(db.utilisateur.find())
def Get_Utilisateur_Id(pseudo):
    id =  db.utilisateur.find_one({"pseudo": pseudo}, {"_id": 1})
    return id["pseudo"] if id else None
def Get_Utilisateur_nom(id): 
    nom =db.utilisateur.find_one({"_id" : id} , {"nom" : 1 , "_id" : 0 } )
    return  nom["nom"] if nom else None
def Get_Utilisateur_prenom(id): 
    prenom =db.utilisateur.find_one({"_id" : id} , {"prenom" : 1 , "_id" : 0 })
    return prenom["prenom"] if prenom else None
def Get_Utilisateur_pseudos(id): 
    pseudo =db.utilisateur.find_one({"_id" : id} , {"pseudo": 1 , "_id" : 0 })
    return pseudo["pseudo"] if pseudo else None
def Get_Utilisateur_mot_de_pass(id): 
    mdp =db.utilisateur.find_one({"_id" : id} , {"mdp" : 1 , "_id" : 0 })
    return mdp["mdp"] if mdp else None
def Get_Utilisateur_email(id): 
    email =db.utilisateur.find_one({"_id" : id} , {"email" : 1 , "_id" : 0 })
    return email["email"] if email else None
def Get_Utilisateur_cb(id): 
    cb =db.utilisateur.find_one({"_id" : id} , {"cb" : 1 , "_id" : 0 })
    return cb["cb"] if cb else None
def Get_Utilisateur_status(id): 
    status = db.utilisateur.find_one({"_id": id}, {"status": 1, "_id": 0})
    return status["status"] if status else None
def Get_Utilisateur_winstreak(id): 
    winstreak = db.utilisateur.find_one({"_id" : id} , {"winstreak" : 1 , "_id" : 0 })
    return winstreak["winstreak"] if winstreak else None
def Get_Utilisateur_win(id): 
    win = db.utilisateur.find_one({"_id" : id} , {"win" : 1 , "_id" : 0 })
    return win["win"] if win else None
def Get_Utilisateur_email(id):
    lose = db.utilisateur.find_one({"_id" : id} , {"lose" : 1 , "_id" : 0 })
    return lose["lose"] if lose else None
# Setteur de la tabble utilisateur

def Set_Utilisateur(nom,prenom,pseudo,mot_de_pass,email,status,winstreak,win,lose,qrcode):
    result = db.utilisateur.update_one({"_id" : id} ,{"$set" : {"nom": nom,"prenom" : prenom , "pseudo": pseudo, "mdp": mot_de_pass, "email": email, "status" : status, "winstreak": winstreak, "win" : win , "lose" : lose,"qrcode" : qrcode} })
    return result.modified_count > 0
def Set_Utilisateur_nom(id,nom): 
    result = db.utilisateur.update_one({"_id" : id} ,{"$set" :  {"nom" : nom} })
    return result.modified_count > 0
def Set_Utilisateur_prenom(id,prenom): 
    result = db.utilisateur.update_one({"_id" : id} ,{"$set" :  {"prenom" : prenom} })
    return result.modified_count > 0
def Set_Utilisateur_pseudos(id,pseudo): 
    result = db.utilisateur.update_one({"_id" : id} ,{"$set" :  {"pseudo": pseudo} })
    return result.modified_count > 0
def Set_Utilisateur_mot_de_pass(id,mot_de_pass): 
    result = db.utilisateur.update_one({"_id" : id} , {"$set" : {"mdp" : mot_de_pass} })
    return result.modified_count > 0
def Set_Utilisateur_email(id,email): 
    result = db.utilisateur.update_one({"_id" : id} ,{"$set" :  {"email" : email} })
    return result.modified_count > 0
def Set_Utilisateur_cb(id,Cb): 
    result = db.utilisateur.update_one({"_id" : id}, {"$set" :  {"cb" : Cb} })
    return result.modified_count > 0
def Set_Utilisateur_status(id,status): 
    result = db.utilisateur.update_one({"_id" : id} ,{"$set" : {"status" : status} })
    return result.modified_count > 0
def Set_Utilisateur_winstreak(id,winstreak): 
    result = db.utilisateur.update_one({"_id" : id} ,{"$set" : {"winstreak" : winstreak} })
    return result.modified_count > 0
def Set_Utilisateur_win(id,win): 
    result =db.utilisateur.update_one({"_id" : id},{"$set" : {"win" : win} })
    return result.modified_count > 0
def Set_Utilisateur_lose(id,lose): 
    result = db.utilisateur.update_one({"_id" : id} ,{"$set" :  {"lose" : lose} })
    return result.modified_count > 0




# equipe
def Add_Equipe(nom,tab_joueur,password=""):
    return db.equipe.insert_one({"nom": nom, "tab_joueur" : tab_joueur, "password" : password})

def Sup_Equipe(id):
    return db.equipe.delete_one({"_id" : id})

#getteur de equipe
def Get_Equipe(): 
    return list(db.equipe.find())
def Get_Equipe_nom(id): 
    nom = db.equipe.find_one({"_id" : id} , {"nom" : 1 , "_id" : 0 } )
    return nom["nom"]if nom else None
def Get_Equipe_tab_joueur(id): 
    tab_joueur =db.equipe.find_one({"_id" : id} , {"tab_joueur" : 1 , "_id" : 0 })
    return list(tab_joueur["tab_joueur"]) if tab_joueur else None
def Get_Equipe_password(id):
    password = db.equipe.find_one({"_id" : id} , {"password" : 1 , "_id" : 0 })
    return password["password"] if password else None

#setteur de equipe
def Set_Equipe(nom,tab_joueur,password):
    result = db.equipe.update_one({"_id" : id} ,{"$set" : {"nom": nom, "tab_joueur" : tab_joueur, "password" : password}})
    return result.modified_count > 0
def Set_Equipe_nom(id,nom): 
    result = db.equipe.update_one({"_id" : id} ,{"$set" :  {"nom" : nom} })
    return result.modified_count > 0
def Set_Equipe_tab_joueur(id,tab_joueurs): 
    result = db.equipe.update_one({"_id" : id} ,{"$set" :  {"tab_joueur" : tab_joueurs} })
    return result.modified_count > 0
def Set_Equipe_password(id,password):
    result = db.equipe.update_one({"_id" : id} ,{"$set" :  {"password" : password} })
    return result.modified_count > 0

#table event ( tournoi)
def Add_Event(nom,date_debut,date_fin,place_max,place_libre,cash_price,status,prix,tab_inscrit=[]):
    return db.event.insert_one({"nom" : nom , "date_debut": date_debut, "date_fin" : date_fin, "place_max" : place_max, "place_libre" : place_libre, "cash_price" : cash_price, "status" : status,"prix":prix, "inscrit":tab_inscrit })

def Sup_Event(id):
    return db.event.delete_one({"_id" : id})

# getteur event 

def Get_Event(): 
    return list(db.event.find())
def Get_Event_nom(id): 
    nom = db.event.find_one({"_id" : id} , {"nom" : 1 , "_id" : 0 } )
    return nom["nom"] if nom else None
def Get_Event_date_debut(id): 
    debut = db.event.find_one({"_id" : id} , {"date_debut" : 1 , "_id" : 0 })
    return debut["date_debut"] if debut else None
def Get_Event_date_fin(id): 
    fin = db.event.find_one({"_id" : id} , {"date_fin" : 1 , "_id" : 0 })
    return fin["date_fin"] if fin else None
def Get_Event_place_max(id): 
    max =db.event.find_one({"_id" : id} , {"place_max": 1 , "_id" : 0 })
    return max["place_max"] if max else None
def Get_Event_place_libre(id): 
    libre =db.event.find_one({"_id" : id} , {"place_libre" : 1 , "_id" : 0 })
    return libre["place_libre"] if libre else None
def Get_Event_cash_price(id):
    cash_price = db.event.find_one({"_id" : id} , {"cash_prices" : 1 , "_id" : 0 })
    return cash_price["cash_prices"] if cash_price else None
def Get_Event_status(id):
    status =db.event.find_one({"_id" : id} , {"status" : 1 , "_id" : 0 })
    return status["status"] if status else None
def Get_Event_prix(id):
    prix =db.event.find_one({"_id" : id} , {"prix" : 1 , "_id" : 0 })
    return prix["prix"] if prix else None
def Get_Event_inscrit(id):
    inscrit =db.event.find_one({"_id" : id} , {"inscrit" : 1 , "_id" : 0 })
    return inscrit["inscrit"] if inscrit else None

#setteur event
def Set_Event(nom,date_debut,date_fin,place_max,place_libre,cash_price,status,prix,tab_inscrit): 
    result = db.event.update_one({"nom" : nom} ,{"$set" :  {"date_debut": date_debut, "date_fin" : date_fin, "place_max" : place_max, "place_libre" : place_libre, "cash_price" : cash_price, "status" : status,"prix":prix, "inscrit":tab_inscrit }})
    return result.modified_count > 0
def Set_Event_nom(id,nom): 
    result = db.event.update_one({"_id" : id} ,{"$set" :  {"nom" : nom} })
    return result.modified_count > 0
def Set_Event_date_debut(id,date_debut): 
    result = db.event.update_one({"_id" : id} ,{"$set" :  {"date_debut" : date_debut} })
    return result.modified_count > 0
def Set_Event_date_fin(id,date_fin): 
    result = db.event.update_one({"_id" : id} ,{"$set" :  {"date_fin" : date_fin} })
    return result.modified_count > 0
def Set_Event_place_max(id,place_max): 
    result = db.event.update_one({"_id" : id} , {"$set" : {"place_max" : place_max} })
    return result.modified_count > 0
def Set_Event_places_min(id,place_libre): 
    result = db.event.update_one({"_id" : id} ,{"$set" :  {"place_libre": place_libre} })
    return result.modified_count > 0
def Set_Event_cash_price(name,cash_price): 
    result = db.event.update_one({"nom" : name}, {"$set" :  {"cash_price" : cash_price} })
    return result.modified_count > 0
def Set_Event_status(id,status): 
    result = db.event.update_one({"_id" : id}, {"$set" :  {"status" : status} })
    return result.modified_count > 0
def Set_Event_prix(id,prix): 
    result = db.event.update_one({"_id" : id}, {"$set" :  {"prix" : prix} })
    return result.modified_count > 0
def Set_Event_inscrit(id,inscrit): 
    result = db.event.update_one({"_id" : id}, {"$set" :  {"inscrit" : inscrit} })
    return result.modified_count > 0

# match
def Add_Match(equipe1,equipe2,date,score1,score2,wineur, arbitre, _event):
    return db.match.insert_one({"equipe1" : equipe1, "equipe2" : equipe2, "date" : date, "score1" : score1, "score2" : score2, "wineur" : wineur, "arbitre" : arbitre,"_event" : _event})


def Sup_Match(id):
    return db.match.delete_one({"_id" : id})


#getteur match
def Get_Match(): 
    return list(db.match.find())
def Get_Match_equipe1(id): 
    equipe1 =db.match.find_one({"_id" : id} , {"equipe1": 1 , "_id" : 0 } )
    return list(equipe1["equipe1"]) if equipe1 else None
def Get_Match_equipe2(id): 
    equipe2 =db.match.find_one({"_id" : id} , {"equipe2" : 1 , "_id" : 0 })
    return list(equipe2["equipe2"]) if equipe2 else None
def Get_Match_date(id): 
    date = db.match.find_one({"_id" : id} , {"date" : 1 , "_id" : 0 })
    return date["date"] if date else None
def Get_Match_score1(id): 
    score1 =db.match.find_one({"_id" : id} , {"score1": 1 , "_id" : 0 })
    return  score1["score1"] if score1 else None
def Get_Match_score2(id): 
    score2 =db.match.find_one({"_id" : id} , {"score2" : 1 , "_id" : 0 })
    return score2["score2"] if score2 else None
def Get_Match_wineur(id):
    wineur = db.match.find_one({"_id" : id} , {"wineur" : 1 , "_id" : 0 })
    return wineur["wineur"] if wineur else None
def Get_Match_arbitre(id):
    arbitre = db.match.find_one({"_id" : id} , {"arbitre" : 1 , "_id" : 0 })
    return arbitre["arbitre"] if arbitre else None
def Get_Match_event(id):
    event = db.match.find_one({"_id" : id} , {"_event" : 1 , "_id" : 0 })
    return event["_event"] if event else None

#setteur match
def Set_Match(equipe1,equipe2,date,score1,score2,wineur, arbitre, _event ):
    result = db.match.update_one({"equipe1" : equipe1, "equipe2" : equipe2, "_event" : _event} ,{"$set" :  {"equipe1" : equipe1, "equipe2" : equipe2, "date" : date, "score1" : score1, "score2" : score2, "wineur" : wineur, "arbitre" : arbitre ,"_event": _event} })
    return result.modified_count > 0
def Set_Match_equipe1(id,equipe): 
    result = db.match.update_one({"_id" : id} ,{"$set" :  {"equipe1" : equipe} })
    return result.modified_count > 0
def Set_Match_equipe2(id,equipe): 
    result = db.match.update_one({"_id" : id} ,{"$set" :  {"equipe2" : equipe} })
    return result.modified_count > 0
def Set_Match_date(id,date): 
    result = db.match.update_one({"_id" : id} ,{"$set" :  {"date" : date} })
    return result.modified_count > 0
def Set_Match_score1(id,score): 
    result = db.match.update_one({"_id" : id} , {"$set" : {"score1": score} })
    return result.modified_count > 0
def Set_Match_score2(id,score): 
    result = db.match.update_one({"_id" : id} ,{"$set" :  {"score2": score} })
    return result.modified_count > 0
def Set_Match_wineur(id,wineur): 
    result = db.match.update_one({"_id" : id}, {"$set" :  {"wineur" : wineur} })
    return result.modified_count > 0
def Set_Match_wineur(id,arbitre): 
    result = db.match.update_one({"_id" : id}, {"$set" :  {"arbitre" : arbitre} })
    return result.modified_count > 0
def Set_Match_wineur(id,_event): 
    result =db.match.update_one({"_id" : id}, {"$set" :  {"_event" : _event} })
    return result.modified_count > 0

# inscrit

def Add_Inscrit(utilisateur, event):
    return db.inscrit.insert_one({"utilisateur" : utilisateur , "event" : event})


def Sup_Inscrit(id):
    return db.inscrit.delete_one({"_id" : id})

#getteur inscrit
def Get_Inscrit(): 
    return list(db.inscrit.find())
def Get_Inscrit_utilisateur_one(id): 
    utilisateur =db.inscrit.find_one({"_id" : id} , {"utilisateur": 1 , "_id" : 0 } )
    return utilisateur["utilisateur"] if utilisateur else None
def Get_Inscrit_event_one(id): 
    event =db.inscrit.find_one({"_id" : id} , {"event" : 1 , "_id" : 0 })
    return event["event"] if event else None
def Get_Inscrit_utilisateur_event(event): 
    utilisateur_all =db.inscrit.find({"event" : event} , {"event": 1 , "_id" : 0 } )
    return list(utilisateur_all["event"]) if utilisateur_all else None
def Get_Inscrit_event_utilisateur(utilisateur): 
    event_all =db.inscrit.find({"utilisateur" : utilisateur} , {"event" : 1 , "_id" : 0 })
    return event_all["event"] if event_all else None


#setteur de inscrit
def Set_Inscrit(utilisateur, event ):
    result = db.inscrit.update_one({"_id" : id} ,{"$set" :  {"utilisateur" : utilisateur , "event" : event} })
    return result.modified_count > 0
def Set_Inscrit_utilisateur(id,utilisateur): 
    result = db.inscrit.update_one({"_id" : id} ,{"$set" :  {"utilisateur" : utilisateur} })
    return result.modified_count > 0
def Set_Inscrit_equipe2(id,event): 
    result = db.inscrit.update_one({"_id" : id} ,{"$set" :  {"event" : event} })
    return result.modified_count > 0