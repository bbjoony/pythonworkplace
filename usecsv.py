import csv, os, re

def opencsv(filename): # CSV 파일 읽어오기
    f = open(filename, 'r', encoding='cp949') 
    reader = csv.reader(f)
    output = []
    for i in reader:
        output.append(i)    
    return output

def writecsv(filename, the_list): # 첫 번째 변수는 만들 파일 이름, 두 번째 변수는 CSV형 리스트를 저장할 객체 이름
    with open(filename, 'w', newline = '') as f:
        a = csv.writer(f, delimiter = ',')
        a.writerows(the_list)

def switch(listname): # 리스트를 읽어서 쉼표를 제거하고 숫자를 실수형으로 변환하는 함수
    for i in listname:
        for j in i:    
            try:
                i[i.index(j)] = float(re.sub(',','', j))
            except:
                pass
    return listname