import win32api, win32con
import time
import pynput
from pynput.keyboard import Key, Controller
from multiprocessing.connection import wait
import pyautogui
import psutil
import os
import subprocess
import sys
from league_connection import LeagueConnection

keyboard2 = Controller()

def Lclick(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

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

#os.startfile (r"C:\Users\PpekKOX\Desktop\ifritMango\FPS\fps32.lnk")
print('Aram-Bot Version: 4.1')
print('Last date of Update: 13.04.2023')
os.system("TASKKILL /F /IM RiotClientServices.exe")
os.system("TASKKILL /F /IM explorer.exe")
time.sleep(2)


print('Proceeding to open LeagueClient...')
subprocess.call(['C:\Riot Games\League of Legends\LeagueClient.exe'])
time.sleep(2)
Lclick(843,456)



time.sleep(20)
lockfile = os.path.expanduser('~\\AppData\\Local\\Riot Games\\Riot Client\\Config\\lockfile')
connection = LeagueConnection(lockfile, timeout=10)
data = {'username': 'h201916604', 'password': 'wY5fTsno1anBEE2d', 'persistLogin': False}
res = connection.put('/rso-auth/v1/session/credentials', json=data)
res.status_code

time.sleep(15)
Lclick(267,839)

time.sleep(20)
time.sleep(1)
subprocess.call([sys.executable, 'C:\\Users\\PpekKOX.Laptop\\Desktop\\League-Of-Legends-ARAM_BOT\\Bot.py'])
time.sleep(5)
Lclick(280,843)
time.sleep(1)
Lclick(280,843)
