#coding=utf-8

import unittest

# 创建测试套件
def create_test_suite():
    #测试用例存放位置
    test_case_dir = ".\\testsuits"
    test_unit = unittest.TestSuite()

    #discover 方法定义
    test_suites = unittest.defaultTestLoader.discover(test_case_dir, pattern='AT_*.py', top_level_dir=None)

    #discover 方法筛选出来的用例，循环添加到测试套件中
    for test_suite in test_suites:
        for test_case in test_suite:
            test_unit.addTests(test_case)
    return test_unit