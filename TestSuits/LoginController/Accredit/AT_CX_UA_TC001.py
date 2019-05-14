#coding=utf-8
import sys
sys.path.append("/TestSuits")
from TestSuits import *
#userPath = project_dir + '/Data/LoginController/Login/TestData.xlsx'
filepath = project_dir + '/Data/LoginController/Accredit/TestData.xlsx'
caseId = 0
class TC001(unittest.TestCase):
    def setUp(self):
        self.dictdata = pfFile.read_data_from_csv(filepath)
        self.accredit = Accredit(self.dictdata[caseId])
    def testCase(self):
        '''用户授权'''
        print '-' * 20, 'AT_US_UL_TC001：用户授权', '-' * 20
        request = json.loads(self.dictdata[caseId]["Params"])
        r = self.accredit.send_request(request)
        self.accredit.get_status(r)
        print "--------------------->"
        # endregion

        # region step2：断言
        result = self.accredit.verify_success_return(r)
        # 断言结果写入到excel中的result列
        pfAPI.write_result_in_csv(filepath, caseId + 2, r, result)
        pfAPI.assert_condition('AT_CX_UA_TC001', '：授权', result)
        # endregion
        # endregion

if __name__ == '__main__':
    unittest.main()