import redis, time, datetime, sys

endpoint='redis-virginia.fcycnd.ng.0001.use1.cache.amazonaws.com'
#endpoint='myred-001.dpchko.0001.usw2.cache.amazonaws.com'

def prepareConn(endpoint):
	r = redis.StrictRedis(host=endpoint, port=6379, db=0, socket_timeout=1)
	return r

r = prepareConn(endpoint)

while True:
	print(datetime.datetime.now())
	try:
		print(r.keys())
	except:
		print ("Unexpected error:", sys.exc_info()[0])
	time.sleep(1)



# import redis
# # create a connection to the localhost Redis server instance, by
# # default it runs on port 6379
# redis_db = redis.StrictRedis(host="redis-virginia.fcycnd.ng.0001.use1.cache.amazonaws.com", port=6379, db=0)
# # see what keys are in Redis
# redis_db.keys()
# # output for keys() should be an empty list "[]"
# redis_db.set('full stack', 'python')
# # output should be "True"
# redis_db.keys()
# # now we have one key so the output will be "[b'full stack']"
# redis_db.get('full stack')
# # output is "b'python'", the key and value still exist in Redis
# redis_db.incr('twilio')
# # output is "1", we just incremented even though the key did not
# # previously exist
# redis_db.get('twilio')
# # output is "b'1'" again, since we just obtained the value from
# # the existing key
# redis_db.delete('twilio')
# # output is "1" because the command was successful
# redis_db.get('twilio')
# # nothing is returned because the key and value no longer exist
