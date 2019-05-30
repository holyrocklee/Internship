# # -*- coding: utf-8 -*-
# # 开发人员   ：Rocklee
# # 开发时间   ：2019/5/28  10:14
# # 文件名称   ：weibao.PY
# # 开发工具   ：PyCharm
#
#
# import os
# import re
# import json
#
# def eachFile(filepath):
#     pathDir =os.listdir(filepath)        #遍历文件夹中的text
#     return pathDir
#
# def readfile(name):
#     fopen=open(name,'r')
#     list = []
#     for lines in fopen.readlines():         #按行读取text中的内容
#         matchresult = re.findall(r'[(](.*?)[)]', lines)
#         if '发动机' in str(matchresult) or '变速箱' in str(matchresult):
#             list.append(matchresult)
#             print(list)
#         else:
#             pass
#     #print(len(list))
#     fopen.close()
#     return list
#
# # def writefile(filename):
# #     with open(filename, "wb") as f:
# #         for i in range(len(lists)):
# #             f.write(lists[i],encoding="utf-8")
#
#
# if __name__ == '__main__':
#     filePath = "D:\\cxli\\api\\维保"
#     pathDir=eachFile(filePath)
#     for allDir in pathDir:
#         #child = '\\'.join([filePath, allDir])
#         child = "D:\\cxli\\api\\维保" + '\\' + allDir
#         lists = readfile(child)
#         # for i in range(len(lists)):
#         #     print(lists[i])
#         #writefile("D:\\cxli\\api\\1.txt")
#         f = open("D:\\cxli\\api\\1.txt",'a')
#         f.writelines(str(lists[i]) for i in range(len(lists)))
#         f.close()
#


import requests as rq
import pandas as pd
import jsonpath
import json
url = 'http://118.25.180.178:5013/checkaccproblemv1'


with open('D:\\cxli\\api\\维保\\result_20181216.txt', 'r',encoding='utf-8') as f:
    data = list(map(lambda x: x.strip(), f))


result = list(map(lambda x: rq.post(url, {'accident_record': str(x)}).json(), data))
print(result)
for i in range(len(result)):
    result = str(result[i])
    print(result)
    result = json.loads(result)
    engine = jsonpath.jsonpath(result,"$.data.[?(@.code == 'engine')]")
    #print(engine)

pd.DataFrame({'data': data, 'result': result}).to_csv('D:\\cxli\\api\\result.csv', index=False)
