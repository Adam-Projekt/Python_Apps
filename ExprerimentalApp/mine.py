import pyautogui as p
import time
import random
import keyboard

def lose(): p.click(1000,300)
def checkwin(): return not p.pixelMatchesColor(1026, 293, (255, 255, 0))
def checklose(): return not p.pixelMatchesColor(1022,311,(255,255,0)) 
def checkalive(): return not checklose() or checkwin()
def clickTile(x,y): 
    p.click(x*50 + 800,y*50 + 400) 
def clickMine(x,y): 
    p.click(x*50 + 800,y*50 + 400,button='right')
def gridreset():
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
def readTile(x, y):
    px = p.pixel(x*50 + 800, y*50 + 425)  
    color_map = {
        (189,189,189):-1,
        (189,189,189): 0,
        (17,17,249): 1,
        (0,189,0): 2,
        (255,0,0): 3,
        (0,0,123): 4,
        (127,13,13): 5,
        (0,123,123): 6,
        (0,0,0): 7,
        (123,123,123): 8,
    }
    return color_map.get(px, -1)  

active = False
grid = []
gridreset()
    



print("Jdi do minespeewer do 3 sekund")
time.sleep(3)

clickTile(4,4)
print(readTile(4,4))
while active:
    print(grid)
    if keyboard.is_pressed('e'):
        active = False
    if checklose(): 
        gridreset()
        lose()
    elif checkwin(): 
        active = False
    
    clickTile(4,4)
    
    
print(checkwin())
print(checklose())
print(checkalive())
time.sleep(100)
    
