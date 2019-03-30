# -*- coding: utf-8 -*-
import os

if __name__ == '__main__':
    '''单独运行这个文件可以将所有第三方的依赖包全部安装起来'''
    project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    installFile = project_dir + '/Tools/requirements'
    os.system('pip2 install -r '+installFile)
