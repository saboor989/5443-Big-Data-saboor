 import redis
import string
import json
import sys

#Link up with redis 
r = redis.StrictRedis(host='localhost', port=6379, db=0)

# Open file for reading

f = open('nutrition.json', 'r')
#f= open('x00', 'r')
# Read one line from file
fout = open('nutrition_clean.json', 'w')
#print >> f, 'Filename:', filename  # or f.write('...\n')
writemd=open('writeup.md','w')


def is_json(myjson):
   try:
      json_object = json.loads(myjson)
   except ValueError, e:
      return False
   return True

count = 0
count2 = 0
for line in f:
    # Filter that line, removing non ascii characters
    # Doesn't identify which, just filters
	if is_json(line):
		count = count + 1
		line = json.loads(filter(lambda x: x in string.printable, line))
		l = json.dumps(line)
		fout.write(l)
	else:
		count2 = count2 + 1
	#if(json.dumps(line, sort_keys=True, indent=4, separators = (',',':'))):
	#	count = count + 1
	#print json.dumps(line, sort_keys=True, indent=4, separators = (',',':'))
		#print >>fout, json.dumps(line, sort_keys=True, indent=4, separators = (',',':'))
	#print line

#print count
#print >> writemd, "### Json File Processing"
#print >> writemd, "### Written by Saboor"
#print >> writemd, "- Total Lines Processed:" xxxxxx
#print >> writemd, "- Total Lines Remove:" xx
#print >> writemd, "- Ratio of Good Vs Bad:" x%

#print >> writemd, "### Bonus"

#print >> writemd, "- Illegal character "?" found on line" xxx

fout.close()
writemd.close()
#db.zipcodes.find({"_id":"02333"},{state:1,_id:0})

#db.zipcodes.find({"pop":{$gt:2000}},{state:1,_id:0})

#db.zipcodes.find({"pop":{$gt:2000,$lt:4000}},{state:1,pop:1,_id:0})
#db.zipcodes.find({loc:{$near:[-98.473206,32.936239],$maxDistance :5}}).limit(20)._addspecial("$orderby",{_id:1})
#list use list for 1 problem .