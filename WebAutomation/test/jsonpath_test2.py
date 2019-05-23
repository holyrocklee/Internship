# -*- coding: utf-8 -*-
# 开发人员   ：Rocklee
# 开发时间   ：2019/5/6  15:17 
# 文件名称   ：jsonpath_test2.PY
# 开发工具   ：PyCharm

import jsonpath

d = { "store": {
    "book": [
      { "category": "纪录片",
        "author": "赵",
        "title": "A",
        "price": 8.95
      },
      { "category": "喜剧片",
        "author": "钱",
        "title": "B",
        "price": 12.99
      },
      { "category": "喜剧片",
        "author": "孙",
        "title": "C",
        "isbn": "0-553-21311-3",
        "price": 8.99
      },
      { "category": "喜剧片",
        "author": "李",
        "title": "D",
        "isbn": "0-395-19395-8",
        "price": 22.99
      }
    ],
    "bicycle": {
      "color": "red",
      "price": 19.95
    }
  }
}

tmp1 = jsonpath.jsonpath(d,'$.store.book[*].author') # *通配符，表示所有的元素; 在此表示所有书的作者
print("tmp1:%s"%tmp1)
tmp1_1 = jsonpath.jsonpath(d,'$.store') #表示store内所有的元素
print("tmp1_1:%s"%tmp1_1)

tmp2 = jsonpath.jsonpath(d,'$..author')#所有书的作者， ..表示模糊匹配
print("tmp2:%s"%tmp2)

tmp3 = jsonpath.jsonpath(d,'$.store.*') #表示store下book和bicycle的所有元素
print("tmp3:%s"%tmp3)

tmp4 = jsonpath.jsonpath(d,'$.store..price') #所有物品的价格
print("tmp4:%s"%tmp4)

tmp5 = jsonpath.jsonpath(d,'$..book[2]') #第三本书的所有信息
print("tmp5:%s"%tmp5)

tmp6 = jsonpath.jsonpath(d,'$..book[(@.length-1)].title')[0] #最后一本书
print("tmp6:%s"%tmp6)
tmp6_1 = jsonpath.jsonpath(d,'$..book[(@.length)]') #没有则输出False
print("tmp6_1:%s"%tmp6_1)
tmp6_2 = jsonpath.jsonpath(d,'$..book[-1:]') #最后一本书
print("tmp6_2:%s"%tmp6_2)

tmp7 = jsonpath.jsonpath(d,'$..book[0,1]') #前两本书  多选操作
print("tmp7:%s"%tmp7)

tmp8 = jsonpath.jsonpath(d,'$..book[:2]') #前两本书  切片操作
print("tmp8:%s"%tmp8)

tmp9 = jsonpath.jsonpath(d,'$..book[?(@.isbn)].title') #筛选操作 筛选book中包含isbn的book
print("tmp9:%s"%tmp9)

tmp10 = jsonpath.jsonpath(d,'$..book[?(@.price!=10)].[title,author]') # @表示当前对象book，逻辑表达式用来筛选
print("tmp10:%s"%tmp10)

tmp11 = jsonpath.jsonpath(d,'$..*')
print("tmp11:%s"%tmp11)