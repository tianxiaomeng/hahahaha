
import csv,datetime
csvfile = open("SRC.csv",'w')
writer = csv.writer(csvfile)
writer.writerow([' 出现次数',' 连续组数'])
csvfile.close()
a = []
for i in range(64):
    row = [0]*64
    a += [row]
count = 1
src_times = 0
total_times = 1
times = 0
file = open("D:/shujuchuli4.txt")

line = file.readline()
index_src = line.find("SRC:")
index_dst = line.find("DST:")
index_adr = line.find("ADR:")
index_typ = line.find("TYP:")
num = int("".join(list(line)[index_src + 4:index_src + 6]))
adr = "".join(list(line)[index_adr + 4:index_adr + 14])
typ = "".join(list(line)[index_typ + 4:index_typ + 20])
dst = int("".join(list(line)[index_dst + 4:index_dst + 6]))
a[num][dst] += 1
line = file.readline()

starttime = datetime.datetime.now()



while line :
    total_times += 1
    index_src = line.find("SRC:")
    index_adr = line.find("ADR:")
    index_typ = line.find("TYP:")
    index_dst = line.find("DST:")
    num_src = int("".join(list(line)[index_src + 4:index_src + 6]))
    num_adr = "".join(list(line)[index_adr + 4:index_adr + 14])
    num_typ = "".join(list(line)[index_typ + 4:index_typ + 20])
    num_dst = int("".join(list(line)[index_dst + 4:index_dst + 6]))
    a[num_src][num_dst] += 1
    if num_src == num and num_adr == adr and num_typ == typ:
        count += 1
    else:
        if count != 1:
            src_times += count
            times += 1
            
            data = [times,count]
            csvfile = open("SRC.csv",'a+')
            writer = csv.writer(csvfile)
            writer.writerow(data)
            csvfile.close()
            
            
        num = num_src
        adr = num_adr
        typ = num_typ
        count = 1
    line = file.readline()
    if not line and count != 1:
        times += 1
        src_times += 1
        
    




dst_times = 0
total_times = 1
count = 1
times = 0
file = open("D:/shujuchuli4.txt")

line = file.readline()
index_dst = line.find("DST:")
index_adr = line.find("ADR:")
index_typ = line.find("TYP:")
num = "".join(list(line)[index_dst + 4:index_dst + 6])
adr = "".join(list(line)[index_adr + 4:index_adr + 14])
typ = "".join(list(line)[index_typ + 4:index_typ + 20])
line = file.readline()
while line :
    total_times += 1
    index_adr = line.find("ADR:")
    index_typ = line.find("TYP:")
    index_dst = line.find("DST:")
    num_dst = "".join(list(line)[index_dst + 4:index_dst + 6])
    num_adr = "".join(list(line)[index_adr + 4:index_adr + 14])
    num_typ = "".join(list(line)[index_typ + 4:index_typ + 20])
    if num_dst == num and num_adr == adr and num_typ == typ:
        count += 1
    else:
        if count != 1:
            dst_times += count
            times += 1
            
           
        num = num_dst
        adr = num_adr
        typ = num_typ
        count = 1
    line = file.readline()
    
    



endtime = datetime.datetime.now()
print(endtime-starttime)


import matplotlib.pyplot as plt

labels1 = "equal total SRC numbers","trace total numbers"
labels2 = 'equal total DST numbers','trace total numbers'
sizes1 = [ 100*src_times/total_times ,100-100*src_times/total_times]
sizes2 = [ 100*dst_times/total_times ,100-100*src_times/total_times]

explode = (0.8,0)

fig1,ax1 = plt.subplots()
ax1.pie(sizes1,explode=explode,autopct='%1.4f%%',labels=labels1,shadow=True,center = (0, 1),radius=0.8)
ax1.pie(sizes2,explode=explode,autopct='%1.4f%%',labels=labels2,shadow=True,center = (0,-1),radius=0.8)
ax1.axis('equal')

plt.show()
"""0:05:03.318349"""

