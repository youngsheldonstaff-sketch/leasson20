import random
import time

def getrandomdate(startdate,enddate):
    print("random date between ", startdate,"and", enddate)

    randomgen = random.random()
    dateformat = '%m/%d/%Y'

    starttime = time.mktime(time.strptime(startdate,dateformat))

    endtime = time.mktime(time.strptime(enddate,dateformat))



    randomtime = starttime + randomgen *(endtime - starttime)
    randomdate = time.strftime(dateformat,time.localtime(randomtime))
    return randomdate 

    
print("random date is:",getrandomdate("1/1/2016","12/31/2025"))
