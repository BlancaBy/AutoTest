#coding=utf-8
import sys

from APIS.LoginController.CarAccredit import CarAccredit
sys.path.append("/TestSuits")
from TestSuits import *
userPath = project_dir + '/Data/LoginController/Login/TestData.xlsx'
filepath = project_dir + '/Data/LoginController/CarAccredit/TestData.xlsx'
caseId = 0
class TC001(unittest.TestCase):
    def setUp(self):
        self.dictdata = pfFile.read_data_from_csv(filepath)
        self.carAccredit = CarAccredit(self.dictdata[caseId])
        responseStr = pfFile.read_data_from_csv(userPath)[0]["Response"]
        self.userInfo = json.loads(responseStr)["result"]

    def testCase(self):
        '''确认车机登陆'''
        print '-' * 20, 'AT_CX_CA_TC001：确认车机登陆', '-' * 20
        p = self.dictdata[caseId]["Params"]
        request = json.loads(p)
        r = self.carAccredit.send_request(self.userInfo['serial'],self.userInfo["userId"],request["fromCorporationSerial"],request["isConfirm"],request["deviceId"])
        self.carAccredit.get_status(r)
        print "--------------------->"
        # endregion

        # region step2：断言
        result = self.carAccredit.verify_success_return(r)
        # 断言结果写入到excel中的result列
        pfAPI.write_result_in_csv(filepath, caseId + 2, r, result)
        pfAPI.assert_condition('AT_CX_CA_TC001', '：确认车机登陆', result)
        # endregion
        # endregion

if __name__ == '__main__':
    unittest.main()