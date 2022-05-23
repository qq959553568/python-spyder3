# -*- coding = utf-8 -*-
# @Time : 2022/3/31 20:18
# @Author : DYT
# @File : testCloud.py
# @Software: PyCharm

import jieba
from matplotlib import  pyplot as plt
from wordcloud import WordCloud
from PIL import Image
import numpy as np
import sqlite3

con = sqlite3.connect('movie.db')
cur = con.cursor()
sql = 'select instroduction from movie250'
data = cur.execute(sql)
text = ""
for item in data:
    text = text +item[0]
    #print(item[0])
#print(text)
cur.close()
con.close()

cut = jieba.cut(text)
string = ' '.join(cut)
print(len(string))

img = Image.open(r'.\static\assets\images\1.jpg')
img_array = np.array(img)
wc =WordCloud(
    background_color='white',
    mask = img_array,
    font_path="msyh.ttc",
)
wc.generate_from_text(string)

#绘制图片
fig = plt.figure(1)
plt.imshow(wc)
plt.axis('off')  #是否显示坐标轴

#plt.show() #显示生成的词云图片
plt.savefig(r'.\static\assets\images\word.png',dpi=500)