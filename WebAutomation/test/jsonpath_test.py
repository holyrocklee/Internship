# -*- coding: utf-8 -*-
# 开发人员   ：Rocklee
# 开发时间   ：2019/5/6  11:20 
# 文件名称   ：jsonpath.PY
# 开发工具   ：PyCharm

import jsonpath

d={
        "error_code": 0,
        "stu_info": [
                {
                        "id": 2059,
                        "name": "小白",
                        "sex": "男",
                        "age": 28,
                        "addr": "河南省济源市北海大道32号",
                        "grade": "天蝎座",
                        "phone": "18378309272",
                        "gold": 10896,
                        "info":{
                            "card":434345432,
                            "bank_name":'中国银行'
                        }

                },
                {
                        "id": 2067,
                        "name": "小黑",
                        "sex": "男",
                        "age": 28,
                        "addr": "河南省济源市北海大道32号",
                        "grade": "天蝎座",
                        "phone": "12345678915",
                        "gold": 100
                }
        ]
}

res1 = d["stu_info"][1]["name"]
res1_1 = jsonpath.jsonpath(d,'$.stu_info[1].name')
print(res1)#小黑
print(res1_1) #['小黑']

res2 = d["stu_info"][0]["info"]["bank_name"]
print(res2) #中国银行

res3 = jsonpath.jsonpath(d,'$..name') #嵌套n层也能取到所有学生姓名信息,$表示最外层的{}，..表示模糊匹配
print(res3)#['小白', '小黑']
print(res3[0]) #小白
print(res3[0:1:2]) #['小白']，列表切片操作,从第一行开始到第二行结束，步长为2

res4 = jsonpath.jsonpath(d,'$..bank_name')
print(res4) #['中国银行']

res5 = jsonpath.jsonpath(d,'$..name123')
print(res5) #False

res6 = jsonpath.jsonpath(d,'$.stu_info[(@.length-1)].name')  #$.stu_info[(@.length-1)].[name]  可以使用显示的名称或者索引
print(res6) #['小黑']

res7 = jsonpath.jsonpath(d,'$..[?(@.id<2067)].name')
print(res7) #['小白']
res10 = jsonpath.jsonpath(d,'$..[?(@.id!=2066)].[id,name]')
print('res10:%s'%res10) #[2059, '小白', 2067, '小黑'] 多属性访问，此处换成id=2067就不行

res8= jsonpath.jsonpath(d,'$.[0]')
print(res8)

res9 = jsonpath.jsonpath(d,'$.stu_info[(@.length-1)].[name]')
print('res9:%s'%res9) #['小黑']

