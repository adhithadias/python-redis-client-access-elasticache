from redis.client import Redis

# client_url = 'localhost'
redis_url = 'master.merchportal-redis.e9k47p.use1.cache.amazonaws.com'

redis_port = 6379
# redis_password = '1234'
redis_password = 'rFA94ys3u$6i&snP'

# ssl_enabled = False
ssl_enabled = True

redis_client = Redis(
    host=redis_url, port=6379, db=0, password=redis_password, ssl=ssl_enabled,
    socket_timeout=10, connection_pool=None, charset='utf-8', errors='strict', unix_socket_path=None)

print("Keys in redis at the beginning")
redis_keys = redis_client.keys('merchant-portal:*')
for key in redis_keys:
    print(key)

for key in redis_keys:
	redis_client.delete(key)
	print('Deleted key: %s' % key)

print("Script executed successfully")
