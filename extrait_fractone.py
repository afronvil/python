import numpy as np
from PIL import Image
import os

def extrait_fractone(img):
    arr = np.array(img)
    fract=np.zeros((1024,1024))
    arr=arr.reshape((1024, 1024))
    n=0
    for i in range(1022):
        for j in range(1022):
            if (arr[i+1,j+1]>50 and arr[i,j]>5 and arr[i,j+1]>5 and arr[i,j+2]>5 and arr[i+1,j]>5 and arr[i+1,j+2]>5 and arr[i+2,j]>5 and arr[i+2,j+1]>5 and arr[i+2,j+2]>5 ):
                fract[i+1,j+1]=arr[i+1,j+1]
                fract[i,j]=arr[i,j]
                fract[i,j+1]=arr[i,j+1]
                fract[i,j+2]=arr[i,j+2]
                fract[i+1,j]=arr[i+1,j]
                fract[i+1,j+1]=arr[i+1,j+1]
                fract[i+1,j+2]=arr[i+1,j+2]
                fract[i+2,j]=arr[i+2,j]
                fract[i+2,j+1]=arr[i+2,j+1]
                fract[i+2,j+2]=arr[i+2,j+2]
                n+=1
    print(n)
    diff=arr-fract
    im_fract = Image.fromarray(fract)
    im_diff = Image.fromarray(diff)
    im_fract.save("your_file.tif")
    im_fract.show()
    

    

dir='/home/afronvil/essaipython/Data/'
directory=os.listdir(dir)
print(directory)
for imgs in directory:
    img = Image.open(os.path.join(dir,imgs))
    img.show()   
    extrait_fractone(img)
np.savetxt('result-2.txt', vector, fmt='%.2f')

