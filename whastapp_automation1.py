from whatsapp import WhatsApp
import pywhatkit as kit
import time
import datetime
import os
import clipboard
from pytube import YouTube
import pyautogui as pg

phone=input("Please enter the phone number of your contact: ")
whatsapp = WhatsApp(100, session="mysession")
latest_msg=""
lis=[]

for i in range(0,100):
    messages = whatsapp.get_last_message_for(phone)
    latest_msg = str(messages[-1])
    latest_msg.lstrip
    
    time.sleep(1)
    if "!stop" not in latest_msg:
        if "!wiki" in latest_msg:
            latest_msg.lstrip("!wiki")
            a=str(kit.info(latest_msg,3,True))
            if i==0:
                whatsapp.sendwhatmsg_instantly(phone,"INITIALIZING... Thank you for waiting. ChatBot started. Made by Kushagra\n\n"+a,15,True)
                lis.append(latest_msg)
                clipboard.copy(a)
            if latest_msg!=lis[-1]:
                lis.append(latest_msg)
                clipboard.copy(a)
                pg.hotkey("ctrl", "v")
                pg.press("enter")
                print(messages)
                lis.pop(0)
    if "!stop" in latest_msg:
        exit()

