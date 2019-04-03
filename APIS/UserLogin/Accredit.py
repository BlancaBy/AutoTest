# coding=utf-8
import os, json
import Framwork.PfAPI as pfAPI
project_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
class Accredit():
    '''
    用户登录
        Method：POST
        URL：https://<base url>/user/v0/accredit
        参数： {
        authCode (string): 上汽给到的authCode ,
        deviceId (string): 上汽给到的deviceId ,
        deviceType (string): 上汽给到的deviceType,手机端用app表示,车机端用vehicle ,
        encrytedData (string, optional): 上汽给到的encrytedData ,
        fromCorporationSerial (string): 上汽的企业号(必传:001) ,
        sendToPhone (string, optional): 发送登录消息给手机端（只限车机登录使用） ,
        sequenceId (string),
        toCorporationSerial (string): 杭研的企业号(必传:002)
        }
    '''
    # region 初始化
    def __init__(self,dicdata):
        self.dicdata=dicdata
        self.config=pfAPI.getConfig(self.dicdata)
        self.params=json.loads(self.dicdata.get('param'))
        self.headers=self.Config['headers']
    # endregion
    # region 业务操作
    # 发送request
    def send_request(self, authCode, encrytedData, fromCorporationSerial, toCorporationSerial):
        self.params['authCode']=authCode
        self.params['encrytedData']=encrytedData
        self.params['fromCorporationSerial']=fromCorporationSerial
        self.params['toCorporationSerial']=toCorporationSerial
        data = json.dumps(self.params)  # 字典转成字符串
        r=pfAPI.sendRequests(self.config['url'],self.config['method'],headers=self.headers,data=data,auth=self.config['auth'])
        return r
    # 获取response中的message值
    def get_message(self,r):
        res=json.loads(r.text)
        return res['message']
    # 获取response中的messageCode值
    def get_messageCode(self,r):
         res=json.loads('message')
         return res['messageCode']
    # 获取response中的status值
    def get_status(self,r):
        res=json.loads(r.text)
        return res['status']
     # 获取response中的statusCode值
    def get_statusCode(self, r):
        res = json.loads(r.text)
        return res['statusCode']
    # 获取response中的content值
    def get_content(self,r):
        res=json.loads(r.text)
        return res['content']
    # region 检查点

    # 对response进行断言
    def verify_success_return(self, r):
        statusCode=r.statusCode(r)
        message=self.get_message(r)
        status=self.get_status(r)
        result = bool(status == "0000_0") and \
                 bool(statusCode == 200) and bool(message == '执行成功')
        return result