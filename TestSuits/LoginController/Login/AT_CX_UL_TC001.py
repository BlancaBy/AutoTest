#coding=utf-8
import sys
sys.path.append("/TestSuits")
from TestSuits import *

filepath = project_dir + '/Data/LoginController/Login/TestData.xlsx'
print filepath
caseId = 0

class TC001(unittest.TestCase):

    # region 用例初始化
    def setUp(self):
        self.dictdata = pfFile.read_data_from_csv(filepath)
        self.userlogin = Login(self.dictdata[caseId])
    # endregion
    def testCase(self):
        '''登陆'''
        print '-'*20, 'AT_US_UL_TC001：登陆', '-'*20
        # region step1：登陆
        request = json.loads(self.dictdata[caseId]["Params"])
        r = self.userlogin.send_request(request["authCode"], request["encrytedData"],request["fromCorporationSerial"],request["toCorporationSerial"])
        self.userlogin.get_messageCode(r)
        # self.deviceId = self.devicestore.get_content(r)
        print "--------------------->"
        print r
        # endregion

        # region step2：断言
        result = self.userlogin.verify_success_return(r)
        # 断言结果写入到excel中的result列
        pfAPI.write_result_in_csv(filepath, caseId+2, r, result)
        pfAPI.assert_condition('AT_US_UL_TC001', '登陆', result)
        # endregion
        # endregion

if __name__ == '__main__':
    unittest.main()

