import datetime 
import calendar 
  
def day(id): 
    
    information = datetime.datetime.strptime(id, '%d %m %Y').weekday() 
    return (calendar.time_day[information]) 

id = '23 08 2022'
print(day(id)) 