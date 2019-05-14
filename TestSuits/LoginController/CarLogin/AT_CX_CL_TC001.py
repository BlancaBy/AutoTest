#coding=utf-8
import sys

from APIS.LoginController.CarLogin import CarLogin

sys.path.append("/TestSuits")
from TestSuits import *
userPath = project_dir + '/Data/LoginController/Login/TestData.xlsx'
filepath = project_dir + '/Data/LoginController/CarLogin/TestData.xlsx'
caseId = 0
class TC001(unittest.TestCase):
    def setUp(self):
        self.dictdata = pfFile.read_data_from_csv(filepath)
        self.carLogin = CarLogin(self.dictdata[caseId])
    def testCase(self):
        '''车机登陆'''
        print '-' * 20, 'AT_CX_CL_TC001：车机登陆', '-' * 20
        request = json.loads(self.dictdata[caseId]["Params"])
        r = self.carLogin.send_request(request["authCode"],request["encrytedData"],request["fromCorporationSerial"],request["toCorporationSerial"],request["sendToPhone"],request["deviceId"],request["deviceType"])
        self.carLogin.get_status(r)
        print "--------------------->"
        # endregion

        # region step2：断言
        result = self.carLogin.verify_success_return(r)
        # 断言结果写入到excel中的result列
        pfAPI.write_result_in_csv(filepath, caseId + 2, r, result)
        pfAPI.assert_condition('AT_CX_CL_TC001', '：车机登陆', result)
        # endregion
        # endregion

if __name__ == '__main__':
    unittest.main()