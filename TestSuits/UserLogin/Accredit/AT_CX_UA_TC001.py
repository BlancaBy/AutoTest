#coding=utf-8
import sys
sys.path.append("/TestSuits")
from TestSuits import *
userPath = project_dir + '/Data/UserLogin/Login/TestData.xlsx'
filepath = project_dir + '/Data/UserLogin/Accredit/TestData.xlsx'
print filepath
caseId = 0
class TC001(unittest.TestCase):
    def setup(self):
        self.dictdata = pfFile.read_data_from_csv(filepath)
        self.Accredit = Accredit(self.dictdata[caseId])

def testCase(self):
    '''用户授权'''
    print '-' * 20, 'AT_US_UL_TC001：登陆', '-' * 20
    request = self.dictdata[caseId]["Params"]
    r = self.userLogout.send_request(request)
    self.userLogout.get_messageCode(r)
    print "--------------------->"
    # endregion

    # region step2：断言
    result = self.Accredit.verify_success_return(r)
    # 断言结果写入到excel中的result列
    pfAPI.write_result_in_csv(filepath, caseId + 2, r, result)
    pfAPI.assert_condition('AT_CX_UA_TC001', '：授权', result)
    # endregion
    # endregion


if __name__ == '__main__':
    unittest.main()