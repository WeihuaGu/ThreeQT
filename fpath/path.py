import os
def path(filename,whocall):
    basepath = os.path.abspath(whocall)
    folder = os.path.dirname(basepath)
    data_path = os.path.join(folder,filename)
    return data_path;
