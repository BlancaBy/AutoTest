#coding=utf-8
import sys

from APIS.AddressBookController.FindAddressBook import FindAdressBook

sys.path.append("/TestSuits")
from TestSuits import *
userPath = project_dir + '/Data/LoginController/Login/TestData.xlsx'
filepath = project_dir + '/Data/AddressBookController/FindAddressBook/TestData.xlsx'
print filepath
caseId = 0

class TC001(unittest.TestCase):

    # region 用例初始化
    def setUp(self):
        # 读取当前登录的车信用户信息
        self .userdicdate = pfFile.read_data_from_csv(userPath)
        self.dictdata = pfFile.read_data_from_csv(filepath)
        self.findAdressBook = FindAdressBook(self.dictdata[caseId])
    # endregion
    def testCase(self):
        '''查看通讯录'''
        print '-'*20, 'AT_CX_FA_TC001：查看通讯录', '-'*20
        # region step1：登出
        # 取出参数
        user = json.loads(self.userdicdate[caseId]["Response"])['result']
        #request =json.loads(self.dictdata[caseId]["Params"])
        r = self.findAdressBook.send_request(user["serial"])
        self.findAdressBook.get_status(r)
        # self.deviceId = self.devicestore.get_content(r)
        print "--------------------->"
        # endregion

        # region step2：断言
        result = self.findAdressBook.verify_success_return(r)
        # 断言结果写入到excel中的result列
        pfAPI.write_result_in_csv(filepath, caseId+2, r, result)
        pfAPI.assert_condition('AT_CX_FA_TC001', '：查看通讯录', result)
        # endregion
        # endregion

if __name__ == '__main__':
    unittest.main()

