#coding=utf-8
import sys
from APIS.UserController.GetFriendList import GetFriendList

sys.path.append("/TestSuits")
from TestSuits import *
#用例结果回填Excel
filepath = project_dir + '/Data/UserController/GetFriendList/TestData.xlsx'
#登录结果回填Excel，用于读取response里的result里的thirdToken
userfilepath = project_dir + '/Data/LoginController/Login/TestData.xlsx'
caseId = 0

class TC001(unittest.TestCase):

    # region 用例初始化
    def setUp(self):

        #读取该用例的dicdate
        self.dictdata = pfFile.read_data_from_csv(filepath)
        #读取用户登陆信息
        self.userdictdata=pfFile.read_data_from_csv(userfilepath)
        #调用登录
        self.getFriendList = GetFriendList(self.dictdata[caseId])
    # endregion
    def testCase(self):
        '''获取好友列表'''
        print '-'*20, 'AT_CX_GFL_TC001：获取好友列表', '-'*20
        # region step1：企业登录
        #r=self.userLogin.send_request(self,)
        user = json.loads(self.userdictdata[caseId]["Response"])["result"]
        r = self.getFriendList.send_request(user["userId"])
        print "--------------------->"
        print r
        # endregion

        # region step2：断言
        result = self.getFriendList.verify_success_return(r)
        # 断言结果写入到excel中的result列
        pfAPI.write_result_in_csv(filepath, caseId+2, r, result)
        pfAPI.assert_condition('AT_CX_GFL_TC001', '获取好友列表', result)
        # endregion
        # endregion

if __name__ == '__main__':
    unittest.main()

