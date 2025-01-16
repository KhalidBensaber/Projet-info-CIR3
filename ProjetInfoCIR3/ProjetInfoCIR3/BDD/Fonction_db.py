from pymongo import MongoClient
client = MongoClient('mongodb+srv://theomeilliez:Gv1ZmorY2lczag99@projetcir3full.apni4.mongodb.net/?retryWrites=true&w=majority&appName=projetCIR3full')
db = client["projetcir3"]
# utilisateur
def Add_Utilisateur(Nom,Prenom,Pseudo,Mot_de_passe,Email,Status,Winstreak=0,Win=0,Lose=0): #qrcode
    return db.utilisateur.insert_one({"nom": Nom,"prenom" : Prenom , "pseudo": Pseudo, "mdp": Mot_de_passe, "email": Email, "status" : Status, "winstreak": Winstreak, "win" : Win , "lose" : Lose})  

def Sup_Utilisateur(id):
    return db.utilisateur.delete_one({"_id" : id})

# getteur de la table utilisateur 
def Get_Utilisateur(): 
    return list(db.utilisateur.find())
def Get_Utilisateur_Id(pseudo):
    id =  db.utilisateur.find_one({"pseudo": pseudo}, {"_id": 1})
    return id["pseudo"] if user else None
def Get_Utilisateur_Nom(id): 
    Nom =db.utilisateurs.find_one({"_id" : id} , {"nom" : 1 , "_id" : 0 } )
    return  Nom["nom"] if user else None
def Get_Utilisateur_Prenom(id): 
    Prenom =db.utilisateurs.find_one({"_id" : id} , {"prenom" : 1 , "_id" : 0 })
    return Prenom["prenom"] if user else None
def Get_Utilisateur_Pseudos(id): 
    Pseudos =db.utilisateurs.find_one({"_id" : id} , {"pseudo": 1 , "_id" : 0 })
    return Pseudos["pseudo"] if user else None
def Get_Utilisateur_Mot_de_passe(id): 
    mdp =db.utilisateurs.find_one({"_id" : id} , {"mdp" : 1 , "_id" : 0 })
    return mdp["mdp"] if user else None
def Get_Utilisateur_email(id): 
    email =db.utilisateurs.find_one({"_id" : id} , {"email" : 1 , "_id" : 0 })
    return email["email"] if user else None
def Get_Utilisateur_cb(id): 
    cb =db.utilisateurs.find_one({"_id" : id} , {"cb" : 1 , "_id" : 0 })
    return cb["cb"] if user else None
def Get_Utilisateur_Status(id): 
    status = db.utilisateurs.find_one({"_id": id}, {"status": 1, "_id": 0})
    return status["status"] if user else None
def Get_Utilisateur_Winstreak(id): 
    winstreak = db.utilisateurs.find_one({"_id" : id} , {"winstreak" : 1 , "_id" : 0 })
    return winstreak["winstreak"] if user else None
def Get_Utilisateur_Win(id): 
    Win = db.utilisateurs.find_one({"_id" : id} , {"win" : 1 , "_id" : 0 })
    return Win["win"] if user else None
def Get_Utilisateur_email(id):
    lose = db.utilisateurs.find_one({"_id" : id} , {"lose" : 1 , "_id" : 0 })
    return lose["lose"] if user else None
def Get_Utilisateur_qrcode(id): 
    qrcode =db.utilisateurs.find_one({"_id" : id} , {"qrcode" : 1 , "_id" : 0 })
    return qrcode["qrcode"]
# Setteur de la tabble utilisateur

def Set_utilisateur(Nom,Prenom,Pseudo,Mot_de_passe,Email,Status,Winstreak,Win,Lose):
    return db.utilisateurs.update_One({"_id" : id} ,{"$set" : {"nom": Nom,"prenom" : Prenom , "pseudo": Pseudo, "mdp": Mot_de_passe, "email": Email, "status" : Status, "winstreak": Winstreak, "win" : Win , "lose" : Lose} })
def Set_Utilisateur_Nom(id,Nom): 
    return db.utilisateurs.update_One({"_id" : id} ,{"$set" :  {"nom" : Nom} })
def Set_Utilisateur_Prenom(id,Prenom): 
    return db.utilisateurs.update_One({"_id" : id} ,{"$set" :  {"prenom" : Prenom} })
def Set_Utilisateur_Pseudos(id,Pseudo): 
    return db.utilisateurs.update_One({"_id" : id} ,{"$set" :  {"pseudo": Pseudo
} })
def Set_Utilisateur_Mot_de_passe(id,Mot_de_passe): 
    return db.utilisateurs.update_One({"_id" : id} , {"$set" : {"mdp" : Mot_de_passe} })
