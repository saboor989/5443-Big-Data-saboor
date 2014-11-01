import redis
import sys
import json
import string


f= open('x00', 'r')

r = redis.StrictRedis(host='localhost', port=6379, db=0)

r.flushall()

for line in f:
		line = json.loads(filter(lambda x: x in string.printable, line))
		r.sadd('fooditem',{line['description']})
						

for line1 in f:

		line1 = json.loads(filter(lambda x: x in string.printable, line))
		for nut in line1['nutrients']:
			r.zincrby('taghash',nut['description'],1)

				

item = 'Protein'	
print "the percentage of food items which contain  nutrient:",item

numitems = r.scard('fooditem')
print "Unique Items found:", numitems
itemrep = r.zscore('taghash',item)
print item, ' is occuringoccurs ',itemrep

# to find the percentage x/y*100 gives the x percentage of y.
val=(float(itemrep)/float(itemrep))
p = val*100
print item, "occuring " , p , "percentage of fooditems"