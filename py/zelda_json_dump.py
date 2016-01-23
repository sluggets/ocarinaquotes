# zelda_json_dump.py
# takes txt file dump from ocarina of time dialogue
# and strips it down to a relatively clean javascript
# array
import json

f = open('newzelda.txt', 'r')

rawlist = f.readlines()

newlist = []

megalist = []

tempstr = ""

# weeds out strings that have non-ascii characters
# and appends to new list
for x in rawlist:
    if ('\xe2' not in x):
        newlist.append(x)

# takes the new list and creates a string where quotes
# are delineated by asterix
# also strips the newlines out
for x in newlist:
    if ('_' in x):
        tempstr += '*'
    else:
        tempstr += x.strip() + ' '

# quotes can be extracted back out into another
# list using the asterix delimiter
megalist = tempstr.split('*')

# remove empty strings
for x in megalist:
    if (x == ' '):
        megalist.remove(x)

flist = []

# strip spaces at end of strings
for x in megalist:
    flist.append(x.rstrip())

f.close()

# dump to json
json.dump(flist, fp=open('zeldadump.json', 'w'), indent=4)