def Set_Utilisateur_email(id,Email): 
    return db.utilisateurs.update_One({"_id" : id} ,{"$set" :  {"email" : Email} })
def Set_Utilisateur_cb(id,Cb): 
    return db.utilisateurs.update_One({"_id" : id}, {"$set" :  {"cb" : Cb} })
def Set_Utilisateur_Status(id,Status): 
    return db.utilisateurs.update_One({"_id" : id} ,{"$set" : {"status" : Status} })
def Set_Utilisateur_Winstreak(id,Winstreak): 
    return db.utilisateurs.update_One({"_id" : id} ,{"$set" : {"winstreak" : Winstreak} })
def Set_Utilisateur_Win(id,Win): 
    return db.utilisateurs.update_One({"_id" : id},{"$set" : {"win" : Win} })
def Set_Utilisateur_lose(id,Lose): 
    return db.utilisateurs.update_One({"_id" : id} ,{"$set" :  {"lose" : Lose} })
def Set_Utilisateur_lose(id,Qrcode): 
    return db.utilisateurs.update_One({"_id" : id} ,{"$set" :  {"qrcode" : Qrcode} })




# Equipe
def Add_Equipe(Nom,Tab_joueur,Manageur,Jeux):
    return db.Equipe.insert_One({"nom": Nom, "tab_joueur" : Tab_joueur, "manageur" : Manageur, "jeux" : Jeux})

def Sup_Equipe(id):
    return db.Equipe.delete_one({"_id" : id})

#getteur de Equipe
def Get_Equipe(): 
    return db.Equipes.find({},{"_id" : 1 })
def Get_Equipe_Nom(id): 
    return db.Equipes.find_one({"_id" : id} , {"nom" : 1 , "_id" : 0 } )
def Get_Equipe_tab_joueur(id): 
    return db.Equipes.find_one({"_id" : id} , {"tab_joueur" : 1 , "_id" : 0 })
def Get_Equipe_Manageur(id): 
    return db.Equipes.find_one({"_id" : id} , {"Manageur" : 1 , "_id" : 0 })
def Get_Equipe_jeux(id): 
    return db.Equipes.find_one({"_id" : id} , {"jeux" : 1 , "_id" : 0 })

#setteur de Equipes
def Set_Equipes(Nom,Tab_joueur,Manageur,Jeux):
    return db.Equipes.update_One({"_id" : id} ,{"$set" : {"nom": Nom, "tab_joueur" : Tab_joueur, "manageur" : Manageur, "jeux" : Jeux}})
def Set_Equipes_Nom(id,Nom): 
    return db.Equipes.update_One({"_id" : id} ,{"$set" :  {"nom" : Nom} })
def Set_Equipes_tab_joueur(id,Tab_joueurs): 
    return db.Equipes.update_One({"_id" : id} ,{"$set" :  {"tab_joueur" : Tab_joueurs} })
def Set_Equipes_Manageur(id,Manageur): 
    return db.Equipes.update_One({"_id" : id} ,{"$set" :  {"manageur" : Manageur} })

def Set_Equipes_jeux(id,Jeux): 
    return db.Equipes.update_One({"_id" : id} ,{"$set" :  {"jeux" : Jeux} })


#table Event ( tournoi)
def Add_Event(Nom,Date_debut,Date_fin,Places_max,Places_libres,Cash_price,Status):
    return db.Event.insert_one({"nom" : Nom , "date_deput": Date_debut, "date_fin" : Date_fin, "places_max" : Places_max, "places_libres" : Places_libres, "cash_price" : Cash_price, "status" : Status})

def Sup_Event(id):
    return db.Event.delete_one({"_id" : id})

# getteur event 

def Get_Event(): 
    return db.event.find({},{"_id" : 1 })
def Get_Event_nom(id): 
    return db.event.find_one({"_id" : id} , {"nom" : 1 , "_id" : 0 } )
def Get_Event_date_debut(id): 
    return db.event.find_one({"_id" : id} , {"date_debut" : 1 , "_id" : 0 })
def Get_Event_date_fin(id): 
    return db.event.find_one({"_id" : id} , {"date_fin" : 1 , "_id" : 0 })
def Get_Event_places_max(id): 
    return db.event.find_one({"_id" : id} , {"places_max": 1 , "_id" : 0 })
def Get_Event_places_libres(id): 
    return db.event.find_one({"_id" : id} , {"places_libres" : 1 , "_id" : 0 })
def Get_Event_cash_price(id):
    return db.event.find_one({"_id" : id} , {"cash_prices" : 1 , "_id" : 0 })
def Get_Event_status(id):
    return db.event.find_one({"_id" : id} , {"status" : 1 , "_id" : 0 })

