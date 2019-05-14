#coding=utf-8

import random, string

# 生成随机数
# 返回值：生成随机数范围min<=int<=max，若参数中有一个不为int类型，则返回值为-1
def get_random_int(min, max):
    if type(min) == int and type(max) == int:
        return random.randint(min, max)
    else:
        return -1

def get_random_lower_char():
    return chr(random.randint(97, 122))

def get_random_upper_char():
    return chr(random.randint(97, 122)).upper()

# 生成指定位数的整型随机数
def get_random_number(count):
    s = ''
    for i in range(count):
        num = get_random_int(0, 9)
        s += str(num)
    return s

# 生成指定数量的a-z的随机数
def get_random_lower_string(count):
    s = ''
    for i in range(count):
        s += chr(random.randint(97, 122))
    return s

# 生成指定数量的A-Z的随机数
def get_random_upper_string(count):
    s = get_random_lower_string(count)
    return s.upper()

# 生成给一个指定长度的包含字母和数字的随机字符串
def get_random_string(count):
    salt = ''.join(random.sample(string.ascii_letters + string.digits, count))
    return salt