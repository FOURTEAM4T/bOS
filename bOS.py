import os
cwd = os.getcwd()
print("Loading...")
print("""\033[93;1m$-------$$$$$---$$$$---------------------
$------$$---$$-$$------------------------
$$$$---$$---$$--$$$$---$-------$--$-$$$$$
$--$$--$$---$$-----$$--$$-$$---$$$$---$--
$$$$----$$$$$---$$$$---$$-$$------$---$--
---------------------------$------$---$--
#####################-----$--------------\033[0m""")
import requests
import sys
import time
import random
import datetime
import zipfile
import shutil
import webbrowser
import plyer
from locale import currency
import platform
import atexit
import glob
import importlib
import sys
import logging
import keyboard
from ping3 import ping, verbose_ping
import json

def add_file(zip_path, file_to_add, arcname=None):
    if arcname is None:
        arcname = os.path.basename(file_to_add)
    with zipfile.ZipFile(zip_path, 'a') as zipf:
        zipf.write(file_to_add, arcname)

version = []
string = 0
url = "http://fourteam4t.temp.swtest.ru/"
#url = "http://bosstageserver.com.swtest.ru/"
f = open(cwd+"/modules.4set","r")
modules = f.read()
nothing = ""
modules = modules.split(",")
if nothing in modules:
    removing = True
    while removing == True:
        modules.remove(nothing)
        if not nothing in modules:
            removing = False
y = 0
for i in modules:
    __import__(modules[y])
    y = y + 1

print("\033[92;1mLoaded successfully\033[0m")



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
    print("Connecting to server...",end = "\r")
    response = requests.get(url+"lastversion.txt")
    response4 = requests.get(url+"emmute.txt")
    response5 = requests.get(url+"startup.txt")
    response7 = requests.get(url+"lastavver.txt")
    if response4.text.lower() == "true":
        print("Maintenance emmute in progress. No info for updates")
    else:
        update = False
        lastver = response.text.split(".")
        lastavver = response.text.split(".")
        with open("ver.4t","r") as f:
            version = f.read().split(".")
        if int(lastver[0]) > int(version[0]) or int(lastver[1]) > int(version[1]):
            print('New version is available! You can update by command "update"')
            update = True
        startup = response5.text.split(",")
        y = 0
        for i in startup:
            response6 = requests.get(url+startup[y])
            exec(response6.text)
            y = y+1
        if update == False:
            print("\033[92;1mSuccessfully connected to server\033[0m")
except:
    plyer.notification.notify(message="bOS Enter System notification:\nCheck your internet connection. Application may have updates",app_name="bOS Enter system",app_icon=cwd+"\\Res\\bOSappicon.ico",title = "Connection failed")
    print("\033[91;1mError while connecting to server\033[0m")



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
            print('SystemError 001: "COMMAND GOT CRASHED"')
            f.close()
    elif com[0] == "update" or com[0] == "reinstall" or com[0] == "restart" or com[0] == "server" or com[0] == "install":
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
        if com[0] == "install":
            print("Don't close your bOS while proccesing!")
            time.sleep(2)
            print("Installing...")
            f = open(cwd+f"/{com[1]}/displayname.4set","r")
            name = f.read().strip("\n")
            print("Setting up...")
            f.close()
            f = open(cwd+"/"+com[1]+"/setup.bscript","r")
            exec(f.read())
            print("Finishing...")
            """
            add_file(cwd+"/_internal/base_library.zip",cwd+"/"+com[1]+"/"+name+".bapp",name+".pyc")
            """
            shutil.move(cwd+"/"+com[1]+"/"+name+".bapp",cwd+"/"+name+".py")
            f = open(cwd+"/modules.4set","a")
            f.write(","+name)
    else:
        y = 0
        ans = False
        for i in modules:
            im = modules[y]
            im2 = importlib.import_module(im)
            ans = im2.main(com)
        if ans:
            pass
        if ans == False:
            print("\033[91;1mIncorrect command\033[0m")
string = 1
while True:
    if len(os.getcwd().split("\\")) <= 4:
        inp = input(f"<{os.getcwd()},string:{string}> $ ")
    else:
        inp = input(f'<{os.getcwd().split("\\")[0]}/.../{os.getcwd().split("\\")[-3]}/{os.getcwd().split("\\")[-2]}/{os.getcwd().split("\\")[-1]}/>')
    command(inp)
    string = string+1
