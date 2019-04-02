from Framwork.PfAPI import *
UserURL=[
    #用户相关
    'user/v0/userInfo/queryUserDetails/${userId}'#查看用户信息
    'user/v0/userInfo/update'#更改用户信息
     'user/v0/carLogin'#车机登陆
     'user/v0/carAccredit'#确认车机登陆
     'user/v0/logoutByPhone'#踢车机登陆
     'user/v0/logout'#手动登出
    #通讯录相关
     'user/v0/addressBook/upload'#上传通讯录
     'user/v0/addressBook/find?userSerial=${serial}'#获取通讯录
     'user/v0/addressBook/findAddressVersion?userSerial=${serial}'#获取通讯录版本
     'user/v0/userInfo/getFriendList?userId=96921167548397'#获取好友列表
    ]

configPath = './Environment.ini'
host = read_data_from_config(configPath)['base_url']
fullUrl = map(lambda url:host+url,UserURL)
def sdkhasurl(url):
  if url.index("user/v0/userInfo/queryUserDetails/")>-1 or url.index("user/v0/addressBook/find?")>-1 or 'user/v0/addressBook/findAddressVersion?':
    return True
  else:
      return url in fullUrl