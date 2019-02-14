import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import random
import json

url = 'https://simple.wikipedia.org/wiki/List_of_European_countries'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')
My_table = soup.find('table')
rows = My_table.findAll('tr')
data = []
for row in rows:
    cols = row.findAll("td")
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])
# Last two lines: I understand what they do, but I cant write them like for loop without sqere brackets

capitals = []
for item in data:
    if len(item)<1: continue
    if item[0]=='Kosovo[a]':continue # yet not solved status
    if item[4]=='Belgrade':continue
    capitals.append(item[4])
print(capitals)

destinations = ''
for i in range(10):
    dest_city = random.choice(capitals)
    capitals.remove(dest_city)
    destinations += '|' + dest_city

parms = {}
parms['origins']='Belgrade'
parms['destinations']= destinations
parms['key']= YOUR API KEY

service_url = 'https://maps.googleapis.com/maps/api/distancematrix/json?'
url = service_url + urllib.parse.urlencode(parms)
uh = urllib.request.urlopen(url)
distances = uh.read().decode()

js = json.loads(distances)
# print(js['rows'][0]['elements'])
distances = 0
durations = 0
for i in range(10):
    distance_km = js['rows'][0]['elements'][i]['distance']['text']
    distance = distance_km[:-3].replace(',','')
    distances += float(distance)
    # print(distance, distance_km)
print('Averige distance is ',distances/10,' km.')
