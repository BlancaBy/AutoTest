#coding=utf-8
import sys,random

from numpy.core import double

from APIS.LocationController.UploadPoint import UploadPoint

sys.path.append("/TestSuits")
from TestSuits import *
userPath = project_dir + '/Data/LoginController/Login/TestData.xlsx'
filepath = project_dir + '/Data/LocationController/UploadPoint/TestData.xlsx'
caseId = 0
class TC001(unittest.TestCase):
    def setUp(self):
        self.dictdata = pfFile.read_data_from_csv(filepath)
        # 在Excel读取用户信息
        self.dictdataUser = pfFile.read_data_from_csv(userPath)
        self.uploadPoint = UploadPoint(self.dictdata[caseId])
    def testCase(self):
        '''单点位置上传'''
        print '-' * 20, 'AT_CX_UP_TC001：单点位置上传', '-' * 20
        #读取excel里的result并转成字典赋值给User
        user = json.loads(self.dictdataUser[caseId]["Response"])['result']
        #读取Excel里的参数
        request = json.loads(self.dictdata[caseId]["Params"])
        request['uid']=user["userId"]
        request["x"]=double(request["x"])+1
        request["y"]=double(request["y"])+1
        request["corporation"]="001"
        #print json.dumps(request)
        r = self.uploadPoint.send_request(request)
        print r.text
        self.uploadPoint.get_status(r)
        print "--------------------->"
        # endregion

        # region step2：断言
        result = self.uploadPoint.verify_success_return(r)
        # 断言结果写入到excel中的result列
        pfAPI.write_result_in_csv(filepath, caseId + 2, r, result)
        pfAPI.assert_condition('AT_CX_UP_TC001', '：单点位置上传', result)
        # endregion
        # endregion

if __name__ == '__main__':
    unittest.main()