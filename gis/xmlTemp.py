import urllib
import xml.etree.ElementTree as ET

serviceurl = raw_input('Enter location: ')
if not serviceurl: serviceurl = 'comments_283746.xml'

print 'Retrieving', serviceurl
uh = urllib.urlopen(serviceurl)
data = uh.read()
info = ET.fromstring(data)

counts = info.findall('name')
dictionary = 0
for i in counts:
    dictionary +=int(i.find('count').text)
print dictionary

#TODO
#Make dictionary from elements in xml file where: key - name, value - count

#print dictionary
