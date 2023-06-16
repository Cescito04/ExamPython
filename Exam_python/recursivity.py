def divinRec(a,b):
    if a < b:
        return 0 #critére d'arrêt
    else:
        return 1 + divinRec(a - b,b) #appel récursif
    

#Ecriture de la fonction de factorielle    
def NouveauRec(a,b):
    if b == 0:
        return 1 #parce que factorielle de 0 est égal à 1
    elif b == 1:
        #lorsque b =1 nous avons a! = a
        return a 
    else:
        return NouveauRec(a,b-1)
    

    
    #Pour a=2 et b=3 nous aurons trois appels récursifs
   #premier appel
NouveauRec(2,3)
#deuxieme appel
NouveauRec(2,2)
#troisieme appel
NouveauRec(2,1)
        
        


