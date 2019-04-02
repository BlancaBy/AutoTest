# coding=utf-8
import os, json
import Framwork.PfAPI as pfAPI
import Framwork.PfFile as pfFile
import Framwork.PfTime as pfTime
import Framwork.database as database

project_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class Login():
    ''' 用户登录
        Method：POST
        URL：https://<base url>/user/v0/login
        参数：
        {
        "authCode": "vj",
        deviceId": "5BE+ZUUceq3Ycc5MfkElB/VMsKGyG+AqqOo8//JCMy9hp0Z3AiARLedPgG+9gOjOHwGqdcWjPbPtdDjDQqF6+U8tvTfrmQmZRhKmIZg0RpHfQZjEa7wDuHuKuvGQvIY5LvTI47vC3Oy9W2CUG0E4FKw+a0mxZM48CzQx+AOpASH6uE+ABKCkDDuEFFhOErfz3IiL+8AcLEqgExfNy3Cg==",
        "deviceType": "0001",
        "encrytedData": "vj5BE+ZUUceq3Ycc5MfkElB/VMsKGyG+AqqOo8//JCMy9hp0Z3AiARLedPgG+9gOjOHwGqdcWjPbPtdDjDQqF6+U8tvTfrmQmZRhKmIZg0RpHfQZjEa7wDuHuKuvGQvIY5LvTI47vC3Oy9W2CUG0E+Cql3dJEXDe727wcz2oSNSWO0pe6HrOdaV4jkfxiCAzemVumwqe1pKU/O6rmJWKEI7/FrRQi/Qtj7/nkWuzlVQ1ZLraxRy2EMx8Msjbs1Cb",
        "fromCorporationSerial": "001",
        sequenceId": "001",
        "toCorporationSerial": "002"
        "deviceType": "0",
        "deviceId": "001",
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
    def send_request(self, authCode, encrytedData, fromCorporationSerial, toCorporationSerial):
        self.params['authCode'] = authCode
        self.params['encrytedData'] = encrytedData
        self.params['fromCorporationSerial'] = fromCorporationSerial
        self.params['toCorporationSerial'] = toCorporationSerial
        data = json.dumps(self.params)  # 字典转成字符串
        # 发送request请求
        r = pfAPI.sendRequests(self.config['method'], self.config['url'], headers=self.headers, data=data,
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
