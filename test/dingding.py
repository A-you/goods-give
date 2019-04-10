# -*- coding: utf-8 -*-
# @Time : 2019/4/10 10:25 
# @Author : Ymy
import datetime
import json
import urllib.request
# import pymysql as pms
def get_Copywriting():
	return "今天是周三"
# 	 # 判断当天是周几选择出文案的函数
# 	 #获取当天日期
# 	 today = datetime.date.today()
# 	 #获取当天是周几
# 	 todayweek = datetime.date.isoweekday(today)
# 	 #利用IF语句判断周几选出当天要发送的文案
# 	Copywriting = "今天是%s" % (today)
#
# 	return Copywriting

def send_request(url, datas):
	 #传入url和内容发送请求
	 # 构建一下请求头部
	 header = {
	 "Content-Type": "application/json",
	 "Charset": "UTF-8"
	 }
	 sendData = json.dumps(datas) # 将字典类型数据转化为json格式
	 sendDatas = sendData.encode("utf-8") # python3的Request要求data为byte类型
	 # 发送请求
	 request = urllib.request.Request(url=url, data=sendDatas, headers=header)
	 # 将请求发回的数据构建成为文件格式
	 opener = urllib.request.urlopen(request)
	 # 7、打印返回的结果
	 print(opener.read())
# def get_datas(sql):
#  # 一个传入sql导出数据的函数
#  # 跟数据库建立连接
#  conn = pms.connect(host='实例地址', user='用户名',
#  passwd='密码', database='库名', port=3306, charset="utf8")
#  # 使用 cursor() 方法创建一个游标对象 cursor
#  cur = conn.cursor()
#  # 使用 execute() 方法执行 SQL
#  cur.execute(sql)
#  # 获取所需要的数据
#  datas = cur.fetchall()
#  # 关闭连接
#  cur.close()
#  # 返回所需的数据
#  return datas
def main():
 #按照钉钉给的数据格式设计请求内容 链接https://open-doc.dingtalk.com/docs/doc.htm?spm=a219a.7629140.0.0.p7hJKp&treeId=257&articleId=105735&docType=1
 my_data = {
 "msgtype": "markdown",
 "markdown": {"title": "每日早报",
 "text": " "
 },
 "at": {
 "isAtAll": True
 }
 }
 #获取当天文案
 my_Copywriting = get_Copywriting()
 #获取昨日成交
 # my_mydata = get_datas(
 # "SELECT sum(usdAmount) FROM dplus_source_productorder_v2 WHERE RealPaidTime >= '2018-08-20 00:00:00' AND RealPaidTime <= '2018-08-20 23:59:59'")
 #获取昨日成交的数值
 # my_mydata = my_mydata[0][0]
 # 保留2位小数
 # my_mydata = "%.2f" % my_mydata
 #把文案中的金额替换为昨天成交金额
 # my_Copywriting = my_Copywriting % my_mydata
 #把文案内容写入请求格式中
 my_data["markdown"]["text"] = my_Copywriting
 #你的钉钉机器人url
 my_url = "https://oapi.dingtalk.com/robot/send?access_token=5292340ef7ec22c21140d9d93292369a7c9229c6739b6a1e52865c8fb5e98629"
 send_request(my_url, my_data)
if __name__ == "__main__":
 main();