# -*- coding: utf-8 -*-
# 开发人员   ：Rocklee
# 开发时间   ：2019/5/31  18:45 
# 文件名称   ：excel_data.PY
# 开发工具   ：PyCharm

import requests as rq
import pandas as pd
import jsonpath
import json
import re

df = pd.read_excel('D:\\cxli\\api\\excel_table\\发动机.xlsx')
data=df.ix[:,['simple_detail','num']].values  #读所有行的simple_detail以及num列的值，这里需要嵌套列表
#print(data)
# detail = data[0][0]
# print(detail)
# number = data[0][1]
PATTERN = r'([\u4e00-\u9fa5]{2,5}?(?:省|自治区|市))([\u4e00-\u9fa5]{2,7}?(?:市|区|县|州)){0,1}([\u4e00-\u9fa5]{2,7}?(?:市|区|县)){0,1}'
data_list = ['发动机', '引擎','换']

for singledata in data:
    print(singledata)
    singledetail = singledata[0]
    print(singledetail)
    singlenum = singledata[1]
    print(singlenum)
    Regex = re.compile(r'')