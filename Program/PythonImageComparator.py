#Como se pueden encaminar las cualidades de la mente con tal de producir acciones de caracter mayor, con tal de sintetizar 
#Los aplicativos que mejoran como el componente intelectual se produce, como el comportamiento interno se conduce.
#Como las experiencias de mi saber determinan como yo puedo entender, las realidades que yo quiero vivir.
#Como aprendo a ser mas magico, como yo aprendo a ser mas alto, como yo puedo entender, las verdades que construyen el 
#El proceso que se mueve en mi, el proceso que produce mente, las cualidades que mejoran como mi realidad se 
#conduce a si misma, como el saber promueve como el comportamiento se analiza.



#Como yo puedo conducir mi mente hacia el trabajo del saber.

#Entendiendo como yo puedo hacer para construir el proceso que produce el codigo que yo quiero entender.


#Installa OpenCV

#Comienza una cosa y completala
#Vamos a comenzar

# pip install numpy
# pip install opencv-python




#Comparame dos imagenes y dime si son iguales
#Describe el proceso de como hiciste el objetivo en un articulo.

#El repositorio con el articulo y el programa, el programa corre cuando instales, y lees el articulo.


#Puedo comparar imagenes, y decir si son iguales

#Yo uso los scripts de python para mandar comandos al terminal.
#Esos scripts ejecutan comandos de git.
#Y esos comandos de git, me actualizan la nubecita.
#Me dan la fuerza.
#Fuerza a GitHub, que cualquier archivo que yo actualize en mi repositorio siempre se sube.
#Yo puedo validar si el comando de git se ejecuto de manera correcta.
#Lo siguiente seria que.
#
 
#import pyscreenshot

  

import pyautogui
import os
import numpy as np
import cv2


#Estas son las imaganes que vamos a procesar

img0 = cv2.imread('6.jpg', 1)
img1 = cv2.imread('1.0.jpg',1)
img2 = cv2.imread('2.jpg',1)

#Estos son los puntos de coordenada de la imaginen a comparar.
print(img0)

#longitud de las columnas 
print(len(img0[0]))

#Es el directorio donde esta el script en el que estamos trabajando.
print(os.getcwd())

print("Generate more code")


#Sacame la data de que como hicimos esto.
for i in range(len(img0)):
    for j in range(len(img0[0])):
        img0[i,j]

print('here')


#Pruebo que la biblioteca funcione
screenHeight = pyautogui.size() 
print(screenHeight)
currentMouseY = pyautogui.position()
print(currentMouseY)

#Tomo el screenshot
im = pyautogui.screenshot('my_screenshot.png')


# since the pyautogui takes as a 
# PIL(pillow) and in RGB we need to 
# convert it to numpy array and BGR 
# so we can write it to the disk



""" 
# To capture the screen
image = pyscreenshot.grab()
  
# To display the captured screenshot
image.show()
  
# To save the screenshot
image.save("GeeksforGeeks.png")
 """














