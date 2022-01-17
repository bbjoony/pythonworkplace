import re, io

f = io.open('friends101.txt','r')
sentences = f.readlines()
would = [i for i in sentences if re.match(r'[A-Za-z]+:', i) and re.search('would', i)]

# print(would)

newf = io.open('would.txt', 'w')
newf.writelines(would)
newf.close()