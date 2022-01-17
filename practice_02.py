import os, re, io

f = io.open('friends101.txt', 'r', encoding = 'utf8') # 'os' 대신 'io'를 import 해야 함
script01 = f.read()

print(re.findall(r'\([A-Za-z].+?[a-z|\.]\)', script01)[:6])