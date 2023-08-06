from cnredis import r
from datapreprocessing import digitization
from datapreprocessing import getonelistfromredis
import json
li=getonelistfromredis('002911');
for i in li:
    toindex=list(range(2,len(i)));
    digitization(i,toindex);
    print(i);

