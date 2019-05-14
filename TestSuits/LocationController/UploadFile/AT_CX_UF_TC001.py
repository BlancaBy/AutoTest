#coding=utf-8
import sys,random

from numpy.core import double

from APIS.LocationController.UploadFile import UploadFile

sys.path.append("/TestSuits")
from TestSuits import *
#userPath = project_dir + '/Data/LoginController/Login/TestData.xlsx'
filepath = project_dir + '/Data/LocationController/UploadFile/TestData.xlsx'
gpspath=  project_dir + '/Data/LocationController/UploadFile/gps.gz.txt'
caseId = 0
class TC001(unittest.TestCase):
    def setUp(self):
        self.dictdata = pfFile.read_data_from_csv(filepath)
        # 在Excel读取用户信息
        #self.dictdataUser = pfFile.read_data_from_csv(userPath)
        self.uploadFile = UploadFile(self.dictdata[caseId])
    def testCase(self):
        '''单点位置上传'''
        print '-' * 20, 'AT_CX_UF_TC001：文件位置上传', '-' * 20
        #request=open(gpspath,"rf")
        #读取excel里的result并转成字典赋值给User
        #user = json.loads(self.dictdataUser[caseId]["Response"])['result']
        #读取Excel里的参数
        #request = json.loads(self.dictdata[caseId]["Params"])
        #request['uid']=user["userId"]
        #request["x"]=double(request["x"])+1
        #request["y"]=double(request["y"])+1
        #request["corporation"]="001"
        #print json.dumps(request)
        files={'file':open(gpspath,'rb')}
        r = self.uploadFile.send_request(files)
        print r.text
        self.uploadFile.get_status(r)
        print "--------------------->"
        # endregion

        # region step2：断言
        result = self.uploadFile.verify_success_return(r)
        # 断言结果写入到excel中的result列
        pfAPI.write_result_in_csv(filepath, caseId + 2, r, result)
        pfAPI.assert_condition('AT_CX_UF_TC001', '：文件位置上传', result)
        # endregion
        # endregion

if __name__ == '__main__':
    unittest.main()