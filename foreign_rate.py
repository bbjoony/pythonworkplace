import os, re
import usecsv # Customized module

os.chdir(r'/Users/devsiters')
total = usecsv.opencsv('popSeoul.csv') # opencsv('filename')

newPop = usecsv.switch(total)   # 읽어온 CSV 파일을 newPop으로 스위치(실수형으로 변환하고 쉼표 제거)
new = [['구 이름', '한국인 수', '외국인 수', '외국인 비율(%)']] # 4개 항목으로 구성된 새로운 리스트 'new' 생성

for i in newPop:
    foreign = 0 # 'foreign' 이라는 변수 초기화
    try:
        foreign = round(i[2] / (i[1]+i[2]) * 100, 1) 
        # 한국인 + 외국인을 합해 외국인 수로 나눔 X 100 = 'foreign' 이라는 변수로 계산 -> 소수점 1자리로 반올림(round)
        if foreign > 3:
            new.append([i[0], i[1], i[2], foreign]) 
            #'foreign'이 3을 초과하면 new 리스트에 해당하는 구 이름, 한국인 수, 외국인 수, 위에서 구한 외국인 비율을 기록함
    except:
        pass
    
usecsv.writecsv('newPop.csv', new)