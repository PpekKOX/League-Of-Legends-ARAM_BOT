from time import sleep
import pyautogui as pg
import os
from pynput.keyboard import Key, Controller
import win32api, win32con
import random
import psutil
from multiprocessing.connection import wait

keyboard2 = Controller()

def Lclick(x,y):
    if x is not None and y is not None:
        win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def Rclick(x=None, y=None):
    if x is not None and y is not None:
        win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
    sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)

def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;

class gra():
    def minimap_movement():
        x = random.randint(1365,1545)
        y = random.randint(665,838)
        pg.movETo(x,y,0.5)
        Rclick()
        sleep(0.1)
        Rclick()
        sleep(0.4)

    def open_shop():
        keyboard2.press('p')
        sleep(0.1)
        keyboard2.release('p')

    def close_shop():
        keyboard2.press('p')
        sleep(0.1)
        keyboard2.release('p')

    def buy_items():
        Rclick(581,542)
        sleep(0.1)
        Rclick(581,542)
        sleep(0.5)
        Rclick(716,540)
        sleep(0.1)
        Rclick(716,540)
        sleep(0.5)
        Rclick(850,538)
        sleep(0.1)
        Rclick(850,538)
        sleep(0.5)


sleep(10)

#Zamyka E-mail Pop-Up
Lclick(1047,227)
sleep(2)

#Sprawdza czy konto ma 30 LvL
while True:
    if pg.locateOnScreen('30.png', confidence=0.92):
        print('Account finished, waiting...')
        while pg.locateOnScreen('30.png', confidence=0.92):
            sleep(1)
    else:
        print('Account not finished yet')
        break

#Sprawdza Leaverbustera
print('Checking Leaverbuster PoP-Up...')
while True:
    if pg.locateOnScreen('leaver.png', confidence=0.7):
        sleep(5)
        Lclick(821,431)
        sleep(5)
        pg.typewrite("I Agree")
        sleep(5)
        Lclick(837,485)
        print('Leaverbuster PoP-Up closed')
        break
    else:
        break


#Wchodzi w kolejke
print('Closing all PoP-Ups and background RiotClient services')
os.system("TASKKILL /F /IM RiotClientUxRender.exe")
os.system("TASKKILL /F /IM RiotClientUxRender.exe")
os.system("TASKKILL /F /IM RiotClientUx.exe")
os.system("TASKKILL /F /IM RiotClientCrashHandler.exe")

play = pg.locateCenterOnScreen('play.png', confidence=0.95)
pg.leftClick(play)
sleep(2)

pg.leftClick(381,261)   #PvP
sleep(2)

aram_mode = pg.locateCenterOnScreen('aram_mode.png', confidence=0.95)
pg.leftClick(aram_mode)
sleep(2)

confirm = pg.locateCenterOnScreen('confirm.png', confidence=0.95)
pg.leftClick(confirm)
sleep(2)

find_match = pg.locateCenterOnScreen('find_match.png', confidence=0.95)
pg.leftClick(find_match)
sleep(2)


#Akceptuje Mecz
while True:
    accept = pg.locateCenterOnScreen('accept.png')
    if pg.locateOnScreen(accept):
        print('Accepting Match!')
        sleep(1)
        pg.leftClick(accept)
        break
    else:
        sleep(0.2)

#Champion Select

while True:
    if checkIfProcessRunning('legends'):
        break
    else:
        champselect_aram = pg.locateCenterOnScreen('champselect_aram.png')
        #sprawdza czy jestes w champion seletcie
        if pg.locateOnScreen(champselect_aram, confidence=0.8):         
            sleep(0.5)
        else:
            sleep(3)
            Lclick(845,841)
            sleep(3)
            Lclick(958,717)        

sleep(10)

#######################################################################################################################################################
#######################################################################################################################################################
#######################################################################################################################################################
#In-Game

#Shop

while True:
    if pg.locateOnScreen('in_game', confidence=0.9):
        gra.open_shop()
        sleep(3)
        gra.buy_items()
        sleep(3)
        gra.close_shop()
        break
    else:
        sleep(0.2)
        