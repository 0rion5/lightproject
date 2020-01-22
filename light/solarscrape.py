#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 11:02:51 2019

@author: dalikali
"""

from selenium import webdriver # Get webdriver from selenium package
from selenium.webdriver.chrome.options import Options# Get some options to configure
from bs4 import BeautifulSoup as soup# Get BeautifulSoup to parse the browser.page_source
import os# Get the os involved
from datetime import datetime as dt# Get the datetime Module

homeDir= os.path.expanduser("~")# Get home directory
filePath= homeDir + '/Desktop/'# Make a save path
fileName= 'daylighthours.txt'# Give it a file name  

try: # Test to see if file exists
    if not os.system('test -f '+filePath+fileName) == 0: # If no file exists
        os.system('touch '+filePath+fileName) # Make a file exist with touch by concatenating filename to the filePath 
    else: # Else the file does exist just pass
        pass       
except Exception:
    pass        

for year in range(2019, 2035):
    month=['january',
           'february',
           'march',
           'april',
           'may',
           'june',
           'july',
           'august',
           'september',
           'october',
           'november',
           'december']
    #year= input('What year is it now? :')
    for i,v in enumerate(month):

          
        options= Options()# Get the selenium.webdriver.chrome.options Options() funtion.
        options.headless= True# Get the headless option (True= no display, False= display)
        url='https://www.sunrise-and-sunset.com/en/sun/canada/lac-la-biche/'+str(year)+'/'+month[i]# Get url to open
        browser= webdriver.Chrome(options=options)# Get a browser to open the url
        browser.get(url)# Open the url with the browser object
        data= list()# Make a list to store the loot in 
        stew= soup(browser.page_source, 'html.parser')# Get the html stored into a variable called stew
        table= stew.find('div',{'class':'col-sm-7 col-md-8'}).findAll('tr')# Get the data we want
        TF= '%d %B %Y, %A'
        
        # Enumerate the data and format it
        for i,v in enumerate(table):
            td= table[i].findAll('td')
            data.append([_.text.strip('\n\t ') for _ in td])
         
        for i,v in enumerate(data):    
            if not len(data[i]) == 4:
                data.remove(data[i])
            if len(data[0]) == 0:
                data.remove(data[i])
            try:
                d= dt.strptime(data[i][0], TF)
                data[i][0]= d.date().strftime(TF)
                print(data[i][0])
            except IndexError:
                pass
                
        # Write the loot to file
        with open(filePath+fileName,'+a') as f:
            for i,v in enumerate(data): 
                for _ in data[i]:
                    print(_, file=f)
        browser.close()   