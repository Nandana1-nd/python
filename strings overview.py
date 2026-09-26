#string slicing
a="Hello,World"
print(a[0:12])
print(a[0:5])
print(a[6:12])
print(a[0:12:3])
print(a[::-1])
#Modifying Strings
s="Hello,World"
new_s=s.replace("World","Python")
print(new_s)
print(s)
print(s.upper())
print(s.lower())
#String concatenation
s1="Hello"
s2="Beauty"
print(s1+","+s2)
a=["Python","is","awesome" ]
print(" ".join(a))
#f- String
name="Ardra"
age=21
print(f"my name is {name},and iam {age} years old") 
#Escape Characters
print("hello\nWorld")
#Inserting a tab
print("Hello\tWorld")
#Using quotes
print('He said,"Python is amazing!"')
#String methods
#len()
s="Hello, World!"
print(len(s))
#strip
s="Hello, World!"
print(s.strip())
#split
s="Hello, World!"
print(s.split(","))
#find
s="Hello, World!"
print(s.find("Hello"))
#count
s="Hello, World, World!"
print(s.count("World"))
#startswith() and endswith()
s="Hello, World!"
print(s.startswith("Hello"))
print(s.endswith("World!"))
#creating a list
a=[1,2,3,4.5]
print(a)
#Accessing List
my_list=['apple','orange','cherry']
print(my_list[1])
print(my_list[-2])
#Range of Index
my_list=[1,2,3,4,5]
print(my_list[1:4])
#changing list items
a=['apple','banana','cherry']
a[1]='mango'
print(a)
#changing multiple items
a=[1,2,3,4,5]
a[1:4]='a','b','c'
print(a)
#Adding items to a List
#append
s=['apple','banana']
s.append('cherry')
print(s)
#insert
s=['apple','banana']
s.insert(1,'cherry')
print(s)
#extend
s=['apple','banana']
new=['cherry','orange']
s.extend(new)
print(s)
#Removing items from a list
#remove
a=['apple','banana','cherry']
a.remove('banana')
print(a)
#pop
a=['apple','banana','cherry']
popped_item=a.pop(1)
print(a)
#del
a=['apple','banana','cherry']
del a[0]
print(a)
#clear
a=['apple','banana','cherry']
a.clear()
print(a)
#list methods
#count
a=[1,2,3,2,4]
print(a.count(2))
#Index
s=['apple','banana','cherry']
print(s.index('banana'))
#reverse
a=[1,2,3]
a.reverse()
print(a)
#Sort
s=[3,1,2]
s.sort()
print(s)
#Copy
og=[1,2,3]
copy=og.copy()
print(copy)
#sorting a list
#sorted
original=[3,1,4]
a=sorted(original)
print(a)
#Joining lists
a1=['apple','banana']
a2=['cherry','orange']
combined_list=a1+a2
print(combined_list)
#using extend
list1=['apple','banana']
list2=['cherry','orange']
list1.extend(list2)
print(list1)