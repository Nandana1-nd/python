#Creating a Tuple
s=(1,2,3,'Python',4.5)
print(s)
#Single item Tuple
s=(5,)
print(type(s))
#accessing tuple items
a=('apple','banana','cherry')
print(a[1])
#slicing tuples
a=(10,20,30,40,50)
print(a[1:4])
#Updating
#Reassigning a Tuple
a=(1,2,3)
a=(4,5,6)
print(a)
#Convert Tuple to List
a=('apple','banana','cherry')
t=list(a)
t[1]='orange'
a=tuple(t)
print(a)
#unpacking tuples
a=('apple','banana','cherry')
(fruit1,fruit2,fruit3)=a
print(fruit1)
print(fruit2)
print(fruit3)
#using*(asterisk)
a=(1,2,3,4,5)
(first,*middle,last)=a
print(first)
print(middle)
print(last)
#Joining tuples
t1=(1,2,3)
t2=(4,5,6)
a=t1+t2
print(a)
#tuple methods
#count
a=(1,2,3,2,2,4)
print(a.count(2))
#index
a=('apple','banana','cherry')
print(a.index('banana'))
