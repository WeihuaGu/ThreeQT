import concurrent.futures
import json
import time
import random
import baostock as bs
from factor.factor import onefactor;
from factor.factor import description;
from cnredis import r
import datetime;
from timeupdate import isTimeUpdate;

if r.scard('index')==0:
    print('no index list in redis');

def random_sleep(mu=1, sigma=0.4):
    '''正态分布随机睡眠
    :param mu: 平均值
    :param sigma: 标准差，决定波动范围
    '''
    secs = random.normalvariate(mu, sigma)
    if secs <= 0:
        secs = mu  # 太小则重置为平均值
    time.sleep(secs)

# 定义一个函数来处理单个股票代码
def process_item(scode):
    # 进行一次计算
    random_sleep();
    faccode = 'factor_'+scode;
    if r.llen(faccode)==0 or r.get('forcerefresh')=='true':
        onef = onefactor('sz.'+scode);
        print('向redis写入股票代码为'+scode+'的因子信息,redis list key 为'+faccode);
        print(description());
        for one in onef:
            onejson = json.dumps(one);
            r.lpush(faccode,onejson);
            print(onejson);
        print('----------------------------------------');
        print('\n');
        return faccode;
    print('股票代码为'+scode+'的因子信息,redis list key 为'+faccode+' 已经写入过redis中');
    return faccode;

def load_factor(works=4,force='false'):
        #if isTimeUpdate(30,r.get('factor_updatetime')):
        writetoredis(works,force);
    
def writetoredis(works,force):
        # 定义要处理的列表
        my_list = r.smembers('index');
        if force=='true':
            r.set('forcerefresh','true');
        else:
            r.set('forcerefresh','false');
        bs.logout();
        random_sleep();
        bs.login();
        print('载入所有股票因子数据到redis,因为股票数在几百上下，所以启用了多线程，请耐心等待载入完成');
        print('如果载入卡死，可以再次运行脚本');
        time.sleep(5);
        r.set('factor_updatetime',datetime.date.today().strftime('%Y-%m-%d'));
        # 创建一个线程池
        with concurrent.futures.ThreadPoolExecutor(max_workers=works) as executor:
            # 使用map函数提交任务到线程池
            results = executor.map(process_item, my_list)

        # 等待所有任务完成
        executor.shutdown(wait=True)
        bs.logout();
        print('所有指数内股票因子已载入redis完成')
