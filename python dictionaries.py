#Creating a dictionary
#using curly braces
my_dict={"name":"John","age":30,"city":"New York"}
#Using the dict()constructor
another_dict=dict(name="Alice",age=25,city="Los Angeles")
print(my_dict)
print(another_dict)
#Empty Dictionary
empty_dict={}
print(empty_dict)
#Accessing Dictionary Items
#Accessing with Brackets
my_dict={"name":"John","age":30}
print(my_dict["name"])
#Using get()
print(my_dict.get("age"))
print(my_dict.get("salary"))
#Changing Dictionary Items
my_dict={"name":"John","age":30}
my_dict["age"]=31
print(my_dict)
my_dict["city"]="New York"
print(my_dict)
#Adding Items to a Dictionary
my_dict={"name":"John","age":30}
my_dict["city"]="New York"
print(my_dict)
#Removing Items from a Dictionary
#pop(key)
my_dict={"name":"John","age":30,"city":"New York"}
age=my_dict.pop("age")
print(age)
print(my_dict)
#popitem()
my_dict={"name":"John","age":30}
last_item=my_dict.popitem()
print(last_item)
#del statement
my_dict={"name":"John","age":30}
del my_dict["age"]
print(my_dict)
#clear()
my_dict.clear()
print(my_dict)
#Copying a Dictionary
#using copy()
original={"name":"John","age":30}
copy_dict=original.copy()
print(copy_dict)
#using dict()constructor
original={"name":"John","age":30}
copy_dict=dict(original)
print(copy_dict)
#Nested Dictionaries
nested_dict={
    "person1":{"name":"John","age":30},
    "person2":{"name":"Alice","age":25}
}
print(nested_dict["person1"]["name"])
#Dictionary method
#keys()
my_dict={"name":"John","age":30}
print(my_dict.keys())
#values()
print(my_dict.values())
#items()
print(my_dict.items())
#update()
my_dict={"name":"John","age":30}
my_dict.update({"city":"New York"})
print(my_dict)
#fromkeys()
keys=["name","age","city"]
new_dict=dict.fromkeys(keys,"Unknown")
print(new_dict)
#setdefault(key,value)
my_dict={"name":"John","age":30}
city=my_dict.setdefault("city","New York")
print(city)
print(my_dict)




