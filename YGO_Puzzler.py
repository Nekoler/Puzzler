import re
import os
from PIL import Image

def get():
    for i in os.listdir():
        if 'ydk' in i:
            res = open(i).read()
            break
    return re.findall(r'\d{3,}',res)
#将ydk处理为列表
def check(res):
    pic = os.listdir('pic')
    lack = [i for i in res if not i+'.png' in pic]
    if bool(lack):
        for i in lack:
            print(i)
        exit()
    return res
#检查是否缺少卡图
def add(res):
    if len(res)%9 != 0:
        res.extend((9-len(res)%9)*['temp'])
    return res
#将卡的数量处理为9的倍数
def puzzle(cards,name,posi):
    res = Image.new('RGBA',(2115,3069),(255,255,255))
    for i1,i2 in zip(cards,posi):
        if i1 == 'temp':
            card = Image.new('RGB',(697,1015),(255,255,255))
        else:
            card = Image.open('pic/%s.png'%i1).resize((697,1015))
        res.paste(card,i2)
    res.save('%d.png'%name)
#将9张图拼成1张
def start(res,posi):
    for i in range(len(res)//9):
        puzzle(res[0:9],i,posi)
        del res[0:9]
#启动拼图
position = ((0,0),(709,0),(1418,0),(0,1027),(709,1027),(1418,1027),(0,2054),(709,2054),(1418,2054))
#卡图的位置
start(add(check(get())),position)
