#coding=utf-8
import sys,random

from APIS.AddressBookController.UploadAddressBook import UploadAddressBook

sys.path.append("/TestSuits")
from TestSuits import *
userPath = project_dir + '/Data/LoginController/Login/TestData.xlsx'
filepath = project_dir + '/Data/AddressBookController/UploadAddressBook/TestData.xlsx'
print filepath
caseId = 0

class TC001(unittest.TestCase):

    # region 用例初始化
    def setUp(self):
        # 读取当前登录的车信用户信息
        self .Userdicdate = pfFile.read_data_from_csv(userPath)
        self.dictdata = pfFile.read_data_from_csv(filepath)
        self.uploadAddressBook = UploadAddressBook(self.dictdata[caseId])

    # endregion
    def testCase(self):
        '''上传通讯录'''
        print '-'*20, 'AT_CX_UAB_TC001：上传通讯录', '-'*20
        # region step1：登出
        # 取出参数
        user = json.loads(self.Userdicdate[caseId]["Response"])['result']
        request =json.loads(self.dictdata[caseId]["Params"])
        request['userSerial']=user['serial']
        people = request["infos"][0]
        people["firstName"]="JM" + random.choice(['赵','钱','孙','李'])
        people["phones"]=[]
        for item in range(5):
            header=random.choice(['86','+86',''])
            start=random.choice(['13','15','17','18','16'])
            end=''.join(random.sample(['0','1','2','3','4','5','6','7','8','9'],9))
            phone=header + start + end
            people["phones"].append({"phone":phone})
        r = self.uploadAddressBook.send_request(request)
        self.uploadAddressBook.get_status(r)
        # self.deviceId = self.devicestore.get_content(r)
        print "--------------------->"
        # endregion

        # region step2：断言
        result = self.uploadAddressBook.verify_success_return(r)
        # 断言结果写入到excel中的result列
        pfAPI.write_result_in_csv(filepath, caseId+2, r, result)
        pfAPI.assert_condition('AT_CX_UAB_TC001', '：上传通讯录', result)
        # endregion
        # endregion

if __name__ == '__main__':
    unittest.main()

