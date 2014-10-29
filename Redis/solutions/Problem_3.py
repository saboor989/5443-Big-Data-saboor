import redis
import string
import json
import sys

#Link up with redis 
r = redis.StrictRedis(host='localhost', port=6379, db=0)
r.flushall()
# Open file for reading
#f = open('nutrition_clean.json', 'r')
f = open('x00','r')
# Read one line from file
count = 0
for line in f:
    # Filter that line, removing non ascii characters
    # Doesn't identify which, just filters
	line = json.loads(filter(lambda x: x in string.printable, line))
	l = json.dumps(line)
	#r.sadd("nutrients",line['_id'])
	for nut in line['nutrients']:
		#r.sadd('nutrients',nut['tagname'])
		#r.hset('taghash',nut['_id'],nut['tagname'])
		r.hincrby('taghash', nut['tagname'],1)
	#print json.dumps(line, sort_keys=True, indent=4, separators = (',',':'))
	#print line

#key = r.smembers('nutrients')

#count = 0
#for k in key
#	h.getall(k)
#	count = count + 1

# from here taken sai material help in doing.
len=r.zcard('taghash')
value=r.zrange('taghash',len-5,len)

for nutrient_tag in value:
	list.append(nutrient_tag)

print "### Top 5 most commonly occuring nutrients:"

i = 4
j = 1	
while i >= 0 :
	print j, '. ', list[i], ' occurs ', r.zscore('hashtag',list[i]), 'number of times'
	j += 1
	i -= 1


#print count
#i= 0
#for n in line['nutrients']:
#	if i <= 3:
#		print r.hscan('taghash')
#		i=i+1
	
	
#print r.smembers('nutrients')
#print "unique nutrients", r.scard('nutrients')
#print r.hgetall('taghash')
#print r.hlen('taghash')

#db.zipcodes.find({"_id":"02333"},{state:1,_id:0})

#db.zipcodes.find({"pop":{$gt:2000}},{state:1,_id:0})

#db.zipcodes.find({"pop":{$gt:2000,$lt:4000}},{state:1,pop:1,_id:0})
#db.zipcodes.find({loc:{$near:[-98.473206,32.936239],$maxDistance :5}}).limit(20)._addspecial("$orderby",{_id:1})
#list use list for 1 problem .