import requests
from bs4 import BeautifulSoup

url = "https://github.com/OpenDataDE/State-zip-code-GeoJSON"
r = requests.get(url)
soup = BeautifulSoup(r.content.decode("utf-8"),'html.parser')

links = []
for a in soup.find_all('a', href=True):
    if ".min.json" in a['href']: # all geo json in this github repo ends with this suffix
        links.append(a['href'])

url = "https://raw.githubusercontent.com/OpenDataDE/State-zip-code-GeoJSON/master/"
for l in links:
    l = l.split("/")
    r = requests.get(url + l[-1])
    with open(f"{l[-1][:2]}.geo.json","w") as f:
        f.write(r.content.decode("utf-8"))
