import os
cwd = os.getcwd()
from pygame import mixer
f = open("sfx.4set","r")
sfx = f.read()
if sfx != "none":
    mixer.init()
    mixer.music.load(cwd+"/sfx/"+sfx+".mp3")
    mixer.music.play()
f.close()
print("Loading...")
print("""$-------$$$$$---$$$$-
$------$$---$$-$$----
$$$$---$$---$$--$$$$-
$--$$--$$---$$-----$$
$$$$----$$$$$---$$$$-""")
import requests
import sys
import time
import random
import datetime
import shutil
import webbrowser
import win11toast
from locale import currency
import platform
import atexit
import glob
import importlib
import sys
import psutil
import logging
import keyboard
from ping3 import ping, verbose_ping
import json

version = []
string = 0
#url = "http://fourteam4t.temp.swtest.ru/"
url = "http://bosstageserver.com.swtest.ru/"

print("Loaded successfully")

def install():
    try:
        print("Loading...")
        response3 = requests.get(url+"emmute.txt")
        if response3.text.lower() == "true":
            print("Maintenance emmute in progress. Try this action later")
            return "maintenance"
        else:
            response5 = requests.get(url+"commands.txt")
            commands = response5.text.split(",")
            x = 90.0 / float(len(commands))
            print("Patching commands...")
            y = 0
            percent = 0.0
            for i in range(len(commands)):
                response6 = requests.get(url+commands[y])
                comtext = response6.text
                os.chdir("Commands")
                f = open(commands[y]+".4com","a")
                f.close()
                f = open(commands[y]+".4com","w")
                f.write(comtext)
                f.close()
                y = y+1
                percent = percent + x
                print(str(percent)+"%")
                os.chdir("..")
            y = 1
            f = open("commands.4t","a")
            f.close()
            f = open("commands.4t","w")
            f.write(commands[0])
            f.close()
            for i in range(len(commands)-1):
                f = open("commands.4t","a")
                f.write(","+commands[y])
                f.close()
                y = y+1
            time.sleep(2)
            print("95.0%")
            response7 = requests.get(url+"lastversion.txt")
            f = open("ver.4t","a")
            f.close()
            f = open("ver.4t","w")
            f.write(response7.text)
            f.close()
            print("100.0%")
            return "successful"




    except:
        print("Something went wrong. Check your internet connection")
        return "error"

def login():
    logged = False
    while logged == False:
        username = input("Enter username: ")
        password = input("Enter password: ")
        f = open(cwd+"/users.4t","r")
        uns = f.read().split()
        if username in uns:
            f = open(cwd+"/Users/"+username+"/password.4set")
            pw = f.read()
            if pw == password:
                print("Welcome")
                logged = True
                return username
            else:
                print("Try again")
        else:
            print("Try again")

f = open("back","r")
while f.read() == "":
    print("Welcome to OS! Wait before OS install")
    status = install()
    if status == "successful":
        print("bOS successfully installed")
        f2 = open("back","w")
        f2.write("true")
        f2.close()
    if status == "error":
        print("There was error in install")
        input("Tap ENTER to try again")
    if status == "maintenance":
        print("Maintenance emmute will ends soon. Come back later")
        input("Tap ENTER to try again")
f.close()

try:
    print("Connecting to server...")
    response = requests.get(url+"lastversion.txt")
    response4 = requests.get(url+"emmute.txt")
    response5 = requests.get(url+"startup.txt")
    if response4.text.lower() == "true":
        print("Maintenance emmute in progress. No info for updates")
    else:
        if response.status_code == 200:
            lastver = response.text.split(".")
        else:
            print(f"Error: {response.status_code}")
        with open("ver.4t","r") as f:
            version = f.read().split(".")
        if int(lastver[0]) > int(version[0]) or int(lastver[1]) > int(version[1]):
            print('New version is available! You can update by command "update"')
        startup = response5.text.split(",")
        y = 0
        for i in startup:
            response6 = requests.get(url+startup[y])
            exec(response6.text)
            y = y+1
except:
    print("No info for updates")



def command(command):
    com = command.split(" ")
    com[0] = com[0].lower()
    f = open(cwd+"/commands.4t","r")
    commands = f.read().split(",")
    f.close()
    if com[0] in commands:
        f = open(cwd+"/Commands/"+com[0]+".4com","r")
        
        try:
            try:
                exec(f.read())
            except IndexError:
                print('CommandError 001: "NO NEEDEN ARGUMENT"')
        except:
            print('SystemError 001: "COMMAND CODE GOT CRASHED"')
            f.close()
    elif com[0] == "update" or com[0] == "reinstall" or com[0] == "restart" or com[0] == "server":
        if com[0] == "update":
            f = open(cwd+"/ver.4t","r")
            inp = input("Sure you want to update to last version? After update you wont be able to install earlier version.(Y/n)").lower()
            if inp == "y":
                print("Update started")
                try:
                    st = datetime.datetime.now()
                    status = install()
                    et = datetime.datetime.now()
                    if status == "successful":
                        print(f"Start time:{st}\nEnd time:{et}")
                        print("Updated successfully")
                        print("Restarting in 5 seconds...")
                        time.sleep(5)
                        print("Restarting...")
                        import restart
                    if status == "error":
                        print("Error in update. Try again")
                    if status == "maintenance":
                        print("Maintenance will ends soon. Try again later")
                except:
                    print("No internet connection")
        if com[0] == "reinstall":
            inp = input("Sure you want to reinstall your OS? After reinstall you will update to last version and wont be able to install earlier version.(Y/n)").lower()
            if inp == "y":
                print("Reinstall started")
                st = datetime.datetime.now()
                status = install()
                et = datetime.datetime.now()
                if status == "successful":
                    print(f"Start time:{st}\nEnd time:{et}")
                    print("Reinstalled successfully")
                    print("Restarting in 5 seconds...")
                    time.sleep(5)
                    print("Restarting...")
                    import restart
                if status == "error":
                    print("Error in reinstall. Try again")
                if status == "maintenance":
                    print("Maintenance will ends soon. Try again later")
        if com[0] == "restart":
            inp = input("Sure?(Y/n)").lower()
            if inp == "y":
                print("Restarting in 2 seconds...")
                time.sleep(2)
                import restart

    else:
        print("Incorrect command")
f = open("music.4set","r")
music = f.read()
if music != "none":
    mixer.init()
    mixer.music.load(cwd+"/music/"+music+".mp3")
    mixer.music.play(loops=-1)
f.close()
while True:
    inp = input(f"<{os.getcwd()},string:{string}> Enter your command:")
    command(inp)
    string = string+1