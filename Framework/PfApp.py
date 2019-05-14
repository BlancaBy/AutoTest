#coding=utf-8

import os, time

# 启动Appium服务器
def start_appium_server():
    filepath = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/Tools/startAppiumServer.bat'
    cmd = 'start ' + filepath
    os.system(cmd)   #启动appium服务
    time.sleep(8)

# 关闭Appium服务器
def stop_appium_server():
    filepath = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/Tools/stopAppiumServer.bat'
    cmd = 'start ' + filepath
    os.system(cmd)