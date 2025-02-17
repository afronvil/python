def total(ST):
    l=0
    DEBUT=np.zeros((LX, CX))
    for w in ST: 
        l+=1 
        DEBUT+=l*w[0]
    return DEBUT

def totaltimer(ST):
    DEBUT=np.zeros((LX, CX))
    for v in ST: 
        DEBUT+=v[3]        
    return DEBUT

def plotFlag(grid):
    # Créer une figure et un axes
    fig, ax = plt.subplots()
    cmap =plt.get_cmap()
    cmap = ListedColormap(['black' ,'green','white','red','blue', 'orange'])
    bounds = [0, 1, 2, 3, 4,5]
    #cmap = ListedColormap([g['color'] for g in genes])
    im = ax.imshow(matrice_int, cmap=cmap, vmin=0, vmax=7)  # Ajuster les limites pour centrer les couleurs
    plt.show()
