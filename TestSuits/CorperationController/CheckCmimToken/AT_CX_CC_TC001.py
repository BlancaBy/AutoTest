#coding=utf-8
import sys

from APIS.CorporationController.CheckCmimToken import CheckCmimToken
from APIS.CorporationController.CorporationLogin import CorperationLogin

sys.path.append("/TestSuits")
from TestSuits import *
#用例结果回填Excel
filepath = project_dir + '/Data/CorporationController/CheckCmimToken/TestData.xlsx'
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
        #self.userLogin=Login(self.userdictdata[caseId])

        self.checkCmimToken = CheckCmimToken(self.dictdata[caseId])
    # endregion
    def testCase(self):
        '''校验cmimToken'''
        print '-'*20, 'AT_CX_CC_TC001：校验cmimToken', '-'*20
        # region step1：企业登录
        #r=self.userLogin.send_request(self,)
        user = json.loads(self.userdictdata[caseId]["Response"])["result"]
        r = self.checkCmimToken.send_request(user["thirdPartyToken"],"001")
        print "--------------------->"
        print r
        # endregion

        # region step2：断言
        result = self.checkCmimToken.verify_success_return(r)
        # 断言结果写入到excel中的result列
        pfAPI.write_result_in_csv(filepath, caseId+2, r, result)
        pfAPI.assert_condition('AT_CX_CC_TC001', '校验cmimToken', result)
        # endregion
        # endregion

if __name__ == '__main__':
    unittest.main()

