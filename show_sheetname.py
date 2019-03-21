import pandas as pd
import numpy as np

def show_sheet_name(file):

    xl = pd.ExcelFile(file)
    all_sheet = xl.sheet_names  # see all sheet names

    return all_sheet


def jion_sheets(file,sheet_names,datas):

    for sheet_name in sheet_names:
        df = pd.read_excel(file,sheet_name=sheet_name,header=0)

        datas = pd.concat([datas, df], axis=0, join='outer', ignore_index=True)
    return datas
