import googlemaps
from datetime import datetime
from bs4 import BeautifulSoup
import urllib.request
from urllib.request import urlopen
import random
import time


url = 'http://dailypi.tech/DailyPisubmitted.html'
hdr = {'User-Agent': 'Mozilla/5.0','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
request = urllib.request.Request(url, headers = hdr) #defines what to open
page = urllib.request.urlopen(request) #opens page
soup = BeautifulSoup(page,'html.parser') #markup_type=''#parses HTML in python
home = soup.findAll('p')#finds specific HTML code in HTML taken from a page
homestrp = home[3].text.strip()
away = home[4].text.strip()

gmaps = googlemaps.Client(key='AIzaSyCgBrq2Bk1W7YPnu2JFXKOL_1kGoRk2jjQ')

now = datetime.now()

departure_location = homestrp
destination_location = away

directions_result = gmaps.directions(departure_location, destination_location, mode = "driving", departure_time=now)

#print(directions_result)

d = directions_result[0]['legs'][0]['distance']['text']
t = directions_result[0]['legs'][0]['duration']['text']

t_new = t.split()[0]


x = open('maps.txt','w')
x.write('Due to traffic conditions, your travel time to your workplace is ' + t_new + ' minutes. ')
x.close()
y = open('maps.txt','r')
print(y.read())
y.close()
