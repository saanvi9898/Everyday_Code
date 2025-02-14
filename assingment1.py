# q1
print("Hello, Python!!")
print("Welcome to Python Programming")

# Q2
number=1
print(number, "=>",type(int(number)))
f=2.5
print(f,"=>",type(f))
name="shanvi"
print(name, "=>",type(name))
l=["kavita", 2, 2.4, 6+6j,"meera"]
print(l,"=>",type(l))
b=True
print(b,"=>",type(b))

# Q3
user_name=input("What is your good name?")
user_age=input("how old are you?")
print('Username:',user_name, "And Age:",int(user_age))

# Q4
# integer
# input_num=input("")
num=3
''' String
 s=Hello Pyhon'''
if type(num) is int :
    print("it is numeric number")
elif type(num) is float:
    print("it's floating number!")
else:
    print("it is text")

# Q5
# string literals
s='hello'
s1="hello python"
s2="""hello
 python!"""
print(type(s),s)
print(type(s1),s1)
print(type(s2),s2)
#numeric literals
# integer
num=1
#float
f=3.5
#complex
c=3+3j
print(type(num),num)
print(type(f),f)
print(type(c),c)

#boolean
a=False
b=True
special=None
print(type(a), a)
print(type(b), b)
print(type(special), special)