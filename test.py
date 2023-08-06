from cnredis import r
from datapreprocessing import digitization
from datapreprocessing import getonelistfromredis
from datapreprocessing import nonum;
from datapreprocessing import isnonum;
print(nonum())
print(isnonum(nonum()))
li=getonelistfromredis('002911');
for i in li:
    print(i);

