from datapreprocessing import getonelistfromredis
from cnredis import r

def pull():
    indexlist = r.smembers('index');
    for index in indexlist:
        oneindexlist = getonelistfromredis(index);
        for one in oneindexlist:
            print(one);


pull();
