#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/1/18 16:30
# @Author  : Z.C.Wang
# @Email   : iwangzhengchao@gmail.com
# @File    : cihuiyun.py
# @Software: PyCharm Community Edition
"""
Description :

"""
from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = '''
If the implementation 想你 is hard to explain, it's a bad idea. 想你了
If 成都 implementation is 想你 easy to explain, it may be a good idea.
Namespaces are 端午one 端午 honking great idea -- 成都 
深圳 晚安 深圳 新媒体
'''

# the font from github: https://github.com/adobe-fonts
font = r'C:\Windows\Fonts\simhei.ttf'
wc = WordCloud(background_color='white', font_path=font,
               width=1000, height=1000, margin=2).generate(text)

plt.imshow(wc)
plt.axis("off")
plt.show()
