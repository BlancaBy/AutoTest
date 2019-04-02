#coding=utf-8
import sys
sys.path.append("/TestSuits")
from TestSuits import *



filepath = project_dir + '/Data/UserLogin/Login/TestData.xlsx'
print filepath
caseId = 0

class TC001(unittest.TestCase):

    # region 用例初始化
    def setUp(self):
        print "用例初始化"
        self.dictdata = pfFile.read_data_from_csv(filepath)
        print "读取完文件"
        self.userlogin = Login(self.dictdata[caseId])
        self.deviceId = ''
        print "setup"
    # endregion

    def tearDown(self):
        # region 数据库操作
        # self.devicestore.delete_device_from_db(dbpath, self.deviceId)
        # endregion
        print "tearDown"

    def testCase(self):
        '''登陆'''
        print '-'*20, 'AT_US_UL_TC001：登陆', '-'*20
        # region step1：登陆
        authCode = 'vj5BE+ZUUceq3Ycc5MfkElB/VMsKGyG+AqqOo8//JCMy9hp0Z3AiARLedPgG+9gOjOHwGqdcWjPbPtdDjDQqF6+U8tvTfrmQmZRhKmIZg0RpHfQZjEa7wDuHuKuvGQvIY5LvTI47vC3Oy9W2CUG0E4FKw+a0mxZM48CzQx+AOpASH6uE+ABKCkDDuEFFhOErfz3IiL+8AcLEqgExfNy3Cg=='
        encrytedData = 'vj5BE+ZUUceq3Ycc5MfkElB/VMsKGyG+AqqOo8//JCMy9hp0Z3AiARLedPgG+9gOjOHwGqdcWjPbPtdDjDQqF6+U8tvTfrmQmZRhKmIZg0RpHfQZjEa7wDuHuKuvGQvIY5LvTI47vC3Oy9W2CUG0E+Cql3dJEXDe727wcz2oSNSWO0pe6HrOdaV4jkfxiCAzemVumwqe1pKU/O6rmJWKEI7/FrRQi/Qtj7/nkWuzlVQ1ZLraxRy2EMx8Msjbs1Cb'
        fromCorporationSerial = '001'
        toCorporationSerial = '002'
        r = self.userlogin.send_request(authCode, encrytedData, fromCorporationSerial, toCorporationSerial)
        self.userlogin.get_messageCode(r)
        # self.deviceId = self.devicestore.get_content(r)
        print "--------------------->"
        print r
        # endregion

        # region step2：断言
        result = self.userlogin.verify_success_return(r)
        # 断言结果写入到excel中的result列
        pfAPI.write_result_in_csv(filepath, caseId+2, r, result)
        pfAPI.assert_condition('AT_US_UL_TC001', '第一步：登陆', result)
        # endregion
        # endregion

if __name__ == '__main__':
    unittest.main()