#setteur event
def Set_Event(Nom,Date_debut,Date_fin,Places_max,Places_libres,Cash_price,Status): 
    return db.event.update_One({"_id" : id} ,{"$set" :   {"nom" : Nom , "date_deput": Date_debut, "date_fin" : Date_fin, "places_max" : Places_max, "places_libres" : Places_libres, "cash_price" : Cash_price, "status" : Status}})
def Set_Event_nom(id,Nom): 
    return db.event.update_One({"_id" : id} ,{"$set" :  {"nom" : Nom} })
def Set_Event_date_debut(id,Date_debut): 
    return db.event.update_One({"_id" : id} ,{"$set" :  {"date_debut" : Date_debut} })
def Set_Event_date_fin(id,Date_fin): 
    return db.event.update_One({"_id" : id} ,{"$set" :  {"date_fin" : Date_fin} })
def Set_Event_places_max(id,Places_max): 
    return db.event.update_One({"_id" : id} , {"$set" : {"places_max" : Places_max} })
def Set_Event_places_min(id,Places_libres): 
    return db.event.update_One({"_id" : id} ,{"$set" :  {"place_libres": Places_libres} })
def Set_Event_cash_price(id,Cash_price): 
    return db.event.update_One({"_id" : id}, {"$set" :  {"cash_price" : Cash_price} })
def Set_Event_Status(id,Status): 
    return db.event.update_One({"_id" : id}, {"$set" :  {"status" : Status} })

# match
def Add_Match(Equipe1,Equipe2,Date,Score1,Score2,Wineur, Arbitre, _event):
    return db.Event.insertone({"equipe1" : Equipe1, "equipe2" : Equipe2, "date" : Date, "score1" : Score1, "score2" : Score2, "wineur" : Wineur, "arbitre" : Arbitre,"_event" : _event})


def Sup_Match(id):
    return db.match.delete_one({"_id" : id})


#getteur Match
def Get_Match(): 
    return db.match.find({},{"_id" : 1 })
def Get_Match_equipe1(id): 
    return db.match.find_one({"_id" : id} , {"equipe1": 1 , "_id" : 0 } )
def Get_Match_equipe2(id): 
    return db.match.find_one({"_id" : id} , {"equipe2" : 1 , "_id" : 0 })
def Get_Match_date(id): 
    return db.match.find_one({"_id" : id} , {"date" : 1 , "_id" : 0 })
def Get_Match_score1(id): 
    return db.match.find_one({"_id" : id} , {"score1": 1 , "_id" : 0 })
def Get_Match_score2(id): 
    return db.match.find_one({"_id" : id} , {"score2" : 1 , "_id" : 0 })
def Get_Match_wineur(id):
    return db.match.find_one({"_id" : id} , {"wineur" : 1 , "_id" : 0 })
def Get_Match_Arbitre(id):
    return db.match.find_one({"_id" : id} , {"arbitre" : 1 , "_id" : 0 })
def Get_Match_event(id):
    return db.match.find_one({"_id" : id} , {"_event" : 1 , "_id" : 0 })

#setteur Match
def Set_Match(id,Equipe1,Equipe2,Date,Score1,Score2,Wineur, Arbitre, _event ):
    return db.match.update_One({"_id" : id} ,{"$set" :  {"equipe1" : Equipe1, "equipe2" : Equipe2, "date" : Date, "score1" : Score1, "score2" : Score2, "wineur" : Wineur, "arbitre" : Arbitre ,"_event": _event} })

def Set_Match_equipe1(id,Equipe): 
    return db.match.update_One({"_id" : id} ,{"$set" :  {"equipe1" : Equipe} })
def Set_Match_equipe2(id,Equipe): 
    return db.match.update_One({"_id" : id} ,{"$set" :  {"equipe2" : Equipe} })
def Set_Match_date(id,Date): 
    return db.match.update_One({"_id" : id} ,{"$set" :  {"date" : Date} })
def Set_Match_score1(id,Score): 
    return db.match.update_One({"_id" : id} , {"$set" : {"score1": Score} })
def Set_Match_score2(id,Score): 
    return db.match.update_One({"_id" : id} ,{"$set" :  {"score2": Score} })
def Set_Match_wineur(id,Wineur): 
    return db.match.update_One({"_id" : id}, {"$set" :  {"wineur" : Wineur} })
def Set_Match_wineur(id,Arbitre): 
    return db.match.update_One({"_id" : id}, {"$set" :  {"arbitre" : Arbitre} })
def Set_Match_wineur(id,_event): 
    return db.match.update_One({"_id" : id}, {"$set" :  {"_event" : _event} })

