from redis import Redis

redis_cli=Redis(host='localhost',port=6379,db=0)

redis_cli.set('mingzi','itheima')

name = redis_cli.get("mingzi")

print(name)

redis_cli.delete('mingzi')