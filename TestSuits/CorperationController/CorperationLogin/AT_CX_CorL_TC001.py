#coding=utf-8
import sys
from APIS.CorporationController.CorporationLogin import CorperationLogin
sys.path.append("/TestSuits")
from TestSuits import *

filepath = project_dir + '/Data/CorporationController/CorporationLogin/TestData.xlsx'
print filepath
caseId = 0

class TC001(unittest.TestCase):

    # region 用例初始化
    def setUp(self):
        self.dictdata = pfFile.read_data_from_csv(filepath)
        self.corporationLogin = CorperationLogin(self.dictdata[caseId])
    # endregion
    def testCase(self):
        '''企业登陆'''
        print '-'*20, 'AT_CX_CorL_TC001：企业登陆', '-'*20
        # region step1：企业登录
        request = json.loads(self.dictdata[caseId]["Params"])
        r = self.corporationLogin.send_request(request["accountName"],request["accountPwd"],request["corporationSerial"])

        print "--------------------->"
        print r
        # endregion

        # region step2：断言
        result = self.corporationLogin.verify_success_return(r)
        # 断言结果写入到excel中的result列
        pfAPI.write_result_in_csv(filepath, caseId+2, r, result)
        pfAPI.assert_condition('AT_CX_CorL_TC001', '企业登录', result)
        # endregion
        # endregion

if __name__ == '__main__':
    unittest.main()

