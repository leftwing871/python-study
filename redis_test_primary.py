import redis, time, datetime, sys
# create a connection to the localhost Redis server instance, by
# default it runs on port 6379
redis_db = redis.StrictRedis(host="redis-seoul.sizkxz.ng.0001.apn2.cache.amazonaws.com", port=6379, db=0)
# see what keys are in Redis
redis_db.keys()
# output for keys() should be an empty list "[]"
redis_db.set('full stack' + str(datetime.datetime.now()), 'python')
# output should be "True"
print(datetime.datetime.now())
print(redis_db.keys())

# now we have one key so the output will be "[b'full stack']"
redis_db.get('full stack')
# output is "b'python'", the key and value still exist in Redis
redis_db.incr('twilio')
# output is "1", we just incremented even though the key did not
# previously exist
redis_db.get('twilio')
# output is "b'1'" again, since we just obtained the value from
# the existing key
redis_db.delete('twilio')
# output is "1" because the command was successful
redis_db.get('twilio')
# nothing is returned because the key and value no longer exist
