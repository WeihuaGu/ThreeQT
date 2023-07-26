import baostock as bs
import pandas as pd
import datetime


def onefactor(s_code):
#### 调用前需执行bs.login ####
#### 获取沪深A股估值指标(日频)数据 ####
# peTTM    滚动市盈率
# psTTM    滚动市销率
# pcfNcfTTM    滚动市现率
# pbMRQ    市净率
    today=datetime.date.today();
    # 计算三年前的日期
    three_years_ago = today - datetime.timedelta(days=3*365)
    rs = bs.query_history_k_data_plus(s_code,
    "date,code,close,amount",
    start_date=three_years_ago.strftime('%Y-%m-%d'), end_date=today.strftime('%Y-%m-%d'), 
    frequency="m", adjustflag="3")
    if rs.error_code!='0':
        print('query_history_k_data_plus respond  error_msg:'+rs.error_msg)
        return [];
    #### 打印结果集 ####
    result_list = []
    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        result_list.append(rs.get_row_data())
    return result_list;
