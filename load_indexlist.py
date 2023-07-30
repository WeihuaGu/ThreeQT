from indexlist import getIndexList;
from cnredis import r;
import datetime;
from timeupdate import isTimeUpdate;

def writetoredis():
    print('load index list to redis');
    indexlist = getIndexList.SZ;
    for i in indexlist:
        r.sadd('index',i);
    r.set('indexlist_updatetime',datetime.date.today().strftime('%Y-%m-%d'));

def load_indexlist():
    if r.scard('index')==0:
        writetoredis();
    if isTimeUpdate(30,r.get('indexlist_updatetime')):
        writetoredis();
    return r.smembers('index');

