def mult(s,reste,Dir):
    directions = {
    (0, -1):  (0, 1),  # West -> East
    (0, 1):  (0, -1),  # East -> West
    (1, 0):  (-1, 0),  # South -> North
    (-1, 0):  (1, 0)   # North -> South
    }

    timers=+s[3]
    MDir = directions.get(Dir)
    (stop,nouvelle, new_timers)=P(s, Dir, timers) 
    reste -= M(nouvelle - TOTAL  * nouvelle, MDir)
    s[0] += nouvelle - TOTAL * nouvelle 
    reste+=nouvelle*stop+stop 
    reste-=stop*s[0]  
    s[0]-=reste
    s[2] = s[2]*s[0]
    s[3]=new_timers*s[0]
    return stop, s, reste, 

def growth(s,reste):
    s[3]+=reste*s[0]
    Type=s[1]
    reste = s[0].copy()
    for direction in Type: 
        #print(direction)
        (stop, s,reste)=mult(s,reste,direction)    
    s[0]-=reste*s[0]
    s[0]-=stop*s[0]
    s[3]+=stop*s[3]
    stop = np.zeros((LX, CX)) 
    return s, reste