#coding=utf-8
from Framework.PfTest import create_test_suite
from Tools import HTMLTestRunner
import time,socket,os, requests
from Framework.PfTest import *
requests.packages.urllib3.disable_warnings()

# 创建testsuits配置文件
project_dir = os.path.dirname(os.path.abspath(__file__))

# 设置Carday所有账户的密码
# pf.setPasswordForAll()

#调用createTestSuite()方法
testunit = create_test_suite()

#定义log日志文件的目录和名称
now = time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime(time.time()))

#定义HTML报告的目录和名称
fileName = "./Result/Result.html"
fp = file(fileName, 'wb')

#设置HTML报告的title和description信息
runner = HTMLTestRunner.HTMLTestRunner(
    stream = fp,
    title = u'CarChat_接口自动化测试报告',
    description = u'用例执行情况：')

#启动测试套件
runner.run(testunit)
fp.close()

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8', 80))
ip_addr = s.getsockname()[0]
# 使用花生壳的域名地址
# ip_addr = 'g220387g67.imwork.net'
reportName = "http://" + ip_addr + ":8080/job/CarChat_API_AutoTest/ws/Result/Result.html"
#输出测试报告链接到控制台，然后jenkins会自动将该地址随邮件发送给接收者
print reportName