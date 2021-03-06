from __future__ import print_function
from datetime import datetime
import curses                                                                
from curses import panel                                                     
import time
import ssl
import re
import readline
import threading
import sys
#import requests
import json
import os
from pprint import pprint
import signal,random, getpass
import urlparse, argparse
import pkg_resources
#Counters and Toggles
import readline
import codecs
import unicodedata
import rlcompleter
import random, shlex, atexit
import platform, time, calendar
import quan
import world
import bitcoin
from menus import Menus

arg_count = 0
no_auth = 0
database_count = 0
ddb_count = 0
hist_toggle = 0
prompt_r = 0


        
#For tab completion
COMMANDS = sorted(["menus","bitstamp-price",'list-countries','quan-dl-db','News','quan-stock-price'])

#For X number of arguements
ONE = ['list-countries',"bitstamp-price",'quan-stock-price']
TWO = ['bitstamp-price','quan-stock-price']
THREE = ['quan-dl-db','esx-change-cd']
FOUR = ['domain-resource-create']
FIVE = ['domain-resource-create']
SIX = ['linode-disk-dist']
#For what class
ADNET= ['search-for-name']
QUAN= ['quan-dl-db','quan-stock-price']
HELPER = ['hidden','?','help',"menus", 'quit', 'exit','clear','ls', 'version', 'qotd']
BC = ["bitstamp-price"]
WORLD = ['list-countries']
for arg in sys.argv:
    arg_count += 1

#warnings are ignored because of unverified ssl warnings which could ruin output for scripting
import warnings
warnings.filterwarnings("ignore")



#These are lists of things that are persistent throughout the session
username=''
details = {}
def complete(text, state):
        for cmd in COMMANDS:
                if cmd.startswith(text):
                    if not state:
                        return cmd
                    else:
                        state -= 1


#os expand must be used for 
config_file = os.path.expanduser('~/.um')
hist_file = os.path.expanduser('~/.trash_history')
buff = {}
hfile = open(hist_file, "a")
if os.path.isfile(config_file):
    config=open(config_file, 'r')
    config=json.load(config)
else:
    username = raw_input("Username:")
    password = getpass.getpass("Password:")
    #vcenter = raw_input("VCenter Server (ex: company.local):")
    #sat_url =raw_input("Satellite Server Url (ex: https://redhat/rhn/rpc/api):")
    #jump =raw_input("Jump Server(IP or DNS):")
    quandl_key = getpass.getpass("quandl-key:")
    #api_key = linode_api_key 

    config= {"default":[{"username":username,"password":password, "quandl-key":quandl_key}]}
    
    config_file_new = open(config_file, "w")
    config_f = str(config)
    config_f = re.sub("'",'"',config_f)
    config_file_new.write(config_f)
    config_file_new.close 

#Ending when intercepting a Keyboard, Interrupt
def Exit_gracefully(signal, frame):
    #hfile.write(buff)
    sys.exit(0)



#DUH
def get_sat_key(config):
    signal.signal(signal.SIGINT, Exit_gracefully)
    #global username
    username = config["default"][0]["username"]
    password = config["default"][0]["password"]
    #sat_url = config["default"][0]["sat_url"]
    #vcenter = config["default"][0]["vcenter"]
    #lkey = config["default"][0]["Linode-API-Key"]
    quandl_key = config["default"][0]["quandl-key"]
    key={}
    key['username']=username
    key['password']=password
    key['quandl-key'] = quandl_key
    #key['platform']=ucommands.os_platform()
    #key['vcenter']=vcenter
    #key['si']=None
    #key['Linode-API-Key']=lkey
    #if sat_url:

        #if platform.python_version() == '2.6.6':
            #key['client'] = xmlrpclib.Server(sat_url, verbose=0)
        #else:
            #key['client'] = xmlrpclib.Server(sat_url, verbose=0,context=ssl._create_unverified_context())
        

        #key['key']=key["client"].auth.login(username, password)
    #else:
        #key['client'] = ''
    #key['jump'] = config["default"][0]["jump"]
    try:
        return(key)
    except KeyError:
        print("Bad Credentials!")
        os.unlink(config_file)
        bye()
    return(key)

    

um_p = 'um$ '

#main command line stuff
def cli():
    while True:
        valid = 0

        signal.signal(signal.SIGINT, Exit_gracefully)
        try:
            if 'libedit' in readline.__doc__:
                readline.parse_and_bind("bind ^I rl_complete")
            else:
                readline.parse_and_bind("tab: complete")

            readline.set_completer(complete)
            readline.set_completer_delims(' ')
            cli = str(raw_input(PROMPT))
        except EOFError:
            bye()
        if hist_toggle == 1:
            hfile.write(cli + '\n')
        if 'key' in locals():
            pass
        else:
            key = get_sat_key(config)    

#This is not just a horrible way to take the commands and arguements, it's also shitty way to sanatize the input for one specific scenario

#I miss perl :(


        cli = re.sub('  ',' ', cli.rstrip())
            



