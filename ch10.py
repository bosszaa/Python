import re
from urllib import request
# HTTPResponse
f = request.urlopen('http://fivedots.coe.psu.ac.th')
 
# New List
lst = []
lst = f.read().decode('utf‐8').split('\n')
 
# Get line 32-77 to new raw list
rlist = []
for i in range(len(lst)):
    if ((i > 30) & (i < 77)):
        rlist.append(lst[i])
 
# Extract Title, Name and Lastname from rawlist
nlist = []
tmp = ""
for i in range(len(rlist)):
    tmp = re.match(".*>((?:\w+. \w+ \w+)|(?:\w+ \w+))", rlist[i])
    if tmp:
        print('{0:02}: '.format( i-2),tmp.group(1).replace(" ", ""))
        nlist.append(tmp.group(1).replace("Dr. ", ""))

print(nlist)