import re, usecsv

total = usecsv.opencsv('popSeoul.csv')
   
for i in total:
    for j in i:    
        try:
            i[i.index(j)] = float(re.sub(',','', j))
        except:
            pass

print(total)