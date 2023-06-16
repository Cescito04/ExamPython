import random
class Personne:
    def __init__(self,nom):
        self.nom=nom
        self.annee=None
        self.temps=None
        
def Saisie():
        t = []
        while True:
            nom = input("Entrez le nom de la personne (ou 'n pour quitter')")
            if nom=='n':
                break
            personne=Personne(nom)
            t.append(personne)
        return t
    

def calculAnnee(t,annee_min,annee_max):
        for personne in t:
            periode_approprie = False
            while not periode_approprie:
                periode=input(f"{personne.nom}, dans quelle période voulez-vous effectuer votre voyage? (entre {annee_min} et {annee_max}) ")
                annees=[]
                annee=""
                for element in periode + " ":
                    if element!=" ":
                        annee=annee+element
                    elif annee!="":
                        annees.append(annee)
                        
                
            if len(annees)==2:
                try:
                    annnee_debut,annee_fin=annees
                    if annee_min<=annnee_debut<=annee_max and annee_min<=annee_fin<=annee_max and annee_fin-annnee_debut>=10:
                        periode_approprie=True
                        personne.annee=random.randint(annnee_debut,annee_fin)
                except ValueError:
                    print("Veuillez entrez des années appropriés")       
            else:
                print("Veuillez entrez deux années : ")    
                
    
def calculTemps(t):
        for personne in t:
            annee_actuelle=personne.annee
            saut_min=max(2012,annee_actuelle-10)
            saut_max=min(2022,annee_actuelle+10)
            temps_approprie=0
            while annee_actuelle!=2017:
                annee_saut=random.randint(saut_min,saut_max)
                temps_approprie=temps_approprie+10
                if annee_saut<2017:
                    saut_min=max(saut_min,annee_saut)
                else:
                    saut_max=min(saut_max,annee_saut)
                    annee_actuelle=annee_saut
                    personne.temps=temps_approprie
                

tab = Saisie()
calculAnnee(tab,-10000,10000)
calculTemps(tab)
    
for personne in tab:
    print(f"Nom: {personne.nom}")
    print(f"Année: {personne.annee}")
    print(f"Temps approprié pour revenir en 2017: {personne.temps}")