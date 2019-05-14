# coding=utf-8
import os, json
import Framework.PfAPI as pfAPI
project_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
class PlatformSendMessages():
    '''
    用户登录
        Method：POST
        URL：https://<base url>/user/v0/platformSendMessages
        参数：
        {
        "data": {},
        "messType": 0,
        "phoneNum": "string",
        "receiverName": "string",
        "senderName": "string",
        "userSerial": "string"
        }
    '''
    # region 初始化
    def __init__(self,dicdata):
        self.dicdata=dicdata
        self.config=pfAPI.getConfig(self.dicdata)
        self.params = self.config['params']
        self.headers=self.config['headers']

    # endregion
    # region 业务操作
    # 发送request
    def send_request(self, request):
        data = json.dumps(request)  # 字典转成字符串
        r=pfAPI.sendRequests(self.config['method'],self.config['url'],headers=self.headers,data=data,auth=self.config['auth'])
        return r
    # 获取response中的message值
    def get_message(self,r):
        res=json.loads(r.text)
        return res['messages']
    # 获取response中的messageCode值
    def get_messageCode(self,r):
         res=json.loads(r.text)
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
        statusCode=r.status_code
        message=self.get_message(r)[0]
        status=self.get_status(r)
        result = (bool(status == "0000_0") or bool(status == "0002_5")) and \
                 bool(statusCode == 200) and (bool(message == '执行成功')or bool(message == '您今天已经给该用户发送过邀请短信了'))
        return result