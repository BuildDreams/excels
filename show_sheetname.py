
import time
import pandas as pd
import numpy as np
from multiprocessing import Pool

import os
file_path = "D:/test/test.py"
(filepath,tempfilename) = os.path.split(file_path)
(filename,extension) = os.path.splitext(tempfilename)
def show_sheet_name(file):

    xl =  pd.ExcelFile(file)
    all_sheet = xl.sheet_names  # see all sheet names

    return all_sheet


def jion_sheets(file,chose_type,filename,TO,indexs):
    print('_' * 20, indexs)
    datas = pd.DataFrame()
    sheet_names = show_sheet_name(file)
    for sheet_name in sheet_names:
        print('即将处理%s'%sheet_name)
        try:
            df = pd.read_excel(file,sheet_name=sheet_name,header=1)

            df['from'] = filename+sheet_name
        except:
            pass
        if TO == 0:
            datas = pd.concat([datas, df], axis=0, join=chose_type, ignore_index=True,sort=True)
        elif TO == 1:
            datas = pd.merge(datas, df, on=indexs, how=chose_type)
        print('正在处理%s'%file)
    return datas


def main(files,chose_type,TO,indexs):
    print('Parent process %s.' % os.getpid())
    t1 = time.clock()

    all_data  = pd.DataFrame()
    # files = [r'C:\Users\Administrator\Desktop\cy\excs\1.xlsx',
    #          r'C:\Users\Administrator\Desktop\cy\excs\2.xlsx',
    #          r'C:\Users\Administrator\Desktop\cy\excs\3.xlsx',
    #          r'C:\Users\Administrator\Desktop\cy\excs\4.xlsx',
    #          r'C:\Users\Administrator\Desktop\cy\excs\5.xlsx',
    #          r'C:\Users\Administrator\Desktop\cy\excs\6.xlsx',
    #          r'C:\Users\Administrator\Desktop\cy\excs\7.xlsx',
    #          r'C:\Users\Administrator\Desktop\cy\excs\8.xlsx',
    #          r'C:\Users\Administrator\Desktop\cy\excs\9.xlsx',
    #          r'C:\Users\Administrator\Desktop\cy\excs\10.xlsx',
    #          r'C:\Users\Administrator\Desktop\cy\excs\11.xlsx',
    #          r'C:\Users\Administrator\Desktop\cy\excs\12.xlsx',
    #          r'C:\Users\Administrator\Desktop\cy\excs\13.xlsx',
    #          ]
    p = Pool(4)

    for file in files:
        (filepath, tempfilename) = os.path.split(file)
        (filename, extension) = os.path.splitext(tempfilename)
        print(filename)
        if TO == 0:
            res = p.apply_async(jion_sheets, args=(file,chose_type,filename,TO,indexs))
            all_data = pd.concat([all_data, res.get()], axis=0, join=chose_type, ignore_index=True,sort=True)
        elif TO == 1:
            #jion_sheets(file, chose_type, filename, TO, indexs):
            res = p.apply_async(jion_sheets, args=(file, chose_type, filename,TO,indexs))
            pd.concat(all_data, res.get(), )

    p.close()
    p.join()

    t2 = time.clock()
    ts = t2-t1
    try:
        all_data.set_index('from',inplace=True)
    except:
        pass
    all_data.to_excel('./res.xlsx')

    print("用时{}s".format(ts))
    print('All subprocesses done.')

def jion_left_right(left_files,right_files,indexs,chose_type):
    df_left = pd.read_excel(left_files)
    df_right = pd.read_excel(right_files)
    result = pd.merge(df_left, df_right, on=indexs, how=chose_type)

def cols_name(file):
    df = pd.read_excel(file,header=0)
    cols = df.columns.tolist()
    return cols



if  __name__ =="__main__":
    files = [r'C:\Users\Administrator\Desktop\cy\excs\9.xlsx',r'C:\Users\Administrator\Desktop\cy\excs\10.xlsx']
    main(files)
