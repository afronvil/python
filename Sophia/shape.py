1 """ Module qui cree des formes"""
2
3 DATE = 17022025


import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm
import numpy as np
import growth
import copy
import visualization

def forme(ST):
    total_st_precedent = None
    while True:
        TOTAL=np.zeros((LX, CX))
        DEBUT=total(ST)
        TIMER=totaltimer(ST)
        j=0
        for u in ST:  
            j+=1 
            TOTAL+=u[0]
        VT=copy.deepcopy(ST)
        TT=0
        for s in ST:
            stop=np.zeros((LX, CX))
            TOTAL-=s[0]
            s[0]+=reste
            s[2]-=s[2] 
            s[3]+=reste
            reste=np.zeros((LX, CX))
            #comp=TOTAL-s[2]
            (s, reste)=growth(s, reste)
            del ST[TT]
            TOTAL+=s[0]
            ST.insert(TT,[s[0],s[1],s[2],s[3],s[4]])
            TT+=1
            
        for i in range(len(ST)):
            ST[i][0] += reste * VT[i][0]  # Mise à jour de l'élément 0 (température)
            ST[i][3] += reste * VT[i][3] 
        
        #TOTAL=TOTAL-(ST[3][2])

        total_st_actuel = total(ST)
        if total_st_precedent is not None and np.array_equal(total_st_actuel, total_st_precedent):
            break  # Sortir de la boucle si la somme totale n'a pas changé
        reste-=reste
        k=0
        total_st_precedent = total_st_actuel   
        matrice_int = np.array(total(ST), dtype=int)  # Convertir en entier pour la colormap
        # print("total(ST)")
        # print(total(ST))
        # print("totaltimer(ST)") 
        # print(totaltimer(ST)) 
    return matrice_int
     

if __name__ == " __main__ ":
    print("total(ST)")
    print(total(ST))
    plotFlag(forme(ST))   