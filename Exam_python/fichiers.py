def nbMotsAvecVoyelle(nomf):
    voyelles=['a','e','o','i','u']
    compteur=0
    with open(nomf,'r') as fichier:
        for mot in fichier:
            if mot[0] in voyelles:
                compteur=compteur+1
    return compteur

def compterChaqueMot(nomf1,nomf2):
    with open(nomf1,'r') as fichier1, open(nomf2,'w') as fichier2:
        mot_precedent=''
        compteur=0
        
        for mot in fichier1:
            if mot[-1]=='\n':
                mot = mot[:-1]
               
            
            if mot==mot_precedent:
                compteur=compteur+1
            
            else:
                if mot_precedent:
                    fichier2.write(f"{mot_precedent} {compteur}\n")
                    mot_precedent=mot
                    compteur=1
                    
        if mot_precedent:
            fichier2.write(f'{mot_precedent} {compteur}')
            

mon_fichier="/Users/ablaye/Desktop/Exam_python/fichier.txt"
nombreVoyelles=nbMotsAvecVoyelle(mon_fichier)
print(f"Nombre de mots commençant par une voyelle : {nombreVoyelles}")

mon_fichier1="/Users/ablaye/Desktop/Exam_python/motsTries.txt"
mon_fichier2="/Users/ablaye/Desktop/Exam_python/motsComptes.txt"
compterChaqueMot(mon_fichier1,mon_fichier2)