def print2():
    print()
    print()


def lenOfRows_int():
    for i in range(30):
        print(i)

def draw52Frame_void():
    for i in range(51):
        if( i == 10):
            print('OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO00000000000000000000000000')
        else:
            print(i)

def RunFirstList(variables_Def):

    for i in variables_Def:

        if(i == 'Juego'):
            print2()
            print('Estas dentro de Juego: ')
            print('Show list in game:')
            print('One-1 for yes')
            print('Zero-0 to exit')

            booleano_Goto = True
            while(booleano_Goto):

                try:
                    int_input = input()
                    if(int_input == str(1)):
                        print('Unity')
                        print('Physics simulation')
                        print('THEGAME')
                        print('DirectX')
                        booleano_Goto = False

                    elif(int_input == str(0)):
                        booleano_Goto = False
                        print('Exing from Juego loop')
                        print()
                except:
                    print('Inside the Except of Juego')
                    print('Catching try, return to Juego while')

        elif(i == 'Universidad'):

            print2()
            print('Estas dentro de Universidad: ')
            print('Show list in Universidad:')
            print('One-1 for yes')
            print('Zero-0 to exit')

            booleano_Goto = True
            while(booleano_Goto):

                try:
                    int_input = input()
                    if(int_input == str(1)):
                        print('MATH')
                        print('MATRIX')
                        print('Computer Science')
                        print('SuperComputer-keyboard-ThumbMouse')
                        print('WIKI\'s')
                        booleano_Goto = False

                    elif(int_input == str(0)):
                        booleano_Goto = False
                        print('Exing from Universidad loop')
                        print()
                except:
                    print('Inside the Except of Universidad')
                    print('Catching try, return to Universidad while')

            print('Estas dentro de Universidad')
        elif(i == 'Trabajo'):

            print2()
            print('Estas dentro de Trabajo: ')
            print('Show list in Trabajo:')
            print('One-1 for yes')
            print('Zero-0 to exit')

            booleano_Goto = True
            while(booleano_Goto):

                try:
                    int_input = input()
                    if(int_input == str(1)):
                        print('Python')
                        print('C++')
                        print('Algorithms')
                        print('research')
                        print('C#')

                        booleano_Goto = False

                    elif(int_input == str(0)):
                        booleano_Goto = False
                        print('Exing from Trabajo loop')
                        print()
                except:
                    print('Inside the Except of Trabajo')
                    print('Catching try, return to Trabajo while')

            print('Estas dentro de Trabajo:')



# Como yo puedo seguir jugando al desarrollo de este elemento
# Como yo puedo aprender a mejorar cualidades en la vida.
# las cuales me permitan analizar el fundamento
# Teorico de la mente.


#Porque el puede generar el desarrollo de la realidd
#Como la composicion del saber determina como mi mente se aprende.
#Que puedo yo mejorar en la vida.

#Como yo puedo promover el concepto que determina como la realidad se vive

