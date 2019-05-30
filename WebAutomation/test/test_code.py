# -*- coding: utf-8 -*-
# 开发人员   ：Rocklee
# 开发时间   ：2019/4/18  18:56 
# 文件名称   ：test.PY
# 开发工具   ：PyCharm

import json
import jsonpath
from requests_toolbelt import MultipartEncoder
from util.http_util import get_context

# This file is used to test single request.

def request(data,url):
    data=MultipartEncoder(fields=data)
    c=get_context(url=url,type='post',data=data,otherheader={'Content-Type':data.content_type} )
    return c

url='http://118.25.180.178:5013/checkaccproblemv1'
data = {'accident_record':'{"last_time_to_shop":"2013-02-01","total_mileage":45557,"result":[{"date":"2013-02-01","mile":45557,"type":"维修","detail":"2012年Q4健诊及服务促销活动","other":""},{"date":"2013-01-23","mile":45557,"type":"维修","detail":"更换近光灯泡（L）;更换雨刮片，左前雾灯;检查打方向异响;检查喷水壶不工作","other":"左雨刮片:1;右雨刮片:1;灯泡（大灯/近光）-H7:1;雾灯-前:1"},{"date":"2013-01-23","mile":45557,"type":"维修","detail":"刹车油更换;嘉年华更换前刹车片;拆装方向管柱;拆装喷水壶;更换驱动皮带;清洗喷油嘴;清洗节气门;嘉年华清洗三元催化","other":"油箱洗涤器:1;玻璃水（1.7升）:2;中间铰接轴:1;空气格/09嘉年华/001:1;制动液/通用:1;发动机皮带:1;进气系统清洗剂:1;三元催化清洗剂:2;燃油系统清洗剂325ML/007:1;前刹车片:1"},{"date":"2011-10-28","mile":22367,"type":"维修","detail":"更换全车锁（含电脑编程）","other":"全车锁（新）-嘉年华:1;遥控器-福克斯:1"},{"date":"2011-04-21","mile":13702,"type":"维修","detail":"检查时速120时车抖;四轮动平衡","other":""},{"date":"2011-04-01","mile":6630,"type":"维修","detail":"免费救援","other":""},{"date":"2010-12-27","mile":4539,"type":"维修","detail":"检查地盘螺丝紧固及各球头间隙 胶套 减震器是否漏油;检查外部灯光。;检查轮胎气压及磨损;检查各液面（防冻液 刹车油 自动变速箱油  机油）;检查刹车片（盘式）;清洁空调格 或更换;检查驱动皮带;检查发动机 变速箱 及外部管路是否渗漏;清洁空气格 或更换","other":""},{"date":"2010-12-27","mile":4539,"type":"维修","detail":"免费换油","other":"机油格09嘉年华:1;美孚一号全合成高效机油1L:3"},{"date":"2010-10-29","mile":1,"type":"维修","detail":"更换四轮钢圈","other":""}]}'}

res = request(data,url)
result = json.loads(res)
engine = jsonpath.jsonpath(result,"$.data.[?(@.code == 'engine')]")
print(engine)