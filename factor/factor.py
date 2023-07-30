import baostock as bs
import pandas as pd
import datetime
def month2quarter(m):
    q=m//3;
    r=m%3;
    if r==0:
        return q
    else:
        return q+1


def getdebt(s_code,year, quarter):
    rs_balance = bs.query_balance_data(code=s_code, year=year, quarter=quarter)
    if rs_balance.error_code == '0':
        debtlist = rs_balance.get_row_data();
        if len(debtlist)>0:
            return debtlist;
        else:
            return ["","","","","","","","",""];
    else:
        return ["","","","","","","","",""];
def getTTM(s_code,date):
    rs = bs.query_history_k_data_plus(s_code,
    "peTTM,pbMRQ,psTTM,pcfNcfTTM",
    start_date=date, end_date=date,
    frequency="d", adjustflag="3")
    result_list = []
    if rs.error_code == '0':
        ttmlist = rs.get_row_data();
        if len(ttmlist)>0:
            return ttmlist;
        else:
            return ["","","",""];
    else:
        return ["","","",""];


def onefactor(s_code):
#### 调用前需执行bs.login ####
    # 计算三年前的日期
    today=datetime.date.today();
    lastquarter = today - datetime.timedelta(days=3*30);
    three_years_ago = today - datetime.timedelta(days=3*365)

    rs = bs.query_history_k_data_plus(s_code,
    "date,code,close,volume,amount",
    start_date=three_years_ago.strftime('%Y-%m-%d'), end_date=lastquarter.strftime('%Y-%m-%d'), 
    frequency="m", adjustflag="3")
    if rs.error_code!='0':
        print('query_history_k_data_plus respond  error_msg:'+rs.error_msg)
        return [];
    #### 打印结果集 ####
    result_list = []
    qcache = {};

    while (rs.error_code == '0') & rs.next():
        line = rs.get_row_data()
        dtime = datetime.datetime.strptime(line[0], '%Y-%m-%d')
        qstr = s_code+str(dtime.year)+str(month2quarter(dtime.month));
        if qstr not in qcache:
            lineq = getdebt(s_code,dtime.year,month2quarter(dtime.month));
            qcache[qstr]=lineq
        else:
            lineq = qcache[qstr]
        for lineqitem in range(len(lineq)-3):
            line.append(lineq[lineqitem+3]);

        linettm = getTTM(s_code,line[0]);
        for linettmitem in linettm:
            line.append(linettmitem);

        # 获取一条记录，将记录合并在一起
        line[3]=int(int(line[3])/1000);
        line[4]=int(float(line[4])/10000);
        result_list.append(line)
    return result_list;

def description():
    return '日期，股票代码，收盘价，成交量（千股），成交额（万元）,流动比率,速动比率，现金比率，总负债同比增长率，资产负债率，权益乘数,滚动市盈率,市净率，滚动市销率，滚动市现率';
