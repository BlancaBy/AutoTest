#coding=utf-8

import socket
import time, unittest, os, requests
from Tools import HTMLTestRunner
requests.packages.urllib3.disable_warnings()

# 创建testsuits配置文件
project_dir = os.path.dirname(os.path.abspath(__file__))

# 设置Carday所有账户的密码
# pf.setPasswordForAll()

cur_dir = os.path.abspath(os.curdir)

list=[]
cfile=open(cur_dir+'/caselists.txt')

for data in cfile:
    sdata = str(data).strip()
    if sdata != '' and not sdata.startswith("#"):
        list.append(sdata)
sdir=cur_dir+'/TestSuits'+list[0]
testunit = unittest.defaultTestLoader.discover(sdir, pattern='AT_*.py')
print testunit
#定义log日志文件的目录和名称
now = time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime(time.time()))

#定义HTML报告的目录和名称
fileName = os.path.dirname(os.path.abspath(__file__)) + "/Result/result.html"
fp = file(fileName, 'wb')

#设置HTML报告的title和description信息
runner = HTMLTestRunner.HTMLTestRunner(
    stream = fp,
    title = u'Oscar-mds_接口自动化测试报告',
    description = u'用例执行情况：')

#启动测试套件
runner.run(testunit)
fp.close()

# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.connect(('8.8.8.8', 80))
# ip_addr = s.getsockname()[0]
# # 使用花生壳的域名地址
# # ip_addr = 'g220387g67.imwork.net'
# reportName = "http://" + ip_addr + ":8080/job/Oscar-mds_API_AutoTest/ws/Result/Result.html"
# #输出测试报告链接到控制台，然后jenkins会自动将该地址随邮件发送给接收者
# print reportName