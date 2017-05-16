import csv,datetime

csvfile_src = open("SRC.csv",'w')
writer_src = csv.writer(csvfile_src)
writer_src.writerow([' 出现次数',' 连续组数'])
csvfile_src.close()

csvfile_dst = open("DST.csv",'w')
writer_dst = csv.writer(csvfile_dst)
writer_dst.writerow([' 出现次数',' 连续组数'])
csvfile_dst.close()

#画3d图所需数据

a = []
for i in range(64):
    row = [0]*64
    a += [row]

#初始化
    
src_count = 1
src_equal_appear_times = 0
src_equal_total_times = 0

dst_count = 1
dst_equal_appear_times = 0
dst_equal_total_times = 0

total_times = 1

"""打开文件,这里总结下文件的读写：
1.读写前应打开，使用完后应关闭
2.open 函数:file = open(filename,accessmode(存取模式） = 'r',buffering= -1)存取模式默认是read（只读）
3.常见的存取模式：（1）r 以读的方式打开一个文本文件（文件必须已经存在） （2）w 以写的方式打开一个文本文件（若原来不存在文件，
则新建文件，若存在，写入时会覆盖原文件
（3）a 以追加写入的方式打开一个文本文件，打开时文件指针移到文件末尾
（4） r+ 以读写的方式打开一个文本文件 （5）w+ 以读写的方式新建一个文本文件
(6) a+ 以追加读写的方式打开一个文本文件 以上六种还可以加上b，如 'rb',操作二进制文件
（7）不可读的打开方式w和a，若不存在会创建新文件的打开方式：a，a+，w，w+ """



"""另一种读写文件的方式：
with open(path) as file:
    data = file.read()
"""
file = open("D:/shujuchuli5.txt")#写入文件path




#可以选择正则表达式

line = file.readline()


index_src = line.find("SRC:")
index_dst = line.find("DST:")
index_adr = line.find("ADR:")
index_typ = line.find("TYP:")


src = int("".join(list(line)[index_src + 4:index_src + 6]))
dst = int("".join(list(line)[index_dst + 4:index_dst + 6]))

src_adr = "".join(list(line)[index_adr + 4:index_adr + 14])
src_typ = "".join(list(line)[index_typ + 4:index_typ + 20])


a[src][dst] += 1


dst_adr = src_adr
dst_typ = src_typ


line = file.readline()


t1 = datetime.datetime.now()
#循环

while line :
    total_times += 1
    index_src = line.find("SRC:")
    index_adr = line.find("ADR:")
    index_typ = line.find("TYP:")
    index_dst = line.find("DST:")
    num_src = int("".join(list(line)[index_src + 4:index_src + 6]))
    num_dst = int("".join(list(line)[index_dst + 4:index_dst + 6]))
    con_adr = "".join(list(line)[index_adr + 4:index_adr + 14])
    con_typ = "".join(list(line)[index_typ + 4:index_typ + 20])

    a[num_src][num_dst] += 1

    if num_src == src and con_adr == src_adr and con_typ == src_typ:
        src_count += 1
    else:
        if src_count != 1:
            src_equal_total_times += src_count
            src_equal_appear_times += 1
            src_data = [src_equal_appear_times,src_count]
            csvfile_src = open("SRC.csv",'a+')
            writer_src = csv.writer(csvfile_src)
            writer_src.writerow(src_data)
            csvfile_src.close()
            
            
            
        src = num_src
        src_adr = con_adr
        src_typ = con_typ
        src_count = 1

    if num_dst == dst and con_adr == dst_adr and con_typ == dst_typ:
        dst_count += 1
    else:
        if dst_count != 1:
            dst_equal_total_times += dst_count
            dst_equal_appear_times += 1
            dst_data = [dst_equal_appear_times,dst_count]
            csvfile_dst = open("DST.csv",'a+')
            writer_dst = csv.writer(csvfile_dst)
            writer_dst.writerow(dst_data)
            csvfile_dst.close()
            
            

        dst = num_dst
        dst_adr = con_adr
        dst_typ = con_typ
        dst_count = 1
    line = file.readline()
    if not line :
        if dst_count != 1:
            dst_equal_appear_times += 1
            dst_equal_total_times += 1
        if src_count != 1:
            src_equal_appear_times += 1
            src_equal_total_times += 1

t2 = datetime.datetime.now()
print("程序运行时间: ",(t2-t1).seconds)
print("total_times: ",total_times,"dst_equal_total_times: ",dst_equal_total_times,"src_equal_total_times: ",src_equal_total_times)
print("dst_equal_appear_times: ",dst_equal_appear_times,"src_equal_appear_times: ",src_equal_appear_times)




#做饼状图，利用matplotlib            
import matplotlib.pyplot as plt

labels1 = ["SRC_equal_total_numbers","Total_times"]
labels2 = ["DST_equal_total_numbers","Total_times"]
sizes1 = [100*src_equal_total_times/total_times,100-100*src_equal_total_times/total_times]
sizes2 = [ 100*dst_equal_total_times/total_times ,100-100*dst_equal_total_times/total_times]
explode = [0.8,0]
fig1,ax1 = plt.subplots()
ax1.pie(sizes1,explode=explode,autopct='%1.4f%%',labels=labels1,shadow=True,center = (0,1),radius=0.8)
ax1.pie(sizes2,explode=explode,autopct="%1.4f%%",labels=labels2,shadow=True,center = (0,-1),radius=0.8)
ax1.axis('equal')

plt.show()

#做3d图....这一部分是照葫芦画瓢，很多原理都不太懂。。。学长如果有兴趣了解这个的话，有空可以给我讲下。。。

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
x,y = np.random.rand(2,100)*10
hist,xedges,yedges = np.histogram2d(x,y,bins=64,range=[[0,63],[0,63]])

xpos,ypos = np.meshgrid(xedges[:-1],yedges[:-1])
xpos = xpos.flatten('F')
ypos = ypos.flatten('F')
zpos = np.zeros_like(xpos)

dx = 0.5*np.ones_like(zpos)
dy = dx.copy()
dz = np.array(a).flatten()
ax.bar3d(xpos,ypos,zpos,dx,dy,dz,color='b',zsort='average')

plt.show()






"""写入csv文件中："""


