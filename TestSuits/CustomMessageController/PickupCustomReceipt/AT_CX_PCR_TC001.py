#coding=utf-8
import sys,random

from numpy.core import double

from APIS.CustomMessageController.Pickup import Pickup
from APIS.CustomMessageController.PickupCustomReceipt import PickupCustomReceipt
from APIS.LocationController.UploadFile import UploadFile
sys.path.append("/TestSuits")
from TestSuits import *
userPath = project_dir + '/Data/LoginController/Login/TestData.xlsx'
filepath = project_dir + '/Data/CustomMessageController/PickupCustomReceipt/TestData.xlsx'
caseId = 0
class TC001(unittest.TestCase):
    def setUp(self):
        self.dictdata = pfFile.read_data_from_csv(filepath)
        # 在Excel读取用户信息
        self.dictdataUser = pfFile.read_data_from_csv(userPath)
        self.pickupCustomReceipt = PickupCustomReceipt(self.dictdata[caseId])
    def testCase(self):
        '''接人推送自定义消息回执'''
        print '-' * 20, 'AT_CX_PRC_TC001：接人推送自定义消息回执', '-' * 20
        #读取excel里的result并转成字典赋值给User
        user = json.loads(self.dictdataUser[caseId]["Response"])['result']
        #读取Excel里的参数
        request = json.loads(self.dictdata[caseId]["Params"])
        request['to']=user["userId"]
        r = self.pickupCustomReceipt.send_request(request)
        print r.text
        self.pickupCustomReceipt.get_status(r)
        print "--------------------->"
        # endregion

        # region step2：断言
        result = self.pickupCustomReceipt.verify_success_return(r)
        # 断言结果写入到excel中的result列
        pfAPI.write_result_in_csv(filepath, caseId + 2, r, result)
        pfAPI.assert_condition('AT_CX_PCR_TC001', '：接人推送自定义消息回执', result)
        # endregion
        # endregion

if __name__ == '__main__':
    unittest.main()