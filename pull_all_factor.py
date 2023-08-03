from cnredis import r;

def pull():
    indexlist = r.smembers('index');
    for index in indexlist:
        key = 'factor_'+index
        oneindexlist = r.lrange(key,0,-1);
        for one in oneindexlist:
            print(one);


pull();
