#coding=utf-8
import sys,random

from APIS.UserController.Refresh import Refresh
from APIS.UserController.UpdateUserinfo import UpdateUserinfo

sys.path.append("/TestSuits")
from TestSuits import *
#userPath = project_dir + '/Data/LoginController/Login/TestData.xlsx'
filepath = project_dir + '/Data/UserController/Refresh/TestData.xlsx'
caseId = 0
class TC001(unittest.TestCase):
    def setUp(self):
        self.dictdata = pfFile.read_data_from_csv(filepath)
        # 在Excel读取用户信息
        #self.dictdataUser = pfFile.read_data_from_csv(userPath)
        self.refresh = Refresh(self.dictdata[caseId])
    def testCase(self):
        '''刷新用户信息'''
        print '-' * 20, 'AT_CX_R_TC001：刷新用户信息', '-' * 20
        #读取excel里的result并转成字典赋值给User
        #user = json.loads(self.dictdataUser[caseId]["Response"])['result']
        #读取Excel里的参数
        request = json.loads(self.dictdata[caseId]["Params"])
       # request['userId']=user["userId"]
        #request["nickName"]="JM" + random.choice(['赵','钱','孙','李'])
        #print json.dumps(request)
        #传入参数，UserId=user.userId,nikeName=params.nikeName
        r = self.refresh.send_request(request)
        print r.text
        self.refresh.get_status(r)
        print "--------------------->"
        # endregion

        # region step2：断言
        result = self.refresh.verify_success_return(r)
        # 断言结果写入到excel中的result列
        pfAPI.write_result_in_csv(filepath, caseId + 2, r, result)
        pfAPI.assert_condition('AT_CX_R_TC001', '：刷新用户信息', result)
        # endregion
        # endregion

if __name__ == '__main__':
    unittest.main()