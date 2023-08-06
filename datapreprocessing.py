import json;
from cnredis import r
import math;
def getonelistfromredis(s_code):
    key = 'factor_'+s_code
    oneindexlist = r.lrange(key,0,-1);
    onelist=[];
    for one in oneindexlist:
            one=str2list(one);
            if len(one)==15:
                toindex=list(range(2,len(one)));
                one=digitization(one,toindex)
                onelist.append(one);
    return onelist;


def str2list(strlist):
    return json.loads(strlist);
def nonum():
    return round(-1*math.pi,6);
def isnonum(num):
    if num==nonum():
        return True;
    else:
        return False;


def digitization(li,toindex):
    for index in toindex:
        if li[index]=='':
            li[index]=nonum();
        else:
            li[index]=float(li[index])
    return li;

