#coding=utf-8
import sys,random

from numpy.core import double

from APIS.CustomMessageController.Pickup import Pickup
from APIS.LocationController.UploadFile import UploadFile
from APIS.SendMessageController.AcceptMess import AcceptMess

sys.path.append("/TestSuits")
from TestSuits import *
userPath = project_dir + '/Data/LoginController/Login/TestData.xlsx'
#sdkPath = project_dir + '/Data/SendMessageController/SdkSendMessages/TestData.xlsx'
#platePath=project_dir + '/Data/SendMessageController/AcceptMess/TestData.xlsx'
filepath = project_dir + '/Data/SendMessageController/AcceptMess/TestData.xlsx'
caseId = 0
class TC001(unittest.TestCase):
    def setUp(self):
        self.dictdata = pfFile.read_data_from_csv(filepath)
        # 在Excel读取用户信息
       # self.dictdataUser = pfFile.read_data_from_csv(userPath)
        self.acceptMess = AcceptMess(self.dictdata[caseId])
    def testCase(self):
        '''接受上行消息'''
        print '-' * 20, 'AT_CX_AM_TC001：接受上行消息', '-' * 20
        #读取excel里的result并转成字典赋值给User
        # user = json.loads(self.dictdata[caseId]["Response"])['result']
        #读取Excel里的参数
        request = json.loads(self.dictdata[caseId]["Params"])
        request['msg_id']="123"
        request['msg_content'] = "测试上行消息"
        request['recv_time'] = "12"
        request['sp_code'] = "12"
        request['src_mobile'] = "12"

        r = self.acceptMess.send_request(request)
        print r.text
        self.acceptMess.get_status(r)
        print "--------------------->"
        # endregion

        # region step2：断言
        result = self.acceptMess.verify_success_return(r)
        # 断言结果写入到excel中的result列
        pfAPI.write_result_in_csv(filepath, caseId + 2, r, result)
        pfAPI.assert_condition('AT_CX_AM_TC001', '：接受上行消息', result)
        # endregion
        # endregion

if __name__ == '__main__':
    unittest.main()