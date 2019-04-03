# coding=utf-8
import os, json
import Framwork.PfAPI as pfAPI
import Framwork.PfFile as pfFile
import Framwork.PfTime as pfTime
import Framwork.database as database

project_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class Logout():
    '''
    用户登出
    method:post
    {
    deviceId (string, optional): 设备Id,可选 ,
    deviceType (string): 设备类型 ,
    serial (string): 车信用户序列号 ,
    toCorporationSerial (string): 杭研的企业号(必传:002)
    }
    '''

    # region 初始化
    def __init__(self, dictdata):
        self.dictdata = dictdata
        self.config = pfAPI.getConfig(self.dictdata)
        self.params = json.loads(self.dictdata.get('Params'))
        self.headers = self.config['headers']  # 字符串转成字典

    # endregion

    # region 业务操作
    # 发送request
    def send_request(self, request):
        # 发送request请求
        r = pfAPI.sendRequests(self.config['method'], self.config['url'], headers=self.headers, data=request,
                               auth=self.config['auth'])
        return r

    # 获取response中的message值
    def get_message(self, r):
        res = json.loads(r.text)
        return res['messages'][0]

    # 获取response中的messageCode值
    def get_messageCode(self, r):
        res = json.loads(r.text)
        print res
        return res['messages']

    # 获取response中的statusCode值
    def get_statusCode(self, r):
        res = json.loads(r.text)
        return res['status']

    # 获取response中的content值
    def get_content(self, r):
        res = json.loads(r.text)
        return res['content']

    # region 检查点
    # 对response进行断言
    def verify_success_return(self, r):
        status_code = r.status_code
        status = self.get_statusCode(r)
        message = self.get_message(r)
        result = bool(status == "0000_0") and \
                 bool(status_code == 200) and bool(message == '执行成功')
        '''
         and \
         bool(self.get_content(r) == self.get_data_from_db(dbpath, 'id'))
         '''
        return result
    # endregion
