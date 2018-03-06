import requests
import re
import csv
from imdb import IMDb
top250_url = "https://www.imdb.com/list/ls005197923/?sort=list_order,asc&st_dt=&mode=detail&page=1"
r = requests.get(top250_url)
html = r.text.split("\n")
result = []
for line in html:
  line = line.rstrip("\n")
  m = re.search(r'data-tconst="tt(\d+?)">', line)
  if m:
    id = m.group(1)
    result.append(id)
top250_url = "https://www.imdb.com/list/ls005197923/?sort=list_order,asc&st_dt=&mode=detail&page=2"
r = requests.get(top250_url)
html = r.text.split("\n")
for line in html:
  line = line.rstrip("\n")
  m = re.search(r'data-tconst="tt(\d+?)">', line)
  if m:
    id = m.group(1)
    result.append(id)
top250_url = "https://www.imdb.com/list/ls005197923/?sort=list_order,asc&st_dt=&mode=detail&page=3"
r = requests.get(top250_url)
html = r.text.split("\n")
for line in html:
  line = line.rstrip("\n")
  m = re.search(r'data-tconst="tt(\d+?)">', line)
  if m:
    id = m.group(1)
    result.append(id)
result=set(result)
print(len(result))
ia = IMDb()
import inspect
#print(inspect.getmembers(ia))
with open('somefile.txt', 'a') as the_file:
 for v in result:
  st = []
  x=ia.get_movie(v)
#  print(x)
  y=x.get('rating')
  z=x.get('title')
  ac=x['cast']
  print(y)
  print(z)
  if len(ac)>=15 :
   y=str(y)
   the_file.write(z)
   the_file.write(",")
   the_file.write(y)
   for i in range(0,15):
    print(ac[i])
    the_file.write(","+str(ac[i]))
   the_file.write("\n")
 