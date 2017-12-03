import os
import time
from bs4 import BeautifulSoup
import urllib.request
from urllib.request import urlopen

def extract(url, type, att_key, att_out):
    hdr = {'User-Agent': 'Mozilla/5.0','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
    request = urllib.request.Request(url, headers = hdr)
    page = urllib.request.urlopen(request) #opens page
    soup = BeautifulSoup(page, 'html.parser') #parses HTML in python

    var = soup.find(type, attrs = {att_key:att_out}) #finds specific HTML code in HTML taken from a page
    #or find all types of the atributes: use soup.find(...)
    varstrp = var.text.strip() #strips variable to string data type
    varstrp = str(varstrp)
    return varstrp

def loop_extract(url, type, att_key, att_out, limit, index):
    hdr = {'User-Agent': 'Mozilla/5.0','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
    request = urllib.request.Request(url, headers = hdr)
    page = urllib.request.urlopen(request) #opens page
    soup = BeautifulSoup(page, 'html.parser') #parses HTML in python

    array = soup.findAll(type, attrs = {att_key:att_out, 'role':'heading'}, limit = limit) #finds specific HTML code in HTML taken from a page
    #or find all types of the atributes: use soup.find(...)
    val = array[index].text.strip()
    return val

localtime = time.localtime(time.time())
month = localtime[1]
day = localtime[2]
year = localtime[0]
weekday = localtime[6]


def word_month(month):
    if month == 1:
        global month_word
        month_word = 'January'
    elif month ==2:
        global month_word
        month_word = 'February'
    elif month ==3:
        global month_word
        month_word = 'March'
    elif month ==4:
        global month_word
        month_word = 'April'
    elif month ==5:
        global month_word
        month_word = 'May'
    elif month ==6:
        global month_word
        month_word = 'June'
    elif month ==7:
        global month_word
        month_word = 'July'
    elif month ==8:
        global month_word
        month_word = 'August'
    elif month ==9:
        global month_word
        month_word = 'September'
    elif month ==10:
        global month_word
        month_word = 'October'
    elif month ==11:
        global month_word
        month_word = 'November'
    elif month ==12:
        global month_word
        month_word = 'December'

def ordinal(day):
    if day == 1 or day == 21 or day == 31:
        global ordinal_day
        ordinal_day = str(day) + "st"
    if day == 2 or day == 22:
        global ordinal_day
        ordinal_day = str(day) + 'nd'
    if day == 3 or day == 23:
        global ordinal_day
        ordinal_day = str(day) + 'rd'
    if day == 4 or day == 5 or day == 6 or day == 7 or day == 8 or day == 9 or day == 10 or day == 11 or day == 12 or day == 13 or day == 14 or day == 15:
        global ordinal_day
        ordinal_day = str(day)+'th'
    if day == 16 or day == 17 or day == 18 or day == 19 or day == 20 or day == 24 or day == 25 or day == 26 or day == 27 or day == 28 or day == 29 or day == 30:
        global ordinal_day
        ordinal_day = str(day) + 'th'

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
word_month(month)
ordinal(day)
year = str(year)

print(weekword)
print(month_word + ' ' + ordinal_day + ' ' + year)
#date has printed

temp = extract('https://www.google.com/search?q=weather&oq=weather&aqs=chrome.0.69i59l2j69i60l2j0l2.748j0j7&sourceid=chrome&ie=UTF-8', 'span', 'class', 'wob_t')
#temp has printed
headline1 = loop_extract('https://news.google.com/news/?ned=us&hl=en', 'a', 'class', 'nuEeue hzdq5d ME7ew', 5, 0)
headline2 = loop_extract('https://news.google.com/news/?ned=us&hl=en', 'a', 'class', 'nuEeue hzdq5d ME7ew', 5, 1)
headline3 = loop_extract('https://news.google.com/news/?ned=us&hl=en', 'a', 'class', 'nuEeue hzdq5d ME7ew', 5, 2)
headline4 = loop_extract('https://news.google.com/news/?ned=us&hl=en', 'a', 'class', 'nuEeue hzdq5d ME7ew', 5, 3)
headline5 = loop_extract('https://news.google.com/news/?ned=us&hl=en', 'a', 'class', 'nuEeue hzdq5d ME7ew', 5, 4)
weather = extract('https://search.yahoo.com/search?p=weather&fr=yfp-t&fp=1&toggle=1&cop=mss&ei=UTF-8', 'span', 'class', 'condition')

if weather == 'Rainy':
    need = 'You might need an umbrella!'
elif weather == 'Partly Cloudy':
    need = "Does\'t look too bright outside today!"
elif weather == 'Sunny':
    need = "It's pretty nice outside!"
elif weather == 'Windy':
    need = 'You might need a hat and come gloves!  It is pretty chilly!'
else:
    need = 'It is great outside!'


print(temp)
print(weather)
print(need)

print(headline1)
print(headline2)
print(headline3)
print(headline4)
print(headline5)

x = open('Date.txt','w')
x.write('Welcome to the Daily pie, your trusty personal assistant.')
x.write('Today is ' + weekword + ', ' + month_word + ' ' + ordinal_day + ' ' + year + '.')
x.close()
w = open('Date.txt','r')
print(w.read())
w.close()
z = open('TW.txt', 'w')
z.write('It is ' + temp + ' farenheit outside.  ')
z.write('The weather is ' + weather + '. ')
z.write(need)
z.close()
y = open('TW.txt','r')
print(y.read())
y.close()

head1 = open('news1.txt','w')
head1.write('Here is some breaking news!  The top headlines for today. ')
head1.write(headline1 + '. ')
head1.close()

head2 = open('news2.txt', 'w')
head2.write(headline2 + '. ')
head2.close()

head3 = open('news3.txt', 'w')
head3.write(headline3 + '. ')
head3.close()

head4 = open('news4.txt', 'w')
head4.write(headline4 + '. ')
head4.close()

head5 = open('news5.txt', 'w')
head5.write(headline5 + '. ')
head5.close()


#b = open('news.txt','r')
#print(b.read())
#b.close()

#date, weather, temperature, headlines have printed
