import os, re
import usecsv

os.chdir(r'/Users/devsiters')
total = usecsv.opencsv('popSeoul.csv')

newPop = usecsv.switch(total)
new = [['구 이름', '한국인(명)', '외국인(명)', '외국인 비율(%)']]

for i in newPop:
    foreign = 0
    try:
        foreign = round(i[2]/(i[1]+i[2]) *100, 1)
        if foreign > 3:
            new.append([i[0], i[1], i[2], foreign])
    except:
        pass

usecsv.writecsv('newPop.csv', new)