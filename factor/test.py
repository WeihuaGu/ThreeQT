from factor import onefactor;
from factor import description;
from factor import  getdebt;
from factor import  getTTM;
import baostock as bs
bs.login();
hah="2023-06-30", "sz.002078"
print(description());
print(getTTM('sz.002078','2023-04-28'));

bs.logout();
