import pandas as pd
import numpy as np
from multiprocessing import Pool
import os

def Show_sheet_name(file):
    """
    获取文件的所有sheet
    :param file:单个excel文件
    :return:文件内所有sheet名字
    """
    print('show_sheet_name函数')
    xl =  pd.ExcelFile(file)
    all_sheet = xl.sheet_names  # see all sheet names
    return all_sheet

def Cols_name(file):
    """
    返回单个文件的字段名
    :param file: 单个文件
    :return: 字段名
    """
    try:
        df = pd.read_excel(file,header=0,nrows=5)
        cols = df.columns.tolist()
        if cols != []:
            return cols
    except:
        pass



def Outer_files(file,chose_type,axis,indexs):

    """
    全集模式连接
    :param file: 单个文件
    :param chose_type: 合并方式 inner\outer
    :param axis: 合并方向 横向\竖向
    :param indexs: 此参数为横向独有参数，因为横向连接需要指定连接轴
    :return: 每个excel文件内部sheet的合并
    """
    print('outerfile函数')
    all_data = pd.DataFrame()
    sheet_names= Show_sheet_name(file)
    if axis == 0:
        for sheet_name in sheet_names:
            df = pd.read_excel(file,sheet_name=sheet_name,header=0)
            all_data = pd.concat([all_data, df], sort=True, join=chose_type, axis=axis)
        return all_data
    elif axis ==1:
        try:
            for sheet_name in sheet_names:
                df = pd.read_excel(file,sheet_name=sheet_name,header=0,index_col=indexs)
                all_data = pd.concat([all_data, df], sort=True, join=chose_type, axis=axis)
        except:
            return 'Y'
        return all_data

def Start(files,chose_type,axis,indexs):
    """
    多线程读取合并文件
    :param files:用户选择的所有文件
    :param chose_type:合并方式 OUTER /INNER
    :param axis:合并方向 横向/竖向
    :return:将输出最终目标文件
    """
    print('Start函数')
    # p = Pool(2)
    all_data = pd.DataFrame()
    if axis == 0:
        for file in files:
            res = Outer_files(file, chose_type, axis, indexs)
            # res = p.apply_async(Outer_files, args=(file,chose_type,axis,indexs))
            all_data = pd.concat([all_data, res], axis=axis, join=chose_type, sort=True)

    elif axis == 1:
        for file in files:
            res = Outer_files(file,chose_type,axis,indexs)

            # res = p.apply_async(Outer_files, args=(file,chose_type,axis,indexs))
            all_data = pd.concat([all_data, res], axis=axis, join=chose_type, sort=True)

    # p.close()
    # p.join()
    all_data.to_excel('./%s.xlsx'%chose_type)


    return