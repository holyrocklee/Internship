# -*- coding: utf-8 -*-
# 开发人员   ：Rocklee
# 开发时间   ：2019/5/24  12:44 
# 文件名称   ：index.PY
# 开发工具   ：PyCharm
import re
import pymysql

def ways_name():
    target_mode, target_func = url.split(".")
    model_name = re.sub('[(](\d+)[)]', '', target_mode)
    return model_name

def data_id():
    p1 = re.compile(r'[(](\d+)[)]', re.S)  # 最小匹配
    target_mode, target_func = url.split(".")
    model_num = re.findall(p1, target_mode)[0]
    return model_num

def return_result():
    r = ''
    target_mode, target_func = url.split(".")  # 输入url的格式为:方法名(行号).函数名 commons(177009).f2
    model_name = ways_name()
    f = __import__('util.' + model_name, fromlist=True)  # 导入util目录下的某个文件模块
    if hasattr(f, target_func):  # 判断函数是否存在
        function_name = getattr(f, target_func)  # 获取函数名
        r = function_name()  # 执行
        #print("反射结果：%s" % r)
    else:
        print("函数不存在，404")
    return r

def link_database():
    db = pymysql.connect(**config)
    cur = db.cursor()
    model_num =data_id()
    cur.execute("SELECT user_name FROM gamma_rc.inf_admin_user WHERE user_id=%s" % model_num)
    sql_return = cur.fetchall()
    #print(sql_return)
    cur.close()
    db.close()
    return sql_return

def judge_input(url):
    if url.isspace() or re.match("\w+[(](\d+)[)].\w+",url)==None:
        return 0
    else:
        pass
        return 1

if __name__ == '__main__':
    #数据库配置
    config = {
    'host' : '192.168.0.192',
    'port' : 3306,
    'user' : 'root',
    'password' : 'root@1212',
    'database' : 'gamma_rc',
    'charset' : 'utf8',
    }
    url = input("url:")
    if judge_input(url) == 0:
        print("请输入有效字符串,格式为Way(id).Function")
    else:
        print("方法名：%s" % ways_name())
        print("数据库id号：%s" % data_id())
        print(return_result())
        print("数据库返回结果:%s"%link_database())





    #p1 = re.compile(r'[(](.*?)[)]', re.S)  #最小匹配
    #target_mode,target_func = url.split(".") #输入url的格式为:模块名(行号).函数名 commons(177009).f2
    # model_name = re.sub('\\(.*?\\)','',target_mode)
    # model_num = re.findall(p1,target_mode)[0]
    # print("方法名：%s"%model_name)
    # print("数据库id号：%s"%model_num)
    # model_name = ways_name()
    # f = __import__('util.'+model_name,fromlist=True)  #导入util目录下的某个文件模块
    # if hasattr(f,target_func):  #判断函数是否存在
    #     function_name = getattr(f,target_func) #获取函数名
    #     r = function_name()  #执行
    #     print("反射结果：%s"%r)
    # else:
    #     print("404")

    # db = pymysql.connect(host='192.168.0.192',port=3306,user='root',password='root@1212',db='gamma_rc',charset='utf8')
    # cur = db.cursor()
    # cur.execute("SELECT user_name FROM gamma_rc.inf_admin_user WHERE user_id=%s"%model_num )
    # print(cur.fetchall())
    # cur.close()
    # db.close()

