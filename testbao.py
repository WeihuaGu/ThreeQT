import baostock as bs
import pandas as pd

#### 登陆系统 ####
lg = bs.login()

#### 获取历史K线数据 ####
# 详细指标参数，参见“历史行情指标参数”章节
rs = bs.query_history_k_data_plus("sh.600000",
    "date,code,preclose",
    start_date='2017-06-01', end_date='2017-07-31', 
    frequency="d", adjustflag="3") #frequency="d"取日k线，adjustflag="3"默认不复权

#### 打印结果集 ####
data_list = []
while (rs.error_code == '0') & rs.next():
    # 获取一条记录，将记录合并在一起
    data_list.append(rs.get_row_data())
result = pd.DataFrame(data_list, columns=rs.fields)
#### 结果集输出到csv文件 ####
print(result)

#### 登出系统 ####
bs.logout()
