import os,sys,unittest,ssl,json,requests,json,datetime,time
from dateutil.relativedelta import relativedelta
requests.packages.urllib3.disable_warnings()
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dbpath = project_dir + '/config/database_config.ini'

import Framwork.database as database
from Framwork.logger import Logger
import Framwork.PfAPI as pfAPI
import Framwork.PfFile as pfFile
import Framwork.PfMisc as pfMisc
import Framwork.PfRandom as pfRandom
import Framwork.PfSys as pfSys
import Framwork.PfTest as pfTest
import Framwork.PfTime as pfTime


from APIS.User2b.U2BChangePassword import U2BChangePassword
from APIS.User2b.U2BChangeUserPhone import U2BChangeUserPhone
from APIS.User2b.U2BCheckUnique import U2BCheckUnique
from APIS.User2b.U2BCheckUserNamePasswordMatch import U2BCheckUserNamePasswordMatch
from APIS.User2b.U2BRegisterUser import U2BRegisterUser
from APIS.User2b.U2BUpdateUserInfo import U2BUpdateUserInfo
from APIS.User2b.U2BUserInfo import U2BUserInfo
from APIS.User2b.U2BWrittenOff import U2BWrittenOff

from APIS.User2c.U2CChangePassword import U2CChangePassword
from APIS.User2c.U2CChangeUserPhone import U2CChangeUserPhone
from APIS.User2c.U2CCheckUnique import U2CCheckUnique
from APIS.User2c.U2CCheckUserNamePasswordMatch import U2CCheckUserNamePasswordMatch
from APIS.User2c.U2CRegisterUser import U2CRegisterUser
from APIS.User2c.U2CUpdateUserInfo import U2CUpdateUserInfo
from APIS.User2c.U2CUserInfo import U2CUserInfo
from APIS.User2c.U2CWrittenOff import U2CWrittenOff

from APIS.User2OP.U2OPChangePassword import U2OPChangePassword
from APIS.User2OP.U2OPChangeUserPhone import U2OPChangeUserPhone
from APIS.User2OP.U2OPCheckUnique import U2OPCheckUnique
from APIS.User2OP.U2OPCheckUserNamePasswordMatch import U2OPCheckUserNamePasswordMatch
from APIS.User2OP.U2OPRegisterUser import U2OPRegisterUser
from APIS.User2OP.U2OPUpdateUserInfo import U2OPUpdateUserInfo
from APIS.User2OP.U2OPUserInfo import U2OPUserInfo
from APIS.User2OP.U2OPWrittenOff import U2OPWrittenOff

from APIS.SimCard.Activation import Activation
from APIS.SimCard.SimCardInfo import SimCardInfo
from APIS.SimCard.Store import Store
from APIS.SimCard.WrittenOff import WrittenOff

from APIS.Enterprise.DeleteEnterprise import DeleteEnterprise
from APIS.Enterprise.EnterpriseInfo import EnterpriseInfo
from APIS.Enterprise.StoreEnterprise import StoreEnterprise
from APIS.Enterprise.UpdateEnterpriseInfo import UpdateEnterpriseInfo

from APIS.Enterprise.BindEnterprise import BindEnterprise
from APIS.Enterprise.EnterpriseByUserId import EnterpriseByUserId
from APIS.Enterprise.UnbindEnterprise import UnbindEnterprise
from APIS.Enterprise.UserByEnterpriseId import UserByEnterpriseId

from APIS.UserSimCard.UserSimCardBind import UserSimCardBind
from APIS.UserSimCard.UserSimCardList import UserSimCardList
from APIS.UserSimCard.UserSimCardInfo import UserSimCardInfo
from APIS.UserSimCard.UserSimCardUnbind import UserSimCardUnbind

from APIS.UserThirdParty.ThirdPartyById import ThirdPartyById
from APIS.UserThirdParty.UserThirdPartyBind import UserThirdPartyBind
from APIS.UserThirdParty.UserInfoById import UserInfoById
from APIS.UserThirdParty.UserThirdPartyUnbind import UserThirdPartyUnbind

from APIS.Device.DeleteDevice import DeleteDevice
from APIS.Device.DeviceInfo import DeviceInfo
from APIS.Device.DeviceStore import DeviceStore
from APIS.Device.UpdateDeviceInfo import UpdateDeviceInfo

from APIS.DeviceSimCard.DeviceSimCardBind import DeviceSimCardBind
from APIS.DeviceSimCard.DeviceInfoBySimCardId import DeviceInfoBySimCardId
from APIS.DeviceSimCard.SimCardInfoByDeviceId import SimCardInfoByDeviceId
from APIS.DeviceSimCard.DeviceSimCardUnbind import DeviceSimCardUnbind

from APIS.DeviceUser.DeviceInfoByUserId import DeviceInfoByUserId
from APIS.DeviceUser.UserInfoByDeviceId import UserInfoByDeviceId
from APIS.DeviceUser.DeviceUserBind import DeviceUserBind
from APIS.DeviceUser.DeviceUserUnbind import DeviceUserUnbind

from APIS.Vehicle.UpdateVehicleInfo import UpdateVehicleInfo
from APIS.Vehicle.DeleteVehicle import DeleteVehicle
from APIS.Vehicle.StoreVehicle import StoreVehicle
from APIS.Vehicle.VehicleInfoById import VehicleInfoById

from APIS.VehicleSimCard.VehicleSimCardBind import VehicleSimCardBind
from APIS.VehicleSimCard.SimCardInfoByVehicleId import SimCardInfoByVehicleId
from APIS.VehicleSimCard.VehicleSimCardUnbind import VehicleSimCardUnbind
from APIS.VehicleSimCard.VehicleInfoBySimCardId import VehicleInfoBySimCardId

from APIS.VehicleUser.UserInfoByVehicleId import UserInfoByVehicleId
from APIS.VehicleUser.VehicleUserBind import VehicleUserBind
from APIS.VehicleUser.VehicleUserUnbind import VehicleUserUnbind
from APIS.VehicleUser.VehicleInfoByUserId import VehicleInfoByUserId

from APIS.VehicleDevice.DeviceInfoByVehicleId import DeviceInfoByVehicleId
from APIS.VehicleDevice.VehicleDeviceBind import VehicleDeviceBind
from APIS.VehicleDevice.VehicleDeviceUnbind import VehicleDeviceUnbind
from APIS.VehicleDevice.VehicleInfoByDeviceId import VehicleInfoByDeviceId

from APIS.Operate.StoreOperate import StoreOperate
from APIS.Operate.DeleteOperate import DeleteOperate
from APIS.Operate.GetOperateInfo import GetOperateInfo
from APIS.Operate.UpdateOperateInfo import UpdateOperateInfo

from APIS.User.UserLogin import UserLogin