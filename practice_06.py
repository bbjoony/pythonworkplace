import re, os, usecsv

English = 'She is a vegeterian. She does not eat meat. She thinks that animals should not be killed.'
Korean = '그녀는 채식주의자입니다. 그녀는 고기를 먹지 않습니다. 그녀는 동물을 죽이지 말아야 한다고 생각합니다.' 

os.chdir(r'/Users/devsiters')

korean_list = re.split('\.', Korean)
English_list = re.split('\.', English)

total = []

for i in range(len(English_list)):
    total.append([English_list[i], korean_list[i]])
    
usecsv.writecsv('total.csv', total)