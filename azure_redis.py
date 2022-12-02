import redis
import time

print("-----------------------The elapsed time of Azure Redis--------------------------")
myHostname = "wptest01.redis.cache.windows.net"
myPassword = ""

r1 = redis.StrictRedis(host=myHostname, port=6380,
                              password=myPassword, ssl=True)

# Ping Returen
st = time.time()
result = r1.ping()
et = time.time()
elapsed_time = et - st
print("Ping Return : {}; The Elapsed time: {}".format(result, elapsed_time))

# Set Message 
st = time.time()
result = r1.set("Message", "Hello!, The cache is working with Python!")
et = time.time()
elapsed_time = et - st
print("Set Message Return : {}; The Elapsed time: {}".format(str(result), elapsed_time))

# Get Message
st = time.time()
result = r1.get("Message")
et = time.time()
elapsed_time = et - st
print("Get Message Return : {}; The Elapsed time: {}".format(result.decode("utf-8"), elapsed_time))

result = r1.client_list()
print("CLIENT List Return: ")
for c in result:
    print("id : " + c['id'] + ", addr : " + c['addr'])

print("-----------------------The elapsed time of Self managed Redis --------------------------")
myHostname2 = "10.0.0.6"
myPassword2 = "foobared"

r2 = redis.StrictRedis(host=myHostname2, port=6379,
                              password=myPassword2)

# Ping Returen
st = time.time()
result = r2.ping()
et = time.time()
elapsed_time = et - st
print("Ping Return : {}; The Elapsed time: {}".format(result, elapsed_time))

# Set Message 
st = time.time()
result = r2.set("Message", "Hello!, The cache is working with Python!")
et = time.time()
elapsed_time = et - st
print("Set Message Return : {}; The Elapsed time: {}".format(str(result), elapsed_time))

# Get Message
st = time.time()
result = r2.get("Message")
et = time.time()
elapsed_time = et - st
print("Get Message Return : {}; The Elapsed time: {}".format(result.decode("utf-8"), elapsed_time))

result = r2.client_list()
print("CLIENT List Return: ")
for c in result:
    print("id : " + c['id'] + ", addr : " + c['addr'])
