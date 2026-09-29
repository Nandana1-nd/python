#read()
a=open("sample.txt","r")
print(a.read())
a.close()

#readline()
a=open("sample.txt","r")
line1=a.readline()
print(line1)
a.close()

#readlines()
a=open("sample.txt","r")
lines=a.readlines()
print(lines)
a.close()

#write()
a=open("sample.txt","w")
a.write("Hello,World!")
a.close()

##writelines()
a=open("sample.txt","w")
lines=