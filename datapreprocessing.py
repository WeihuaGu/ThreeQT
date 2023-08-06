import json;
from cnredis import r
def getonelistfromredis(s_code):
    key = 'factor_'+s_code
    oneindexlist = r.lrange(key,0,-1);
    onelist=[];
    for one in oneindexlist:
            one=str2list(one);
            if len(one)==15:
                onelist.append(one);
    return onelist;


def str2list(strlist):
    return json.loads(strlist);


def digitization(li,toindex):
    for index in toindex:
        if li[index]=='':
            li[index]=-1;
        else:
            li[index]=float(li[index])
    return li;

