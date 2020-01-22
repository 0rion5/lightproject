#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Thu Nov  7 22:46:45 2019

@author: dalikali
"""

from time import sleep as s # Import sleep as s
import datetime as dt # import datetime module
from os import system # use system to clear the console
import RPi.GPIO as GPIO

pin= 8 # GPIO pin for the light
GPIO.setwarnings(False) # shut off warnings
GPIO.setmode(GPIO.BOARD) # Use physical board numbers
GPIO.setup(pin, GPIO.OUT) # Set the pin to output
GPIO.output(pin, False) # Initialize in the off configuration
system('gpio -1 mode 8 out')
def on():
    system('gpio -1 write 8 0')



def off():
    system('gpio -1 write 8 1 ')


def destroy():
    GPIO.output(pin,False)
    GPIO.cleanup()

def Main():
    
    import datetime # Get the datetime module    
    f= open('/home/pi/light/daylighthours.txt', 'r') # datafile
    searchlines= f.read() # pass in the content to search
    timeFormat = '%d %B %Y, %A'
    timeNow= datetime.datetime.now().strftime(timeFormat)
    
    if datetime.datetime.now().strftime(timeFormat) in searchlines:
        a= searchlines.index(timeNow)
        b= (datetime.date.today() + datetime.timedelta(days=1)).strftime(timeFormat)
        b= searchlines.index(str(b))
        search_index= searchlines[a:b:].replace('\n', ' ')
        a= len(timeNow)
        search_results= search_index[a::].strip(' ')
        sunrise  = search_results[:5:] 
        sunset   = search_results[6:11:]
        daylight = search_results[12:17:] 
    
    f.close()

    return [sunrise, sunset, daylight]

def loop(*args):

    data= Main()# Initialize readfile
    M  = '00:00' # Midnight
    TF = '%H:%M' # Time Format
    b = (dt.datetime.strptime(data[0],TF)- dt.datetime.strptime(M,TF)).seconds # Morning/OFF
    c = (dt.datetime.strptime(data[1],TF)- dt.datetime.strptime(M,TF)).seconds # Evening/ON

    while True:

        a = (dt.datetime.strptime(dt.datetime.now().strftime(TF),TF )- dt.datetime.strptime(M,TF)).seconds

        if dt.datetime.now().strftime(TF) == M:

            data= Main()
            b = (dt.datetime.strptime(data[0],TF)- dt.datetime.strptime(M,TF)).seconds # Morning/OFF
            c = (dt.datetime.strptime(data[1],TF)- dt.datetime.strptime(M,TF)).seconds # Evening/ON
            s(60)
            continue

        elif a < b or a > c:

            todayDate= dt.datetime.now().strftime('%d %B %Y, %A')
            timeNow= dt.datetime.now().strftime('%I:%M:%S %p')
            print('''
            {}
            {}
            The light is on.
            '''.format(todayDate, timeNow))
            on()
            s(1)
            system('clear')
        else:

            todayDate= dt.datetime.now().strftime('%d %B %Y, %A')
            timeNow= dt.datetime.now().strftime('%I:%M:%S %p')
            print('''
            {}
            {}
            The light is off.
            '''.format(todayDate, timeNow))
            off()
            s(1)

try:

    if __name__ == '__main__':
        loop()

except KeyboardInterrupt:
    destroy()
