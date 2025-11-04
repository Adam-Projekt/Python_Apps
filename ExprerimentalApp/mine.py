import pyautogui as p
import time
import random
import keyboard

grid = [
            -1,-1,-1,-1,-1,-1,-1,-1,-1,
            -1,-1,-1,-1,-1,-1,-1,-1,-1,
            -1,-1,-1,-1,-1,-1,-1,-1,-1
            -1,-1,-1,-1,-1,-1,-1,-1,-1,
            -1,-1,-1,-1,-1,-1,-1,-1,-1,
            -1,-1,-1,-1,-1,-1,-1,-1,-1
            -1,-1,-1,-1,-1,-1,-1,-1,-1,
            -1,-1,-1,-1,-1,-1,-1,-1,-1,
            -1,-1,-1,-1,-1,-1,-1,-1,-1
            ]

def lose(): p.click(1000,300)
def checkwin(): return not p.pixelMatchesColor(1026, 293, (255, 255, 0))
def checklose(): return not p.pixelMatchesColor(1022,311,(255,255,0)) 
def checkalive(): return not checklose() or checkwin()
def clickTile(x,y): 
    p.click(x*50 + 800,y*50 + 400) 
def clickMine(x,y): 
    p.click(x*50 + 800,y*50 + 400,button='right')
    
print("Jdi do minespeewer do 3 sekund")
time.sleep(3)
active = True
while active:
    print(grid)
    if keyboard.is_pressed('e'):
        active = False
    if checklose(): 
        grid = [
            -1,-1,-1,-1,-1,-1,-1,-1,-1,
            -1,-1,-1,-1,-1,-1,-1,-1,-1,
            -1,-1,-1,-1,-1,-1,-1,-1,-1
            -1,-1,-1,-1,-1,-1,-1,-1,-1,
            -1,-1,-1,-1,-1,-1,-1,-1,-1,
            -1,-1,-1,-1,-1,-1,-1,-1,-1
            -1,-1,-1,-1,-1,-1,-1,-1,-1,
            -1,-1,-1,-1,-1,-1,-1,-1,-1,
            -1,-1,-1,-1,-1,-1,-1,-1,-1
        ]
        lose()
    elif checkwin(): 
        active = False
    elif checkalive():
        clickTile(4,0)
        clickTile(4,1)
    
print(checkwin())
print(checklose())
print(checkalive())
time.sleep(100)
    
