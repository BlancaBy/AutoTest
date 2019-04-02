#coding=utf-8

import os, requests
import Framwork.PfTime as pfTime
from Framwork.PfFile import *
from Framwork.logger import Logger
logger = Logger(logger="TC").getlog()

# region 处理excel文件中的接口信息
def getHost(dictdata):
    return dictdata.get('Host')

def getPath(dictdata):
    return dictdata.get('Path')

def getMethod(dictdata):
    return dictdata.get('Method')

def getParams(dictdata, rowData=False):
    if rowData:
        return dictdata.get('Params')
    dict = {}
    list = dictdata.get('Params').split(',')
    if dictdata.get('Params') == '':
        return dict
    for i in range(len(list)):
        item = list[i]
        kv = item.split(':')
        if kv[1] == '':
            dict[kv[0]] = None
        dict[kv[0]] = kv[1]
    return dict

def getHeaders(dictdata):
    dict = {}
    list = dictdata.get('Headers').split(',')
    if dictdata.get('Headers') == '':
        return dict
    for i in range(len(list)):
        item = list[i]
        kv = item.split(':')
        dict[kv[0]] = kv[1]
    return dict

def getAuth(dictdata):
    dict = {}
    list = dictdata.get('Auth').split(',')
    if dictdata.get('Auth') == '':
        return dict
    for i in range(len(list)):
        item = list[i]
        kv = item.split(':')
        dict[kv[0]] = kv[1]
    return dict

def getConfig(dictdata, rowData=False):
    configPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/Config/Environment.ini'
    host = read_data_from_config(configPath)['base_url']
    path = getPath(dictdata)
    url = host + path
    headers = getHeaders(dictdata)
    method = getMethod(dictdata)
    params = getParams(dictdata, rowData)
    auth = getAuth(dictdata)
    config = {
        "url":url,
        "headers":headers,
        "method":method,
        "params":params,
        "auth":auth,
    }
    return config

# 发送request请求
def sendRequests(method, url, **kwargs):
    r = requests.request(method, url, verify=False, timeout=30, **kwargs)
    print r
    return r

# 将response、响应时间、断言结果写入testdata文件中
def write_result_in_csv(filepath, rowNum, r, result, record=True):
    if record:
        rewrite_data_in_csv(filepath, 'J%d'%(rowNum), r.text)
    else:
        rewrite_data_in_csv(filepath, 'J%d'%(rowNum), r.headers['Content-Disposition'])
    ms = r.elapsed.microseconds / 1000
    rewrite_data_in_csv(filepath, 'K%d'%(rowNum), ms)
    if result:
        rewrite_data_in_csv(filepath, 'L%d'%(rowNum), 'Pass')
    else:
        rewrite_data_in_csv(filepath, 'L%d'%(rowNum), 'Failed')
    rewrite_data_in_csv(filepath, 'N%d'%(rowNum), pfTime.get_current_time())

# 根据condition的bool值来判断断言结果
def assert_condition(caseName, message, condition):
    message = caseName + ":" + message
    if condition:
        message = message + '成功'
        logger.info(message)
    else:
        message = message + '失败'
        logger.error(message)
        #当判断为False，则抛出断言错误
        raise AssertionError(message)