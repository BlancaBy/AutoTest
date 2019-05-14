#coding=utf-8
import sys,random

from numpy.core import double

from APIS.CustomMessageController.Pickup import Pickup
from APIS.CustomMessageController.PickupCustomReceipt import PickupCustomReceipt
from APIS.CustomMessageController.PushCustomMessage import PushCustomMessage
from APIS.LocationController.UploadFile import UploadFile
from APIS.SendMessageController.SdkSendMessages import SdkSendMessages

sys.path.append("/TestSuits")
from TestSuits import *
userPath = project_dir + '/Data/LoginController/Login/TestData.xlsx'
filepath = project_dir + '/Data/SendMessageController/SdkSendMessages/TestData.xlsx'
caseId = 0
class TC001(unittest.TestCase):
    def setUp(self):
        self.dictdata = pfFile.read_data_from_csv(filepath)
        # 在Excel读取用户信息
        self.dictdataUser = pfFile.read_data_from_csv(userPath)
        self.sdkSendMessages = SdkSendMessages(self.dictdata[caseId])
    def testCase(self):
        '''SDK发送消息'''
        print '-' * 20, 'AT_CX_SSM_TC001：SDK发送消息', '-' * 20
        #读取excel里的result并转成字典赋值给User
        user = json.loads(self.dictdataUser[caseId]["Response"])['result']
        #读取Excel里的参数
        request = json.loads(self.dictdata[caseId]["Params"])
        request['userSerial']=user["serial"]
        r = self.sdkSendMessages.send_request(request)
        print r.text
        self.sdkSendMessages.get_status(r)
        print "--------------------->"
        # endregion

        # region step2：断言
        result = self.sdkSendMessages.verify_success_return(r)
        # 断言结果写入到excel中的result列
        pfAPI.write_result_in_csv(filepath, caseId + 2, r, result)
        pfAPI.assert_condition('AT_CX_SSM_TC001', '：SDK发送消息', result)
        # endregion
        # endregion


if __name__ == '__main__':
    unittest.main()