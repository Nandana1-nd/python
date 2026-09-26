#creating a set
#using curly braces
set1={1,2,3,4}
print(set1)
#using set()function
another_set=set([5,6,7])
print(another_set)
#Empty set
empty_set=set()
print(type(empty_set))
#Accessing set items
my_set={1,2,3}
print(2 in my_set)
print(5 in my_set)
#Adding items to a set
#Adding a single item
my_set={1,2,3}
my_set.add(4)
print(my_set)
#Adding multiple items
my_set={1,2,3,4}
my_set.update([4,5,6])
print(my_set)
#Removing items from a set
#remove()
my_set={1,2,3,4}
my_set.remove(2)
print(my_set)
#discard()
my_set={1,2,3,4}
my_set.discard(5)
print(my_set)
#pop()
my_set={1,2,3,4}
removed_item=my_set.pop()
print(removed_item)
#clear()
my_set={1,2,3,4}
my_set.clear()
print(my_set)
#Joining sets
#union()
set1={1,2,3}
set2={3,4,5}
result=set1.union(set2)
print(result)
#update()
set1={1,2,3}
set2={4,5,6}
set1.update(set2)
print(set1)
#set intersection
set1={1,2,3}
set2={2,3,4}
result=set1&set2
print(result)
#set differece
set1={1,2,3}
set2={2,3,4}
result=set1-set2

