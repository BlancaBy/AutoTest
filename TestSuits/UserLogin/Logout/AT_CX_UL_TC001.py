#coding=utf-8
import sys
sys.path.append("/TestSuits")
from TestSuits import *


userPath = project_dir + '/Data/UserLogin/Login/TestData.xlsx'
filepath = project_dir + '/Data/UserLogin/Logout/TestData.xlsx'
print filepath
caseId = 0

class TC001(unittest.TestCase):

    # region 用例初始化
    def setUp(self):
        print "用例初始化"
        # 读取当前用户登录信息
        responseStr = pfFile.read_data_from_csv(userPath)[0]["Response"]
        self.userInfo = json.loads(responseStr)["result"]
        print self.userInfo
        self.dictdata = pfFile.read_data_from_csv(filepath)
        print "读取完文件"
        self.userLogout = Logout(self.dictdata[caseId])
        self.deviceId = ''
        print "setup"
    # endregion

    def tearDown(self):
        # region 数据库操作
        # self.devicestore.delete_device_from_db(dbpath, self.deviceId)
        # endregion
        print "tearDown"

    def testCase(self):
        '''登出'''
        print '-'*20, 'AT_US_UL_TC001：登陆', '-'*20
        # region step1：登出
        # 取出参数
        request = self.dictdata[caseId]["Params"]
        r = self.userLogout.send_request(request)
        self.userLogout.get_messageCode(r)
        # self.deviceId = self.devicestore.get_content(r)
        print "--------------------->"
        print r
        # endregion

        # region step2：断言
        result = self.userLogout.verify_success_return(r)
        # 断言结果写入到excel中的result列
        pfAPI.write_result_in_csv(filepath, caseId+2, r, result)
        pfAPI.assert_condition('AT_US_UL_TC001', '：登出', result)
        # endregion
        # endregion

if __name__ == '__main__':
    unittest.main()

