# -*- coding: utf-8 -*-
# 开发人员   ：Rocklee
# 开发时间   ：2019/5/7  11:00 
# 文件名称   ：base.PY
# 开发工具   ：PyCharm
import json
import os
import base64

def base(path):
    a=[]
    for filename in os.listdir(path):
        b=[]
        ss = filename.split(".")
        b.append(ss[0])
        newDir = os.path.join(path, filename)
        with open(newDir, 'rb') as f:
                data = f.read()
                s = base64.b64encode(data)
                b.append(str(s,'utf8'))
        #print(len(b))
        a.append(b)
        #print(len(a))
    return a

list=base("C:\\Users\\che300\\PycharmProjects\\WebAutomation\\util\\OcrVerify\\Carpcitures\\认证行驶证照片")

from util.excel_util import excelutil
from util.http_util import get_context
import jsonpath
from requests_toolbelt.multipart.encoder import MultipartEncoder

def request(data,url):
    data=MultipartEncoder(fields=data)
    c=get_context(url=url,type='post',data=data,otherheader={'Content-Type':data.content_type} )
    return c


url = "http://118.25.180.178:5080/isCarImage"
#print(list)
util = excelutil('C:\\Users\\che300\\PycharmProjects\\WebAutomation\\util\\OcrVerify\\OcrResult\\OcrResult.xls', 'w', head=[ '图片名字','可能性','是否局部车图片'])
for name,picbase in list:
    print(picbase)
    print(name)
    data = {}
    data['car_image'] = picbase
    ocrtext = request(data,url)
    #print(ocrtext)
    #这里注意，虽然打印出来的ocrtext看着像字典格式，其实是个字符串，要先用json.loads函数将str类型转换为json类型
    ocrtext = json.loads(ocrtext)
    print(ocrtext)
    #print(engine)
    #possibility = jsonpath.jsonpath(ocrtext,'$.data.*.possibility')
    possibility = ocrtext["possibility"]
    result = ocrtext["result"]
    print(result)
    # if result == 0:
    #     result = "是"
    # else:
    #     result = "否"
    #print(possibility)
    #print(result)
    util.write_nextline([name, possibility,result], save=True)

