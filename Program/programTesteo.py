import os

def print3():
    for i in range(2):
        print()

variableDirectorio = 'D:\\Universidad\\Sistemas\\PrimerSemestre'
os.chdir(variableDirectorio)
directoryCWD = os.getcwd()
print(directoryCWD)

listFilesGit = os.listdir(directoryCWD)

print(listFilesGit)




booleanoGo_1 = True

print('Este comando entra al while')
print3()






""" 

indexVersion = listFilesGit.index('version.txt')
nameFileString = "version.txt"
f = open(nameFileString,"r+")
dataStringFile = f.readline()
f.close()
stringDirectoryFile = variableDirectorio + '\\' + nameFileString
os.remove(stringDirectoryFile)



"""