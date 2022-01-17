python = "Python is Amazing"
print(python.lower())   
print(python.upper())   
print(python[0].isupper()) # 파이썬 문자열의 첫 글자가 대문자인지 확인 
print(len(python))  
print(python.replace("Python", "Java")) 

index = python.index("n")
print(index)    
index = python.index("n", index + 1)
print(index)    

print(python.find("n"))
print(python.find("Java"))
print(python.count("n"))