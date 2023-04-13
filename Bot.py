from time import sleep
import pyautogui as pg
import os
from pynput.keyboard import Key, Controller
import win32api, win32con
import random
import psutil
from multiprocessing.connection import wait
import json
import requests

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
        pg.moveTo(x,y,0.2)
        Rclick()
        sleep(0.1)
        Rclick()
        sleep(0.2)

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
        sleep(1)
        Rclick(716,540)
        sleep(0.1)
        Rclick(716,540)
        sleep(1)
        Rclick(850,538)
        sleep(0.1)
        Rclick(850,538)
        sleep(1)

    def in_game_shop():
        gra.open_shop()
        sleep(1)
        gra.buy_items()
        gra.close_shop()

    def middle_screen_click():
        Rclick(960,540)
        sleep(0.5)

    def follow_ally_1():
        keyboard2.press(Key.f2)
        gra.middle_screen_click()
        keyboard2.release(Key.f2)
        sleep(0.2)
    
    def follow_ally_2():
        keyboard2.press(Key.f3)
        gra.middle_screen_click()
        keyboard2.release(Key.f3)
        sleep(0.2)

    def follow_ally_3():
        keyboard2.press(Key.f4)
        gra.middle_screen_click()
        keyboard2.release(Key.f4)
        sleep(0.2)
    
    def follow_ally_4():
        keyboard2.press(Key.f5)
        gra.middle_screen_click()
        keyboard2.release(Key.f5)
        sleep(0.2)

    def koniec():
        Lclick(1447,547)
        sleep(1)
        Lclick(1268,540)
        sleep(1)
        Lclick(1118,543)
        sleep(1)
        Lclick(975,539)
        sleep(1)
        Lclick(739,545)
        sleep(1)
        Lclick(1433,499)
        sleep(1)
        Lclick(529,544)
        sleep(1)
        Lclick(602,545)
        sleep(1)
        Lclick(961,840)     #okay
        sleep(1)
        Lclick(961,840)                                     
        sleep(1)
        Lclick(961,840)

    def auto_attack():
        keyboard2.press('x')
        sleep(0.1)
        keyboard2.release('x')     


webhook_url = "https://discord.com/api/webhooks/1093984448153927731/Ju2WX0GlTBTKwphMdCqnHJNgkiKl6HEXW9ec0GYl1TBf_AIDLGi2tCVDfNLmbIDkbK5Y"
message = "The account has finished playing."

payload = {
    "content": message
}

json_payload = json.dumps(payload)

headers = {
    "Content-Type": "application/json"
}


sleep(10)

#Zamyka E-mail Pop-Up
Lclick(1047,227)
sleep(2)

#Sprawdza Leaverbustera
Lclick(837,485)


#Sprawdza czy konto ma 30 LvL
while True:
    if pg.locateOnScreen('30.png', confidence=0.92):
        response = requests.post(webhook_url, data=json_payload, headers=headers)
        print("Webhook sent with status code:", response.status_code)
        while pg.locateOnScreen('30.png', confidence=0.92):
            sleep(1)
    else:
        print('Account not finished yet')
        break


#Wchodzi w kolejke
print('Closing all PoP-Ups and background RiotClient services')
os.system("TASKKILL /F /IM RiotClientUxRender.exe")
os.system("TASKKILL /F /IM RiotClientUxRender.exe")
os.system("TASKKILL /F /IM RiotClientUx.exe")
os.system("TASKKILL /F /IM RiotClientCrashHandler.exe")

play = pg.locateCenterOnScreen('play.png', confidence=0.95)
pg.leftClick(play)
sleep(3)

pg.leftClick(381,261)   #PvP
sleep(3)

aram_mode = pg.locateCenterOnScreen('aram_mode.png', confidence=0.95)
pg.leftClick(aram_mode)
sleep(3)

confirm = pg.locateCenterOnScreen('confirm.png', confidence=0.95)
pg.leftClick(confirm)
sleep(3)

find_match = pg.locateCenterOnScreen('find_match.png', confidence=0.95)
pg.leftClick(find_match)
sleep(3)


#Akceptuje Mecz
while True:
    if pg.locateOnScreen('accept.png'):
        print('Accepting Match!')
        sleep(1)
        Lclick(961,721)
        break
    else:
        sleep(0.2)

#Champion Select

while True:
    if checkIfProcessRunning('legends'):
        break
    else:
        #sprawdza czy jestes w champion seletcie
        if pg.locateOnScreen('champselect_aram.png', confidence=0.8):         
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
    if pg.locateOnScreen('in_game.png', confidence=0.9):
        gra.open_shop()
        sleep(3)
        gra.buy_items()
        sleep(3)
        gra.close_shop()
        sleep(3)
        keyboard2.press('y')                          
        sleep(0.1)
        keyboard2.release('y')
        break
    else:
        sleep(0.2)

sleep(3)

#IN-GAME-PATTERNS
while True:
    if checkIfProcessRunning('legends'):
        gra.follow_ally_1()
        gra.auto_attack()
        gra.minimap_movement()
        gra.minimap_movement()
        gra.follow_ally_2()
        gra.auto_attack()
        gra.minimap_movement()
        gra.minimap_movement()        
        gra.follow_ally_3()
        gra.auto_attack()
        gra.minimap_movement()
        gra.minimap_movement()
        gra.follow_ally_4()
        gra.auto_attack()
        gra.minimap_movement()
        gra.minimap_movement()
    else:
        sleep(30)
        gra.koniec()
        print('Game 1 finished')
        break


#Sprawdza czy konto ma 30 LvL
while True:
    if pg.locateOnScreen('30.png', confidence=0.92):
        response = requests.post(webhook_url, data=json_payload, headers=headers)
        print("Webhook sent with status code:", response.status_code)
        while pg.locateOnScreen('30.png', confidence=0.92):
            sleep(1)
    else:
        print('Account not finished yet')
        break


for x in range(2, 302):
    print('Game ' + str(x) + ' finished')
    sleep(3)
    Lclick(848,836)
    sleep(3)
    Lclick(848,836)    
    sleep(1)
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
                Lclick(848,836)
                sleep(3)
                Lclick(958,717)        

    sleep(10)
       
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

    sleep(2)

    #Lockuje Camere
    while True:
        if pg.locateOnScreen('camera.png', confidence=0.9):
            keyboard2.press('y')                          
            sleep(0.1)
            keyboard2.release('y')
            break
        else:
            sleep(0.2)

    sleep(3)

    #IN-GAME-PATTERNS

    while True:
        if checkIfProcessRunning('legends'):
            gra.follow_ally_1()
            gra.auto_attack()
            gra.minimap_movement()
            gra.minimap_movement()
            gra.follow_ally_2()
            gra.auto_attack()
            gra.minimap_movement()
            gra.minimap_movement()        
            gra.follow_ally_3()
            gra.auto_attack()
            gra.minimap_movement()
            gra.minimap_movement()
            gra.follow_ally_4()
            gra.auto_attack()
            gra.minimap_movement()
            gra.minimap_movement()
        else:
            sleep(30)
            gra.koniec()
            break

    sleep(1)

    #Sprawdza czy konto ma 30 LvL
    while True:
        if pg.locateOnScreen('30.png', confidence=0.92):
            response = requests.post(webhook_url, data=json_payload, headers=headers)
            print("Webhook sent with status code:", response.status_code)
            while pg.locateOnScreen('30.png', confidence=0.92):
                sleep(1)
        else:
            print('Account not finished yet')
            break

    sleep(1)       
