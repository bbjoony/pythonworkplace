import re, os
import usecsv   

os.chdir(r'/Users/devsiters')
apt = usecsv.switch(usecsv.opencsv('apt_202201.csv')) # 파일을 불러와서 Switch로 변환

new_list = []

for i in apt:
    try:
        if re.search('마장동', i[0]): 
            new_list.append([i[0], i[4], i[8], i[9]]) # 시군구, 아파트 단지명, 평수, 거래가만 출력
    except:
        pass

print(new_list)
usecsv.writecsv('majang_apt.csv', new_list)