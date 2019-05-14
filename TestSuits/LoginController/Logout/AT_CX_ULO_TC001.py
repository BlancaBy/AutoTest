#coding=utf-8
import sys
sys.path.append("/TestSuits")
from TestSuits import *
userPath = project_dir + '/Data/LoginController/Login/TestData.xlsx'
filepath = project_dir + '/Data/LoginController/Logout/TestData.xlsx'
print filepath
caseId = 0

class TC001(unittest.TestCase):

    # region 用例初始化
    def setUp(self):
        # 读取当前用户登录信息
        responseStr = pfFile.read_data_from_csv(userPath)[0]["Response"]
        self.userInfo = json.loads(responseStr)["result"]
        #print self.userInfo
        self.dictdata = pfFile.read_data_from_csv(filepath)
        self.userLogout = Logout(self.dictdata[caseId])
    # endregion
    def testCase(self):
        '''登出'''
        print '-'*20, 'AT_US_ULO_TC001：登出', '-'*20
        # region step1：登出
        # 取出参数
        request = self.dictdata[caseId]["Params"]
        r = self.userLogout.send_request(request)
        self.userLogout.get_messageCode(r)
        # self.deviceId = self.devicestore.get_content(r)
        print "--------------------->"
        # endregion

        # region step2：断言
        result = self.userLogout.verify_success_return(r)
        # 断言结果写入到excel中的result列
        pfAPI.write_result_in_csv(filepath, caseId+2, r, result)
        pfAPI.assert_condition('AT_US_ULO_TC001', '：登出', result)
        # endregion
        # endregion

if __name__ == '__main__':
    unittest.main()

