import datetime;
def isTimeUpdate(delayday,updatetimestr):
    if updatetimestr==None:
        return False;
    updatetime = datetime.datetime.strptime(updatetimestr, '%Y-%m-%d');
    today = datetime.date.today();
    if (today-updatetime).days > delayday:
        return True;
    else:
        return False;

