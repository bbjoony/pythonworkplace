import csv, io, os

def writecsv(filename, the_list): # 첫 번째 변수는 만들 파일 이름, 두 번째 변수는 CSV형 리스트를 저장할 객체 이름
    with open(filename, 'w', newline = '') as f:
        a = csv.writer(f, delimiter = ',')
        a.writerows(the_list)