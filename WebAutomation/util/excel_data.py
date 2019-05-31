# -*- coding: utf-8 -*-
# 开发人员   ：Rocklee
# 开发时间   ：2019/5/31  18:45 
# 文件名称   ：excel_data.PY
# 开发工具   ：PyCharm

import requests as rq
import pandas as pd
import jsonpath
import json

df = pd.read_excel('D:\\cxli\\api\\excel_table\\发动机.xlsx')
data=df.ix[:,['simple_detail','num']].values  #读所有行的simple_detail以及num列的值，这里需要嵌套列表
#print(data)
detail = data[0][0]
print(detail)
print(data[0][1])


