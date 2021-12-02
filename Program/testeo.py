
import os

lista = []

for i in range(5):
    lista.append('x' + str(i))
    print(lista[i])


try:
    print('dentro del try')
    lista.index('x5')
except:
    print('dentro del except')
    lista.append('x5')

for i in lista:
    print(i)


# k = open('folder1.txt', 'w+')
# k.write('version 1.0.0')
# k.close()


k = open('folder1.txt','r+')
stringBasica = k.readline()
stringBasica = 'version 1.0.1'
k.close()
os.chdir('d:\internet\wiki-1-THEGAME-02\program\\')
nameFile = 'folder1.txt'

stringDirectoryFile = os.getcwd() + '\\'+ nameFile

os.remove(stringDirectoryFile)

k = open('folder1.txt', 'w+')
k.write(stringBasica)
k.close()

#Tirame mas codigo, tirame testeo

f = open('folder.txt','w+')
f.write('version 1.0.0')
f.close()

f = open('folder.txt', 'r+')


#Manejando texto.
#Manejando aplicaciones 
#Manejando componentes.

stringVersion = f.readline()
listastringVersion = stringVersion.split(' ')
#Esto es una string que tiene la forma numerica de la version separada por puntos he iniciando por uno
versionNumerosPuntos = listastringVersion[1]
listaversionNumeroPuntos = versionNumerosPuntos.split('.')
lenlistaVersionNumeroPuntos = len(listaversionNumeroPuntos)
numIncrement = int(listaversionNumeroPuntos[lenlistaVersionNumeroPuntos-1])
numIncrement += 1
listaversionNumeroPuntos[lenlistaVersionNumeroPuntos-1] = str(numIncrement)
stringToTxt = '.'.join(listaversionNumeroPuntos)
print(listastringVersion[0])
print(stringToTxt)
f.write(listastringVersion[0] + stringToTxt)

f.close()










print('casa')
print()
print()
print()
print()

print()

print()

print()
print()



listaTesteo = []

for i in range(5):
    listaTesteo.append('Esta es : ' + str(i))


listaTesteo[len(listaTesteo)-1] = 'Aqui'

print(listaTesteo)


#Esto me esta corriendo 
os.chdir('D:\INTERNET\Wiki-1-THEGAME-02\Program')
listfileVersion = os.listdir(os.getcwd())

#Este comando si presenta existencia, no me lanzas error.
#Pero si no hay existencia me lanza error
indexFileVersion = listfileVersion.index('version.txt')

k = open('read.txt', 'r+')
k.write('version 1.0.0')
k.close()

