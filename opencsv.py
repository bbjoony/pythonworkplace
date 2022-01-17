import csv, os, io

def opencsv(filename):
    f = open(filename, 'r', encoding='cp949') 
    reader = csv.reader(f)
    output = []
    for i in reader:
        output.append(i)    
    return output

opencsv('a.csv')

