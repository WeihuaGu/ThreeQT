from openpyxl import load_workbook
from fpath.path import path
import os
import warnings
warnings.filterwarnings('ignore');
# 1.打开 Excel 表格并获取表格名称
data_path = path('中小企业300指数.xlsx',__file__);
indexsheet = load_workbook(filename=data_path)["指数样本股"];
listA = indexsheet["A"];
SZ = set();
for i in listA:
    if i.value!='证券代码':
        SZ.add(i.value);
