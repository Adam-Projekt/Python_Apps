import pyautogui as p
import time
import random
import keyboard

def lose(): p.click(1000,300)
def checkwin(): return not p.pixelMatchesColor(1026, 293, (255, 255, 0))
def checklose(): return not p.pixelMatchesColor(1022,311,(255,255,0)) 
def checkalive(): return not checklose() or checkwin()
def clickrandom(): 
    p.click(random.randint(1,9)*50 + 800,random.randint(1,9)*50 + 400) 
    if random.randint(1,4) == 1: p.rightClick(random.randint(1,9)*50 + 800,random.randint(1,9)*50 + 400) 
print("Jdi do minespeewer do 3 sekund")

time.sleep(3)
active = True
while active:
    if keyboard.is_pressed('e'):
        active = False
    if checklose(): 
        lose()
    elif checkwin(): 
        active = False
    elif checkalive():
        clickrandom() 
    
print(checkwin())
print(checklose())
print(checkalive())
time.sleep(100)
    
