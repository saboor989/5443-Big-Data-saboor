import redis
import string
import json
import sys

#Link up with redis 
r = redis.StrictRedis(host='localhost', port=6379, db=0)

# Open file for reading

#f = open('GpsFilePoints.csv', 'r')
#f= open('x00', 'r')
# Read one line from file

# Filter that line, removing non ascii characters
# Doesn't identify which, just filters
    #json.loads(filter(lambda x: x in string.printable, f))
    # json.dumps(f)
        # print json.dumps(f, sort_keys=True, indent=4, separators = (',',':'))
	#print line

	
	
# i found it on the site 
file = open('GpsFilePoints.yml')
data = yaml.load(file)
print json.dumps(data, sort_keys=True,indent=4, separators=(',', ': '))
		
		
#yml to json code i found
#-------------------------
#http://yamltojson.com/#python
#import yaml
#import json
#yml = """
#---
#  foo: bar
#"""
#data = yaml.load(yml)
#json = json.dumps(data)

#print(json)


#db.zipcodes.find({"_id":"02333"},{state:1,_id:0})

#db.zipcodes.find({"pop":{$gt:2000}},{state:1,_id:0})

#db.zipcodes.find({"pop":{$gt:2000,$lt:4000}},{state:1,pop:1,_id:0})
#db.zipcodes.find({loc:{$near:[-98.473206,32.936239],$maxDistance :5}}).limit(20)._addspecial("$orderby",{_id:1})
#list use list for 1 problem .