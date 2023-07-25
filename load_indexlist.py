import redis   # 导入redis 模块
from indexlist import getIndexList;
r = redis.Redis(host='localhost', port=6379, decode_responses=True)  
if r.scard('index')==0:
    print('load index list to redis');
    indexlist = getIndexList.SZ;
    for i in indexlist:
        r.sadd('index',i);

print(r.smembers('index'));

