from factor import onefactor;
from factor import description;
from factor import  getdebt;
import baostock as bs
bs.login();
print(description());
for i in onefactor('sz.002138'):
    print(i)
bs.logout();
