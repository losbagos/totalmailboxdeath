## total mailbox death - ,  .  :3

## a losbagos . d 

#           >>>>> >>>>><<<<< <<<<<

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import time
import tkinter
import tkinter as tk
from tkinter import ttk
import sys
from math import trunc

from settings import *


#          >>>>> >>>>><<<<< <<<<<

# -- ᠃ ⚘᠂ ⚘ ˚ ⚘ ᠂ ⚘ ᠃ definitions ᠃ ⚘᠂ ⚘ ˚ ⚘ ᠂ ⚘ ᠃ -- 
 
options = Options()
driver = webdriver.Chrome()
wait = WebDriverWait(driver,5)



prefs = {
  "download.default_directory": "./",
  "credentials_enable_service": False,
  "profile.password_manager_enabled": False,
  "excludeSwitches": ["disable-popup-blocking"]
}

options.add_experimental_option("prefs", prefs)
options.page_load_strategy = 'none'


tmdApp = tk.Tk()
tmdApp.title('total mailbox death')
tmdApp.geometry('280x200')
tmdApp.configure(background=LightPink, highlightbackground=Pink)
tmdApp.iconbitmap("kitty.ico")

def tmdGoob():
    global shnooEmail
    global shnooFirstname
    global shnooLastname
    shnooEmail= tmdEmail_entry.get() 
    shnooFirstname= tmdName_entry.get()
    shnooLastname= tmdLastName_entry.get()
    tmdWeb()


## ˋ°•*⁀➷ shnooie for all email element variants
def tmdShnooie_email(sn_Email):
    try: 
        driver.implicitly_wait(1)
        sn_Email_element = driver.find_element(By.NAME, sn_Email)
        sn_Email_element.send_keys(shnooEmail)
    except:
            pass # will pass any lieek umm ones it can't find

## ˋ°•*⁀➷ shnooie for all first name element variants
def tmdShnooie_firstName(sn_firstName):
    try: 
        driver.implicitly_wait(1)
        sn_Email_element = driver.find_element(By.NAME, sn_firstName)
        sn_Email_element.send_keys(shnooFirstname)
    except:
            pass
    finally:
        time.sleep(1)

def tmdShnooie_lastName(sn_lastname):
    try: 
        driver.implicitly_wait(1)
        sn_Email_element = driver.find_element(By.NAME, sn_lastname)
        sn_Email_element.send_keys(shnooLastname)
    except:
            pass
    finally:
        time.sleep(1)

# -- ᠃ ⚘᠂ ⚘ ˚ ⚘ ᠂ ⚘ ᠃ -- ᠃ ⚘᠂ ⚘ ˚ ⚘ ᠂ ⚘ ᠃ --  

emaillist = ["email", "EMAIL", "contact[email]"]

def tmdSnorrey_email():
    for i in emaillist:
        tmdShnooie_email(i)
    

# -- ᠃ ⚘᠂ ⚘ ˚ ⚘ ᠂ ⚘ ᠃ -- ᠃ ⚘᠂ ⚘ ˚ ⚘ ᠂ ⚘ ᠃ --  

firstNamelist = ["name", "NAME", "first_name", "FNAME", "firstname"]

def tmdSnorrey_firstName():
    for i in firstNamelist:
        tmdShnooie_firstName(i)

# -- ᠃ ⚘᠂ ⚘ ˚ ⚘ ᠂ ⚘ ᠃ -- ᠃ ⚘᠂ ⚘ ˚ ⚘ ᠂ ⚘ ᠃ --  

lastNamelist = ["lastname", "LNAME", "last_name"]

def tmdSnorrey_lastName():
    for i in lastNamelist:
        tmdShnooie_lastName(i)

# -- ᠃ ⚘᠂ ⚘ ˚ ⚘ ᠂ ⚘ ᠃ turning list.txt into a list ᠃ ⚘᠂ ⚘ ˚ ⚘ ᠂ ⚘ ᠃ --  

my_file = open("list.txt", "r")  # list of all da urls n shiet
data = my_file.read() 
websitesList = data.split("\n")   
# -- ᠃ ⚘᠂ ⚘ ˚ ⚘ ᠂ ⚘ ᠃ opening da website ᠃ ⚘᠂ ⚘ ˚ ⚘ ᠂ ⚘ ᠃ -- 

def tmdWebsite(website):
    driver.get(website)
    print(" ⚘᠂ ⚘ The current url is: " + website)
    tmdSnorrey_email()
    tmdSnorrey_firstName()
    tmdSnorrey_lastName()
    time.sleep(1)

# -- ᠃ ⚘᠂ ⚘ ˚ ⚘ ᠂ ⚘ ᠃ -- ᠃ ⚘᠂ ⚘ ˚ ⚘ ᠂ ⚘ ᠃ -- 

step = trunc(100/len(websitesList))

def tmdWeb():
    for i in websitesList:
        tmdWebsite(i)
        webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()
        time.sleep(2)
        progress.step(step)
        progress.update()


        

# -- ᠃ ⚘᠂ ⚘ ˚ ⚘ ᠂ ⚘ ᠃ -App- ᠃ ⚘᠂ ⚘ ˚ ⚘ ᠂ ⚘ ᠃ -- 

tmdEmail_label = tkinter.Label(tmdApp, text="Email Address", background=LightPink)
tmdName_label = tkinter.Label(tmdApp, text="First Name", background=LightPink )
tmdLastName_label = tkinter.Label(tmdApp, text="Last Name", background=LightPink)

tmdEmail_entry = tkinter.Entry(tmdApp)
tmdName_entry = tkinter.Entry(tmdApp)
tmdLastName_entry = tkinter.Entry(tmdApp)

tmdSubmit_label = tkinter.Label(tmdApp, text="Total Mailbox Death!", background=LightPink)
tmdSubmit_button = tkinter.Button (tmdApp, text="run newsletter spammer", background=Pink, command = tmdGoob)

# TO DO, FIGURE OUT !!!!

def tmdExit():
    driver.close()
    sys.exit("bai bai")


    

tmdExit_button = tkinter.Button(tmdApp, text="Quit Script :3", background=Pink, command=tmdExit)



                             




tmdSubmit_label.grid(row=0, column=0, columnspan=2)

tmdName_label.grid(row=1, column=0)
tmdName_entry.grid(row=1, column=1)

tmdLastName_label.grid(row=2, column=0)
tmdLastName_entry.grid(row=2, column=1)

tmdEmail_label.grid(row=4, column=0)
tmdEmail_entry.grid(row=4, column=1)

tmdSubmit_button.grid(row=6, column=0, columnspan=2, pady=1)

tmdExit_button.grid(row=8, column=0, columnspan=2, pady=2)

#--
progress_label = tkinter.Label(tmdApp, text="Progress Bar!", background=LightPink)
progress_label.grid(row=9, column=0)
progress = ttk.Progressbar(tmdApp, length=100)
progress.grid(row=10, column=0, columnspan=2, pady=1)



tmdApp.mainloop()
