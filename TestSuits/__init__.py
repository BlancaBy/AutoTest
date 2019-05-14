import os,sys,unittest,ssl,json,requests,json,datetime,time
from dateutil.relativedelta import relativedelta
requests.packages.urllib3.disable_warnings()
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dbpath = project_dir + '/config/database_config.ini'

import Framework.database as database
import Framework.logger as Logger
import Framework.PfAPI as pfAPI
import Framework.PfFile as pfFile
import Framework.PfMisc as pfMisc
import Framework.PfRandom as pfRandom
import Framework.PfSys as pfSys
import Framework.PfTest as pfTest
import Framework.PfTime as pfTime

from APIS.LoginController.Login import Login
from APIS.LoginController.Logout import Logout
from APIS.LoginController.Accredit import Accredit
from APIS.LoginController.CarLogin import CarLogin
from APIS.LoginController.LogoutByPhone import LogoutByPhone
from APIS.LoginController.CarAccredit import CarAccredit

from APIS.CorporationController.CheckCmimToken import CheckCmimToken
from APIS.CorporationController.CorporationLogin import CorperationLogin


from APIS.UserController.UpdateUserinfo import UpdateUserinfo
from APIS.UserController.GetFriendList import GetFriendList
from APIS.UserController.QueryUserDetails import QueryUserDetails


from APIS.AddressBookController.UploadAddressBook import UploadAddressBook
from APIS.AddressBookController.CheckAddressVersion import CheckAdressVersion
from APIS.AddressBookController.FindAddressBook import FindAdressBook
from APIS.AddressBookController.FindAddressVersion import FindAddressVersion



