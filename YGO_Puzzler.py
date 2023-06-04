import re
import os
from PIL import Image
from multiprocessing import Process

def get():
    for i in os.listdir():
        if 'ydk' in i:
            ydk = open(i).read()
            break
    return re.findall(r'\d{3,}',ydk)
#将ydk处理为列表
def check(ydk):
    pic = os.listdir('pic')
    lack = [i for i in ydk if not '%s.png'%i in pic]
    if bool(lack):
        print('缺少卡图')
        for i in set(lack):
            print(i)
        exit()
    return ydk
#检查是否缺少卡图
def add(ydk):
    if len(ydk)%9 != 0:
        ydk.extend((9-len(ydk)%9)*['temp'])
    return ydk
#将卡的数量处理为9的倍数
def puzzle(nine,name,box):
    res = Image.new('RGBA',(4228,6139),(255,255,255))
    for i1,i2 in zip(nine,box):
        if i1 == 'temp':
            card = Image.new('RGBA',(1394,2031),(255,255,255))
        else:
            card = Image.open('pic/%s.png'%i1)
        res.paste(card,i2)
    res.save('%d.png'%name)
#将9张图拼成1张
def start(ydk,box):
    num = len(ydk)//9
    for i in range(num):
        Process(target=puzzle,args=(ydk[0:9],i,box)).start()
        del ydk[0:9]
#启动拼图
def box():
    x = (0,1417,2834)
    y = (0,2054,4108)
    res = [(i1,i2) for i1 in x for i2 in y]
    return res
#卡图的位置

start(add(check(get())),box())
