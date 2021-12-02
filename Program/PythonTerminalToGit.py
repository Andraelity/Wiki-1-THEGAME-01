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


#Esto lo ejecuto si quiero subirlo a github


import os

def solution():

    booleanoGo_1 = True
    while(booleanoGo_1):
            #Que vamos a hacer?
            #que vamos a emprender
            #
            #
            #
        if(booleanoGo_1 == True):
            print('do yo want to ask to execute system commands from python running script')
            print('1 to write link:')
            print('0 to exit():')
            booleanoGo_2 = True
            while(booleanoGo_2):
                try:
                    entrada = int(input())
                    if(entrada == 1):
                        booleanoGo_2 = False
                    if(entrada == 0):
                        exit()
                except:
                    print('except booleanoGo_2')
        
            booleanoGo_3 = True
            while(booleanoGo_3):
                try:
                    
                    print('Write CMD COMMAND')
                    stringIn_1 = input()
                    os.system(stringIn_1)
                    booleanoGo_3 = False
                    
                except:
                    print("except booleanoGo_3")
                #A donde me mandas
                #al siguiente concepto
                #
                #
                #
                
    return 0


os.system('dir')
pathTesting = os.getcwd()


#os.system('cd d:\\ \ndir')
os.system('dir')




print()
print()
print()

os.chdir('d:\\')
pathTesting = os.getcwd()
print(pathTesting)

#Cual es la carpeta donde me va a botar entrada
#
print('te manda a la carpeta que quieres que se actualize el repositorio.')


#Es un conjunto de formulas 
#Este comando me manda hacia el directorio Internet
print('D:\WRITINGS\Writing-with-code\\')
os.chdir('D:\WRITINGS\Writing-with-code\\')


#Quien es el sujeto que me permite tirar las graficas que construyen como el trabajo interno se puede generar
#Como el concepto del saber hace que todo sea mas practico como el movimiento de mi realidad ayuda a que todo sea mas pleno
#emprendiendo en la realidad esas acciones que sintetizan formas.
#Me ejecutas aplicaciones en carpetas.
#Con tal de tirar aplicaciones 
#Ese es el ritmo
#Este comando me entrega el directorio en el que estoy trabajando
pathDirectory = os.getcwd()
print(pathDirectory)

#Este for me lista todos los subdirectorios del directorio en el que estoy trabajando.
#En forma de string
#Este comando me entrega la lista de los files dentro del directorio que quiero actualizar
listfileVersion = os.listdir(os.getcwd())
#Como yo puedo entender las propiedades que se mueven en mi totalidad.
#Como yo puedo concebir el concepto que me ayuda a entender el movimiento.
#Esto me sirve 
indexFileVersion = 0
booleanoGo = True
while(booleanoGo):
    try:
        print("Estas aqui in the try")
        #Este comando sirve para determinar si es error si el archivo no esta
        #Y si si esta se ejucutan los siguientes comandosl.
        #Esto me verifica si el archivo existe
        indexFileVersion = listfileVersion.index('version.txt')
        #Esto abre para sacar data.
    
        f = open("version.txt","r+")
        #Sacas data en forma de string
        stringVersion = f.readline()
        stringGHlink = f.readline()
        print(stringVersion)


        nameFile = 'version.txt'
        stringDirectoryFile = os.getcwd() + '\\'+ nameFile
        os.remove(stringDirectoryFile)


        #Esto es puro parseo de que?, esto es puro parseo de texto
        #Como yo puedo componer las funciones que nos hacen mas divino.
        #Mero deporte, de golpes al cuerpo.

        listastringVersion = stringVersion.split(' ')
        #Esto es una string que tiene la forma numerica de la version separada por puntos he iniciando por uno
        versionNumerosPuntos = listastringVersion[1]
        listaversionNumeroPuntos = versionNumerosPuntos.split('.')
        lenlistaVersionNumeroPuntos = len(listaversionNumeroPuntos)
        numIncrement = int(listaversionNumeroPuntos[lenlistaVersionNumeroPuntos-1])
        if(numIncrement >= 10000):
            numIncrement2 = int(listastringVersion[lenlistaVersionNumeroPuntos-2])
            numIncrement2 += 1 
            numIncrement = 0


        numIncrement += 1

        #Este comando actualiza, el tipo de data que posicion en la lista ocuapa

        listaversionNumeroPuntos[lenlistaVersionNumeroPuntos-1] = str(numIncrement)
        listToWord =  '.'.join(listaversionNumeroPuntos)
        #Este es el mantra, del comportamiento que permite el desarrollo que se quiere sintetizar.
        #El modelo que me permite comprender como las realidades se conectan en busqueda de un estado mas denso.
        #que tipo de proceso yo quiero sintetizar.
        #que clase de contenido yo quieor promover.
        k = open('version.txt', 'w+')
        logString = os.system('git log -n 1')
        


        """    
        
        os.system('git init')
        os.system('git remote add origin "' + stringGHlink +'"')
        os.system('git add .')
        #Este es el mensaje que me permite unir el parseo de texto de la lista que escribe los archivos.txt dentro del directorio.
        os.system('git commit -m "'+ stringVersionNum +'"')


        """
        stringVersionNum = listToWord

        print('HERE IN THE STRING YOU WANT TO SEE')
        print(listastringVersion[0] + stringVersionNum)
        k.write(listastringVersion[0] + stringVersionNum)
        k.write(stringGHlink)
        k.close()
        #Este es el mantra
        booleanoGo = False
        #Poner esa palabra en 

    except:
        print('Estas en el except')
        f = open("version.txt","w+")
        f.write("v 1.0.0")
        print('Usuario tiene que introducir el url del repositorio:')
        stringIn = input()
        f.write(stringIn)
        #que mas puedo hacer.
        #que mas puedo entender.
        #
        booleanoGo = True
        f.close()
        

#El comportamiento que yo manejo define como el desarrollo de los sucesos se establecen, como los paradigmas de la vida hacen qeu todo sea mas nuevo.
#Como yo puedo enfocar las rutas de mi totalidad.

    #Esto es un manejo de significados, de caracter superior, como el entendimiento de folder.
    #directorios.

    # for i in listfileVersion:
    #     print(i)
    # print(os.getcwd())

    # print(i)
#esto es el directorio
#
stringDirectory = os.getcwd()
print(stringDirectory)
logString = os.system('git log -n 1')
print(logString)


#los parametros que construyen el fundamento que yo quiero promover, la direccion de la mente que me ayuda 
#El tiempo le va da valor.
#Que muchas personas lo sepan manejar
#mera psicologia con puras cabezas mentales.
#detallando las formulas que permiten el movimiento.
#El tiro andresito esta en tirar wikipedias
#En componer las relaciones de la mente que producen
#el movimiento a enfocar.
