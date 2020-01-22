def main():
    
    import datetime # Get the datetime module    
    with open('daylighthours.txt', 'r') as f: # datafile
        searchlines = f.read() # pass in the content to search
        timeFormat = '%d %B %Y, %A' # Match the time format from the txt document
        timeNow = datetime.datetime.now().strftime(timeFormat) # Mark todays date
        
        if timeNow in searchlines: # if todays date is in searchlines do something
            TODAY= searchlines.index(timeNow)
            TIMEDELTA= (datetime.date.today() + datetime.timedelta(days=1)).strftime(timeFormat)
            TOMORROW= searchlines.index(str(TIMEDELTA))
            search_index= searchlines[TODAY:TOMORROW:].replace('\n', ' ')
            INDEX_START= len(timeNow)
            search_results= search_index[INDEX_START::].strip(' ')
            sunrise  = search_results[:5:] 
            sunset   = search_results[6:11:]
            daylight = search_results[12:17:] 
    
    

    return [sunrise, sunset, daylight]