#Create a string "hello" and convert it to uppercase using a string method.
s="hello"
print(s.uppercase)
#Given "PYTHON", convert it to lowercase using a string method.
s="PYTHON"
print(s.lowercase)
#From "hello world, replace "world" with "python"using a string method.
s="hello world"
print(s.replace("world","python"))
#Extract "ell" from "hello"using slicing only.
a="hello"
print(a[1:4])
#Reverse the string "python"using slicing (no loops).
a="python"
print(a.[::-1])
#Combine "hello" and "world"into one string using string operations.
a="hello"
b="world"
print(a+ "" +b)
#Repeat the string "hi" to get "hihihi"using string operations.
a="hi"
print(a*3)
#Check if "cat"exists in "concatenate"using a string operator.
s="concatenate"
print("cat in concatenate")
#Count how many times "a"appears in "banana"using a string method.
s="banana"
print(s.count("a"))
#Remove leading and trailing spaces from " hello "using a string method.
s="hello"
print(s.strip())
#Find the index of "o" in "hello" using a string method.
s="hello"
print(s.index("o"))
#Split the string "a,b,c,d"into a list using a string method.
s="a,b,c,d"
print(s.split(","))
#Join the list ["a","b","c"]into "abc"using a string method.
s=["a","b","c","d"]
print("".join(s))
#Extract every 2nd character from "abcdef"using slicing → expected "ace".
s="abcdef"
print(s[::2])
#Replace all "a"with "@"in "banana"using a string method.
s="banana"
print(s.replace("a","@"))
#Check if "hello123" is alphanumeric using a string method.
s="hello123"
print(s.isalnum())
#Capitalize the first letter of "python"using a string method.
s="python"
print(s.capitalize())
#Convert "hello world"into "Hello World" using a string method.
s="hello world"
print(s.title())
#Remove all vowels from "python"using string operations (no loops ifpossible 😈).
s="python"
print(s.replace("o",""))
#Check if "madam"is a palindrome using slicing
s="madam"
print(s==s[::-1])