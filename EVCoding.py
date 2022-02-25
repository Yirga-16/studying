import math
import numpy as np
import pandas as pd
import openpyxl
from pathlib import Path
import random
from random import seed
from random import randint

# EV_Charging_Time = (SOC_e - SOC_s)*E/(Ch_eff*P_ch)
# SOC_e = expected
# SOC_s = start
# E = Battery capacity
# Ch_eff = charging efficiency
# P_ch = Charging Power

# Wind Turbines
# v = 8
v_in = 5
v_out = 30
v_r = 15
Pr = 500


def Wind_power():
    for v in np.random.randint(2, 35, size=8761):
        # i = len(v)
        if v <= v_in or v >= v_out:
            P_WT = 0
            print(P_WT)
        elif v_in < v or v <= v_r:
            P_WT = Pr * (v ** 3 - v_in ** 3) / (v_r ** 3 - v_in ** 3)
            print(P_WT)
        elif v_r < v or v <= v_out:
            P_WT = Pr
            print(P_WT)
        else:
            print(0)
    return


# P_WTurbine = Wind_power()
Wind_power()
# print(P_WTurbine)
# # def Solar_PV():
# with open("Glob.xlsx","r") as name:
#     my_name = name.read()
#     print(my_name)
# # "r", read file, "w", write file
# # File1.write("thjskfefr")


# csv_path = 'file1.csv'
# df = banana.read_csv(csv_path) #df is data frame
# df.head()
xlsx_path = 'Glob.xlsx'
df = pd.read_excel(xlsx_path)#, encoding='utf-8')  # df is data frame
print(df.head())


xlsx_file = Path('D:\Python Coding', 'Glob.xlsx')
print(xlsx_file)
wb_obj = openpyxl.load_workbook(xlsx_file)
print(wb_obj)

#sheet = wb_obj.sheet1
# print(sheet)