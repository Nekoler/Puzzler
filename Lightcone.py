from os import listdir
from PIL import Image
from multiprocessing import Process

def get():#获取光锥列表
    all = listdir('pic')
    if len(all)%9 != 0:
        all.extend((9-len(all)%9)*['temp'])
    return all

def box():#光锥的位置
    x = (0,915,1830)
    y = (0,1273,2546)
    return [(i1,i2)for i1 in x for i2 in y]

def puzzle(lcs,name,box):#拼图
    res = Image.new('RGBA',(2732,3806),(255,255,255,0))
    for i1,i2 in zip(lcs,box):
        if i1 == 'temp':
            lc = Image.new('RGBA',(902,1260),(255,255,255,0))
        else:
            lc = Image.open('pic/%s'%i1)
        res.paste(lc,i2)
    res.save('%d.png'%name)

def start(lcs,box):#多进程
    num = len(lcs)//9
    for i in range(num):
        Process(target=puzzle,args=(lcs[0:9],i,box)).start()
        del lcs[0:9]

if __name__ == '__main__':
    start(get(),box())