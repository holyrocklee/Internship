# -*- coding: utf-8 -*-
# 开发人员   ：Rocklee
# 开发时间   ：2019/5/28  10:14
# 文件名称   ：weibao.PY
# 开发工具   ：PyCharm

import requests as rq
import pandas as pd
import jsonpath
import json

url = 'http://118.25.180.178:5013/checkaccproblemv1'

with open('D:\\cxli\\api\\维保\\result_20181216.txt', 'r',encoding='utf-8') as f:
    data = list(map(lambda x: x.strip(), f))

results = list(map(lambda x: rq.post(url, {'accident_record': str(x)}).json(), data))
print(results)

i = 0
engine_result = []
for result in results:
    i = i+1
    print(i)
    print(result)
    result_rep = str(result).replace("'",'"')
    result_rep = json.loads(result_rep)
    print(result_rep)
    engine = jsonpath.jsonpath(result_rep,"$.data.[?(@.code == 'engine')]")
    if engine == False:
        engine_result.append("没有匹配结果")
    else:
        engine_result.append(engine[0])
    print(engine_result)

pd.DataFrame({'data': data, 'result': engine_result}).to_csv('D:\\cxli\\result.csv', index=False)
