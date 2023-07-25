import baostock as bs
import pandas as pd


def onefactor(s_code):
    bs.login()
#### 获取沪深A股估值指标(日频)数据 ####
# peTTM    滚动市盈率
# psTTM    滚动市销率
# pcfNcfTTM    滚动市现率
# pbMRQ    市净率
    rs = bs.query_history_k_data_plus(s_code,
    "date,code,close,amount",
    start_date='2022-01-01', end_date='2022-12-31', 
    frequency="m", adjustflag="3")
    if rs.error_code!='0':
        print('query_history_k_data_plus respond  error_msg:'+rs.error_msg)
        return [];
    #### 打印结果集 ####
    result_list = []
    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        result_list.append(rs.get_row_data())
    bs.logout()
    return result_list;
