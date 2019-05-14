#coding=utf-8
import sys
sys.path.append("/TestSuits")
from TestSuits import *
carPath = project_dir + '/Data/LoginController/CarLogin/TestData.xlsx'
filepath = project_dir + '/Data/LoginController/Logout/TestData.xlsx'
print filepath
caseId = 0

class TC001(unittest.TestCase):

    # region 用例初始化
    def setUp(self):
        # 读取当前登录的车信用户信息
        self .Cardicdate = pfFile.read_data_from_csv(carPath)
        self.dictdata = pfFile.read_data_from_csv(filepath)
        self.logoutByPhone = LogoutByPhone(self.dictdata[caseId])
    # endregion
    def testCase(self):
        '''手机踢车机登陆'''
        print '-'*20, 'AT_CX_LBP_TC001：手机踢车机登陆', '-'*20
        # region step1：登出
        # 取出参数
        car = json.loads(self.Cardicdate[caseId]["Response"])['result']
        request =json.loads(self.dictdata[caseId]["Params"])
        r = self.logoutByPhone.send_request(request["deviceId"],request["deviceType"],car["serial"],request["toCorporationSerial"])
        self.logoutByPhone.get_status(r)
        # self.deviceId = self.devicestore.get_content(r)
        print "--------------------->"
        # endregion

        # region step2：断言
        result = self.logoutByPhone.verify_success_return(r)
        # 断言结果写入到excel中的result列
        pfAPI.write_result_in_csv(filepath, caseId+2, r, result)
        pfAPI.assert_condition('AT_US_UL_TC001', '：手机踢车机登陆', result)
        # endregion
        # endregion

if __name__ == '__main__':
    unittest.main()

