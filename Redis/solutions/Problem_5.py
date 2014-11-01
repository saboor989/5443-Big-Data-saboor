import redis
import string
import json
import sys

r = redis.Redis(host='localhost', port=6379, db=0)


#f = open('Nutrition_clean.json','r')
f=open('x00.json','r')

r.flushall()

def totalmemoryfunction():
	memory_info=str(r.info())
	memory_info=memory_info.replace('\'','"')
	if is_json(str(memory_info)):
		memory_val=json.loads(filter(lambda x: x in string.printable, memory_info))
	    print "Memory used to perform the opeations are: ", memory_val['used_memory']


for line in f:
		line = json.loads(filter(lambda x: x in string.printable, line))
		for nut in line['nutrients']:
			r.sadd("nutri",nut['_id'])
			r.hset("nutri_hash",nut['_id'],nut)
			r.sadd("nutri_tag",nut['tagname'])
			r.hset("nutri_tag_hash",nut['tagname'],nut)
		
# calling the memory function to calculate the memory utilized.
totalmemoryfunction()