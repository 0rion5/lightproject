#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun, Apr 20, 2020 11:30:47 PM
@author: 0rion5 B3lt
"""
import pandas as pd
import requests
from bs4 import BeautifulSoup
import datetime as dt
from time import sleep as s
from os import system


class Light:

    
    def __init__(self, file_name):
        self.file_name   =  file_name  # Give it a file name
        self.time_format =  '%I:%M %p'
        self.date_format =  '%a, %B %d %Y'
        self.mid_night   =  '12:00 AM'
        system('gpio -1 mode 8 out')

    
    @property
    def time(self):
        return dt.datetime.now().strftime(self.time_format)

    @property
    def time_now_seconds(self):
        return (dt.datetime.strptime(self.time, self.time_format)
                - dt.datetime.strptime(self.mid_night, self.time_format)).seconds

    @property
    def date(self):
        return dt.datetime.now().strftime(self.date_format)

    def on(self):
        return system('gpio -1 write 8 0')

    def off(self):
        return system('gpio -1 write 8 1')

    def setup(self):
        """collects the sunrise and sunset times for lac la biche from 2020 to 2044."""
        for year in range(2020, 2045):
            # for month in range(int(dt.datetime.now().strftime('%m')), int(dt.datetime.now().strftime('%m'))+1):
            for month in range(1, 13):
                url = 'https://dateandtime.info/citysunrisesunset.php?id=6028050&month=' + \
                    str(month)+'&year='+str(year)
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
                response = requests.get(url, headers=headers)
                soup = BeautifulSoup(response.content, 'lxml')
                response.close()
                dfs = pd.read_html(str(soup))
                for i, row in enumerate(list(dfs[1].Date.Date)):
                    row_items = row.split()
                    if len(row_items[2]) < 2:
                        row = row_items[0]+' '+row_items[1]+' '+row_items[2].zfill(2)
                    with open(self.file_name, 'a') as text_file:
                        text_file.write(row+' '+str(year)+'\n')
                        text_file.write(
                            str(list(dfs[1].Sun.Sunrise)[i].zfill(8)+'\n'))
                        text_file.write(
                            str(list(dfs[1].Sun.Sunset)[i].zfill(8)+'\n'))
   

    @property
    def read_file(self):
        """Reads the text document created by the setup method and returns the sunrise and sunset times for the current day"""
        with open(self.file_name, 'r') as text_file:  # datafile
            searchlines = text_file.read()  # read the text doc into a variable
        
        TODAY = searchlines.index(self.date)  # Get the index number of the current day
        TIMEDELTA = (dt.date.today() + dt.timedelta(days=1)).strftime(self.date_format) # Gets tomorrows date to index
        TOMORROW = searchlines.index(str(TIMEDELTA)) # Get the index number of day following the current day
        search_index = searchlines[TODAY:TOMORROW:] # Get the data in between the two index numbers acquired today and tomorrow
        search_results = search_index[len(self.date)::] # Get a string of the sunrise and sunset times
        
        sunrise_seconds = (dt.datetime.strptime(search_results[1:9:], self.time_format)
                           - dt.datetime.strptime(self.mid_night, self.time_format)).seconds  # slices the sunrise time and turns it into seconds

        sunset_seconds = (dt.datetime.strptime(search_results[10:18:], self.time_format)
                          - dt.datetime.strptime(self.mid_night, self.time_format)).seconds # slices the sunset time and turns it into seconds

        return [sunrise_seconds, sunset_seconds]

    
    def loop(self):
        try:
            while self.time_now_seconds < self.read_file[0] or self.time_now_seconds > self.read_file[1]:
                self.on()
                print('{} {}\nThe light is on.'.format(self.date, self.time))
                s(59)
            # Day
            else:
                self.off()
                print('{} {}\nThe light is off. '.format(self.date, self.time))
                s(59)
        except KeyboardInterrupt:
            print('Loop has been broken.')


# Program Starts Here
if __name__ == "__main__":
    fileName = 'sunrise-and-sunset-times.txt'
    light = Light(fileName)
    #light.setup()
    light.loop()
