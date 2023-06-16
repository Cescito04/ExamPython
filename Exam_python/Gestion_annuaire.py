#Créons une classe Personne 
class Personne:
    def __init__(self, nom, prenom, numero, rue, telephone, code_postal, ville):
        self.nom = nom
        self.prenom = prenom
        self.numero = numero
        self.rue = rue
        self.telephone = telephone
        self.code_postal = code_postal
        self.ville = ville

# Fonction de saisie de l'annuaire
def saisie_tab():
    annuaire = []
    while True:
        nom = input("Nom (ou 'n' pour quitter) : ")
        if nom == 'n':
            break
        prenom = input("Prénom : ")
        numero = input("Numéro : ")
        rue = input("Nom de la rue : ")
        telephone = input("Numéro de téléphone : ")
        code_postal = input("Code postal : ")
        ville = input("Ville : ")
        
        personne = Personne(nom, prenom, numero, rue, telephone, code_postal, ville)
        annuaire.append(personne)
    
    return annuaire
annuaire = saisie_tab()


# Fonction du critère de recherche
# Fonction de choix du critère de recherche
def critere_recherche():
    criteres = ['nom', 'prénom', 'nom de la rue', 'numéro de téléphone', 'code postal', 'ville']
    for critere in criteres:
        print(critere)
    
    choix = int(input("Veuillez choisir le critère de recherche : "))
    return criteres[choix - 1]


critere = critere_recherche()



# Fonction de recherche
def recherche(annuaire, critere):
    valeurRecherche = input("Saisissez la valeur de recherche pour  : ")
    resultat = []
    
    for personne in annuaire:
        if critere == 'nom' and personne.nom == valeurRecherche:
            resultat.append(True)
        elif critere == 'prénom' and personne.prenom == valeurRecherche:
            resultat.append(True)
        elif critere == 'nom de la rue' and personne.rue ==valeurRecherche:
            resultat.append(True)
        elif critere == 'numéro de téléphone' and personne.telephone == valeurRecherche:
            resultat.append(True)
        elif critere == 'code postal' and personne.code_postal == valeurRecherche:
            resultat.append(True)
        elif critere == 'ville' and personne.ville == valeurRecherche:
            resultat.append(True)
        else:
            resultat.append(False)
    
    return resultat
resultat = recherche(annuaire, critere)



#Affichage de l'annuaire
def affiche_tab(annuaire,resultat):
    print("Affichage de l'annuaire:")
    for i in range(len(annuaire)):
        if resultat[i]:
            personne = annuaire[i]
            print(f"Nom : {personne.nom}")
            print(f"Prénom : {personne.prenom}")
            print(f"Numéro : {personne.numero}")
            print(f"Nom de la rue:{personne.rue}")
            print(f"Numéro téléphone : {personne.telephone}")
            print(f"Code Postal : {personne.code_postal}")
            print(f"Ville : {personne.ville}")
            
affiche_tab(annuaire, resultat)

        




    
