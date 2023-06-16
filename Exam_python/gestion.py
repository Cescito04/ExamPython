# Définition de la structure pour une personne
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
        nom = input("Nom (ou 'q' pour quitter) : ")
        if nom == 'q':
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

# Fonction de choix du critère de recherche
def critere_recherche():
    criteres = ['nom', 'prénom', 'nom de la rue', 'numéro de téléphone', 'code postal', 'ville']
    print("Critères de recherche disponibles :")
    for i, critere in enumerate(criteres, 1):
        print(f"{i}. {critere}")
    
    choix = int(input("Veuillez choisir le critère de recherche : "))
    critere = criteres[choix - 1]
    return critere

# Fonction de recherche
def recherche(annuaire, critere):
    valeur_recherche = input(f"Veuillez entrer la valeur de recherche pour {critere} : ")
    resultat = []
    
    for personne in annuaire:
        if critere == 'nom' and personne.nom == valeur_recherche:
            resultat.append(True)
        elif critere == 'prénom' and personne.prenom == valeur_recherche:
            resultat.append(True)
        elif critere == 'nom de la rue' and personne.rue == valeur_recherche:
            resultat.append(True)
        elif critere == 'numéro de téléphone' and personne.telephone == valeur_recherche:
            resultat.append(True)
        elif critere == 'code postal' and personne.code_postal == valeur_recherche:
            resultat.append(True)
        elif critere == 'ville' and personne.ville == valeur_recherche:
            resultat.append(True)
        else:
            resultat.append(False)
    
    return resultat

# Procédure d'affichage de l'annuaire selon les critères de recherche
def affiche_tab(annuaire, resultat):
    print("Résultats de la recherche :")
    for personne, trouve in zip(annuaire, resultat):
        if trouve:
            print(f"Nom : {personne.nom}")
            print(f"Prénom : {personne.prenom}")
            print(f"Numéro : {personne.numero}")
            print(f"Nom de la rue : {personne.rue}")
            print(f"Numéro de téléphone : {personne.telephone}")
            print(f"Code postal : {personne.code_postal}")
            print(f"Ville : {personne.ville}")
            print("--------------------")

# Programme principal
def main():
    annuaire = saisie_tab()
    critere = critere_recherche()
    resultat = recherche(annuaire, critere)
    affiche_tab(annuaire, resultat)

# Exécution du programme principal
if __name__ == '__main__':
    main()
