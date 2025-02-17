import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm
import numpy as np



Nb_Div  = np.zeros((LX, CX))
Div = np.zeros((LX, CX))

T  = np.zeros((LX, CX))
T0= np.zeros((LX, CX))
T1= np.zeros((LX, CX))
T2= np.zeros((LX, CX))
T3= np.zeros((LX, CX))
T4= np.zeros((LX, CX))
reste=np.zeros((LX, CX))

timers=T

stop = np.zeros((LX, CX)) 

MEM0=np.zeros((LX, CX))
MEM1=np.zeros((LX, CX))
MEM2=np.zeros((LX, CX))
MEM3=np.zeros((LX, CX))
MEM4=np.zeros((LX, CX))

timers0 = np.zeros((LX, CX))
timers1 = np.zeros((LX, CX)) 
timers2 = np.zeros((LX, CX)) 
timers3 = np.zeros((LX, CX)) 
timers4 = np.zeros((LX, CX)) 