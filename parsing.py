import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = 'https://www.cbr.ru/scripts/XML_daily.asp'
uh = urllib.request.urlopen(url)
data = uh.read()
#print(data)
tree = ET.fromstring(data)

name = tree.findall('.//CharCode')

for naz in name:
    print(naz.text)

summa = tree.findall('.//Value')

for stoim in summa:
    print(stoim.text)

full = {x.text: y.text for x, y in zip(name, summa)}

print(full[input('Введите валюту:').swapcase()])
