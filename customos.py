"""
this is customos.py and made by givemetocode
github: givemetocode-net-hk/customOSopensource

"""

import sqlite3
import yaml
import customcli as gcli
import rich
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from newfile import userlogin #main
from newfile import boisboot #main
import os
from datetime import datetime
import platform
import requests

def setup_setupdb():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def setup_usersignup(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        print("User signed up successfully!")
    except sqlite3.IntegrityError:
        print("Username already exists.")
    finally:
        conn.close()

def setup():
    setup_setupdb()
    print("Setup Your System")
    print("Part A=User Sign up")
    setup_usersignup(Prompt.ask("Your Username "), Prompt.ask("Your Password "))
    print('Part B=PC settings')
    # Read the config.yaml
    with open('config.yaml', 'r') as yaml_file:
        config = yaml.safe_load(yaml_file)
    # Update the settings
    config['settings']['name'] = Prompt.ask('Your customOS Name ')
    config['settings']['timezone'] = Prompt.ask("Your timezone {e.g. UTC+8, UTC+9, etc.} ")
    # Write the changes to the file
    with open('config.yaml', 'w') as yaml_file:
        yaml.dump(config, yaml_file, default_flow_style=False)
        return print("Please Reboot your Device")
def console(loginusername, pcname) :
	while True: 
		command = input(loginusername + "@" + pcname + " ~$ ")
		if command == "help" :
			table = Table(title="How To Use?")
			table.add_column("command", justify="right", style="cyan", no_wrap=True)
			table.add_column("Can", style="magenta")
			table.add_row("help", "go to there")
			table.add_row("logout", "logout device")
			table.add_row("shutdown", "close your device")
			table.add_row("reboot", "reboot device")
			#if you want to add command please use table.add_row("{command}", "{function})
			console = Console()
			console.print(table)
			gcli.wget(homepath)
		if command == "logout" :
			userlogin(input("Your Username: "), input("Your Password: "))
		if command == "shutdown" :
			quit()
		if command == "reboot" :
			boisboot()
		if command == "reset" :
			os.remove("users.db")
			print("done.")