##########################################################################################
# This starts the single trash commands
#######################################################################################
        buff = str({calendar.timegm(time.gmtime()) : cli})
        #api_key = get_sat_key(config)
        #Write try statement here for error catching
        command = cli.split(' ', 1)[0]

        if command in QUAN:
            l_class = 'quan'
        elif command in BC:
            l_class = "bitcoin"
        elif command in WORLD:
            l_class = "world"
        else:
            l_class = ''
        
        
        if len(cli.split(' ')) > 0:
            if len(cli.split(' ')) ==6:
                command,arg_one,arg_two,arg_three,arg_four,arg_five = cli.split()
                if command in SIX:
                    command = command.replace("-", "_")
                    l_class = eval(l_class)
                    result = getattr(l_class, command)(api_key, arg_one, arg_two,arg_three,arg_four,arg_five)
                    print(result)
                    valid = 1

            if len(cli.split(' ')) ==5:
                command,arg_one,arg_two,arg_three,arg_four = cli.split()
                if command in FIVE:
                    command = command.replace("-", "_")
                    l_class = eval(l_class)
                    result = getattr(l_class, command)(api_key, arg_one, arg_two,arg_three,arg_four)
                    print(result)
                    valid = 1

            if len(cli.split(' ')) ==4:
                command,arg_one,arg_two,arg_three = cli.split()
                if command in FOUR:
                    command = command.replace("-", "_")
                    l_class = eval(l_class)
                    result = getattr(l_class, command)(api_key, arg_one, arg_two,arg_three)
                    print(result)
                    valid = 1

            if len(shlex.split(cli)) ==3:
                command,arg_one,arg_two = shlex.split(cli)
                if command in THREE:
                    command = command.replace("-", "_")
                    if l_class == 'vmutils':
                        l_class = eval(l_class)
                        result = getattr(l_class, command)(api_key, si, arg_one, arg_two)
                    else:
                        l_class = eval(l_class)
                        result = getattr(l_class, command)(api_key, arg_one, arg_two)
 
                    print(result)
                    valid = 1

            elif len(shlex.split(cli)) ==2:
                command,arguement = shlex.split(cli)
                if command in TWO:
                    command = command.replace("-", "_")
                    if l_class == 'vmutils':
                        api_key['vmarg'] = arguement
                        l_class = eval(l_class)
                        result = getattr(l_class, command)(api_key, si)
                    else:
                        l_class = eval(l_class)
                        result = getattr(l_class, command)(api_key, arguement)
                    print(result)
                    valid = 1
                
                else:
                    print("Invalid Arguements")

            else:
               if cli in ONE:
                    cli = cli.replace("-", "_")
                    
                    if l_class == 'vmutils':
                        l_class = eval(l_class)
                        result = getattr(l_class, cli)(api_key, si)
                        pprint(result)
                        valid = 1
                    else:    
                        l_class = eval(l_class)
                        result = getattr(l_class, cli)(api_key)
                        pprint(result)
                        valid = 1
               elif cli in HELPER:
                    if cli == "quit" or cli == "exit":
                        #hfile.write(buff)
                        hfile.close()
                        bye()
                    if cli == "version":
                        print(version())
                        valid = 1
                    if cli == "hidden":
                        print(hidden_menu())
                        valid = 1
                    if cli == "menus":
                        #print(ls_menu())
                        curses.wrapper(ManMenu)   
                        valid = 1
                    if cli == "money":
                        #print(ls_menu())
                        curses.wrapper(MoneyMenu)   
                        valid = 1
                    if cli == "qotd":
                        print(qotd_menu())
                        valid = 1
                    if (cli == "help") or (cli == "?"):
                        print(help_menu())
                        valid = 1
                    if cli == "clear":
                        if ucommands.os_platform() == 'windows':
                            print(os.system('cls'))
                            valid = 1
                        if ucommands.os_platform() == 'nix':
                            #pprint(
                            os.system('clear')
                            valid = 1
               else:
                    print("Invalid Command")

    

        if valid == 0:
            print("Unrecoginized Command")


def help_menu():
####Why did I space the help like this, cause something something, then lazy
    help_var = """
No Help currently Available

"""
    return(help_var)


def hidden_menu():
    hidden_var = """
No Hidden Commands Currently Available
"""
    return(hidden_var)



def version():
    version = pkg_resources.require("trash")[0].version
    return version

def bye():
    exit()

if arg_count == 2:
    command = sys.argv[1]
#noauth is essentially for testing
    if command == "noauth":
        no_auth = 1
#history is to toggle writing a history file, there is currently no clean up so it is off by default
    if command == "history":
        hist_toggle = 1
    if command == "roulette":
        rando = random.randint(1, 3)
    if command == "extra":
        trash_p = config["default"][0]["prompt"]

                 
PROMPT = um_p + '> '

if no_auth == 1:
    api_key =0
else:
    api_key = get_sat_key(config)




class ManMenu(object):

  def __init__(self, stdscreen):                                           
    screen = stdscreen                                              
    curses.curs_set(0)                                                   
    submenu_items = [                                                    
        ('turd', curses.beep),                                       
        ('crap', curses.flash)                                      
    ]                                                            
    submenu = Menus(submenu_items, screen)                           

    main_menu_items = [                                                  
        ('beep', curses.beep),                                       
        ('flash', curses.flash),                                     
        ('submenu', submenu.display)                                 
    ]                                                            
    main_menu = Menus(main_menu_items, screen)                       
    main_menu.display()                                                  

class MoneyMenu(object):

  def __init__(self, stdscreen):                                           
    screen = stdscreen                                              
    curses.curs_set(0)                                                   
    submenu_items = [                                                    
        ('fb', curses.beep),                                       
        ('wiki', curses.flash)                                      
    ]                                                            
    submenu = Menus(submenu_items, screen)                           

    main_menu_items = [                                                  
        ('things', curses.beep),                                       
        ('stocks', curses.flash),                                     
        ('money', submenu.display)                                 
    ]                                                            
    main_menu = Menus(main_menu_items, screen)                       
    main_menu.display()                                                  

 
