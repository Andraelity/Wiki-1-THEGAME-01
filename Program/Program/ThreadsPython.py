from threading import Thread
import time
import os

answer = None
answerCopy = '0'

def ask():
    global start_time, answer
    start_time = time.time()
    print(start_time)
    answer = input("Enter a number:\n")
    time.sleep(0.001)

def threadAsk():
    t1 = Thread(target=ask)
    t1.start()


def condition():
        
    if(answer == 0):
        print('setting out from the loop')
        os._exit()

def secondThread():
    example_thread = Thread(target=condition)
    example_thread.start()
    
def timing():
    global answerCopy, answer
    time_limit = 100
    while True:

        for i in range(50):
            print(str(start_time) + '    ' + str(answerCopy))
            time_taken = time.time() - start_time
            if answer is not None:
                print(answer + '       ' +str(i))   
                answerCopy = answer 
                print(f"You took {time_taken} seconds to enter a number.")
                answer = None
                threadAsk()
                i += 2 
                # os._exit(1)
            # if time_taken > time_limit:
                # print("Time's up !!! \n"
                    #   f"You took {time_taken} seconds.")
                # os._exit(1)
        print('Enter a number:')
        time.sleep(5)


t1 = Thread(target=ask)
t2 = Thread(target=timing)
t1.start()
t2.start()
threadAsk() 


#i Got global conditional variables capable to translate to me the definition of mind that i want to sintetize
#How the complexity of the mind for being able to sintetize products around the general and continual motion of the present time
#How this notion is created, how this complexity make me feel in tune with the whole structure
#How i can approach the continual generation of the mind
#How i can approach the notion of self
#How i can believe in the complexity of the human mind, learning how my necesity to believe create in me a new way to explain the details.

#Como es que estas maquinas de computo pueden generar el desarrollo que usted quiere generar.