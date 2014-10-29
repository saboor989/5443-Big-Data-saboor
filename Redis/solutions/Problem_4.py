import redis
import sys
import json
import string


# taken sai help in doing the problem
f= open('x00', 'r')

r = redis.StrictRedis(host='localhost', port=6379, db=0)

r.flushall()

for line in f:

    # Filter that line, removing non ascii characters
    # Doesn't identify which, just filters
		line = json.loads(filter(lambda x: x in string.printable, line))
		
	
		r.sadd('fooditems',{line['description']})
	
		for nut in line['nutrients']:
				r.zincrby('hashtag',nut['description'],1)


item = 'Protein'	
numitems = r.scard('fooditems')
itemrep = r.zscore('hashtag',item)
print "### Percentage of food items contain ",item," nutrient:"
print "> Unique Items:", numitems
print "> ",item, ' occurs ',itemrep,' times'

p = (float(itemrep)/float(itemrep))*100
print "> ",item, " occurs in " , p , "% number of food items."