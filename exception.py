2#python exceptions

#Zero division error
# a=10
# b=0
# print(a/b)

#Type error
#a="hi"
#b=5
#print(a+b)

#value error
#age=int("hello")
#print(age)

#Index error
#numbers=[1,3,5]
#print(numbers[6])

#key error
#a={"name":"riya"}
#print(a["age"])

#file not found error
#file=open ("python.txt")



3#exception with try except
try:
    a=10
    b=0
    print(a/b) 
except ZeroDivisionError:
    print("you can't divide by zero")


4#using else and finally in exception
try:
    num=int(input("Enter a number:"))
    result=10/num
except ZeroDivisionError:
    print("division by zero is not allowed!")

else:
    print(f"The result is{result}")

finally:
    print("This will always be printed.")


