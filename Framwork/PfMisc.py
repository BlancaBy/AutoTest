#coding=utf-8

# 计算列表中元素出现的次数，并返回为一个字典
def count_element_in_list(list):
    dict = {}
    for i in list:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict

# 判断两个列表是否完全相等
def compare_lists(l1, l2):
    result = len(l1) == len(l2)
    for i in range(len(l1)):
        result = result and (l1[i] in l2)
    return result