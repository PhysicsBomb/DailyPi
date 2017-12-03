from bs4 import BeautifulSoup
import urllib.request
from urllib.request import urlopen
import random
import time

url = 'http://www.wisebread.com/47-cheap-fun-things-to-do-this-weekend'
hdr = {'User-Agent': 'Mozilla/5.0','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
request = urllib.request.Request(url, headers = hdr) #defines what to open
page = urllib.request.urlopen(request) #opens page
soup = BeautifulSoup(page, 'html.parser') #parses HTML in python

var = soup.findAll('h3', limit = 46) #attrs = {'h3': "1. Go to the Park."}) #finds specific HTML code in HTML taken from a page
#or find all types of the atributes: use soup.find(...)
#varstrp = var.text.strip() #strips variable to string data type
#now do whatever you want with the given variable
#print(var[1])
var_rand = random.randint(0, 46)
#print(var[var_rand].text.strip())
#varstrp = var[var_rand]
#varstrp = varstrp.text.strip
#print(varstrp)

#prints plan for weekend
localtime = time.localtime(time.time())
weekday = localtime[6]

def weekday_word(weekday):
    if weekday == 0:
        global weekword
        weekword = 'Monday'
    if weekday == 1:
        global weekword
        weekword = 'Tuesday'
    if weekday == 2:
        global weekword
        weekword = 'Wednesday'
    if weekday == 3:
        global weekword
        weekword = 'Thursday'
    if weekday == 4:
        global weekword
        weekword = 'Friday'
    if weekday == 5:
        global weekword
        weekword = 'Saturday'
    if weekday == 6:
        global weekword
        weekword = 'Sunday'

weekday_word(weekday)
if weekword == "Friday" or weekword == 'Saturday' or weekword == 'Sunday':
    #print('Wondering what to do this weekend?  From our list, why not try number ' + var[var_rand].text.strip())
    x = open('plan.txt','w')
    x.write('Wondering what to do this weekend?  From our list, why not try number ' + var[var_rand].text.strip())
    x.write('Thank you for using the daily pie!  Have a great day!')
    x.close()
    y = open('plan.txt','r')
    print(y.read())
    y.close()
