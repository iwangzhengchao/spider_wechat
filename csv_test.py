#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/1/18 20:13
# @Author  : Z.C.Wang
# @Email   : iwangzhengchao@gmail.com
# @File    : csv_test.py
# @Software: PyCharm Community Edition
"""
Description :

"""
import csv
import jieba
import operator
import pickle
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as col
import matplotlib.cm as cm

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
# print("Full Mode: " + "/ ".join(seg_list))  # 全模式
#
# seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
# print("Default Mode: " + "/ ".join(seg_list))  # 精确模式
#
# seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
# print(", ".join(seg_list))
#
# seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
# print(", ".join(seg_list))

# x = ['北京', '北京', '北京', '', '山东', '浙江', '山东', '山东', '山东', '',
#      '陕西', '山东', '重庆', '北京', '山东', '', 'Styria', '山东', '山东', '',
#      '山东', '山东', '北京', '山东', '山东', '山东', '山东', '山东', '山东',
#      '山东', '山东', '', '山东', '山东', '', '山东', '湖北', '甘肃', '河北',
#      '北京', '宁夏', '北京', '北京', '', '北京', '', '', 'Firenze', '山东',
#      '', '北京', '山东', '山东', '', '上海', '天津', '', '', '山东', '北京',
#      '江苏', '山东', '山东', '甘肃', '山东', '', '北京', '北京', '北京', '北京',
#      '安徽', '山东', '', '山东', '山东', '山东', '', '', '山东', 'Barcelona',
#      '福建', '上海', '湖南', 'Geneve', '北京', '山西', '河南', '山西', '安徽',
#      '北京', '', '山东', '河北', '山东', '', '北京', '山东', '北京', '山东', '北京',
#      '北京', '北京', '北京', '北京', '山东', '河北', '北京', '山东', '', '山东', '',
#      '广东', '北京', '江苏', '山东', '', '北京', '山东', '北京', '北京', '北京',
#      'Bergamo', '北京', '山东', '', '陕西', '', '', '山东', '浙江', '山东', '山东',
#      '山东', '北京', '', '山东', 'Northern Territory', '江苏', '北京', 'Viedma',
#      '山东', '北京', '山东', '山东', '新疆', '山东', '北京', '河北', '北京', '山东',
#      '山东', '', '北京', '山东', '山东', '浙江', '福建', 'Vienna', '', '', '北京',
#      '吉林', '山东', '山东', '', '', '山东', '山东', '广东', '青海', '北京', '四川',
#      '山东', '北京', 'Coloane', '重庆', '北京', '山东', '河南', '河北', '山东',
#      '山东', '河北', '河北', '浙江', 'Ohio', '北京', '', 'Auckland', '山东',
#      '江苏', 'Male Atoll', '山东', '山东', '安徽', 'Madrid', '山东', '',
#      '山东', '', '北京', '山东', '山东', '山东', '河北', '河南', 'Dubayy',
#      '山东', '', '北京', '江苏', '', '北京', '江苏', '山东', '北京', '北京',
#      '山东', '北京', '北京', '']

proList = ['青海', '新疆', '山西', '重庆', '江苏', '安徽', '山东', '浙江', '四川', '天津', '河北',
           '广东', '湖南', '陕西', '上海', '北京', '河南', '吉林', '甘肃', '福建', '宁夏', '湖北', '']
# dic = {}
# for i in proList:
#     dic[i] = 0
# for i in x:
#     if i in dic.keys():
#         dic[i] += 1
#     else:
#         dic['其他'] += 1
# count = []
# for i in proList:
#     count.append(dic[i])
# dic = sorted(dic.items(), key=operator.itemgetter(1))
L = ['青海', '新疆', '四川', '天津', '湖南', '吉林', '宁夏', '湖北', '山西', '重庆', '广东', '陕西', '上海', '甘肃', '福建', '安徽', '河南', '浙江', '江苏', '河北', '北京', '其他', '山东']
C = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 4, 6, 8, 49, 51, 75]
x = range(len(C))
cmap = cm.ScalarMappable(col.Normalize(min(C), max(C), cm.hot))
plt.barh(x, C, align='center', alpha=0.5, color=cmap.to_rgba(C))
plt.xlabel('Count', fontsize=12)
plt.ylabel('Province', fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.yticks(x, L)
plt.show()
data = pickle.load(open('data.txt', 'rb'))
# print(data)
count_male = []
count_female = []
province = data['Province']
sex = data['Sex']
for pro in proList:
    male = 0; female = 0
    for i in range(len(province)):
        if pro == province[i]:
            if sex[i] == 1:
                male += 1
            elif sex[i] == 2:
                female += 1
    count_male.append(male)
    count_female.append(female)
plt.bar(proList, count_male, color='lightblue', label='male')
plt.bar(proList, count_female, bottom=count_male, color='blue', label='female')
plt.xlabel('Count', fontsize=15)
plt.ylabel('Province', fontsize=15)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.show()
