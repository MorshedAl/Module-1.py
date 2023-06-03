

#variable
x=5
y="Abdullah"
print(x)
print(y)

#same var but d_type value initialize

x=100
x="Bangladesh"
print(x) # Bangladesh

#data_type casting

x1=str(5)
x2=str(7)
print(x1+x2) #string concatenate 57

y1=int(5)
y2=int(7)
print(y1+y2) #int sum 12

z=float(5)
print(z) # 5.0


#data_type:

x="Bangladesh"
y=50
print(type(x)) #str
print(type(y)) #int


#syntex

if 10>50:
    print("10 bigger than 5" )
    print("hahahahaha")
if 5>2:
 print("5 greater than 2")
 print("5 greater than 2")

else:
 print("smaller")


 """
camel case:  myVariableNname
pascal case: MyVariableName
snake case : my_variable_name



variable not allowed:

. 5myvar
. my-var
. my var

"""


#assign multiple var & values in one_line
 
x,y,z="mango","banana","orange"
print(x)
print(y)
print(z)

x=y=z="rupok"
print(x)
print(y)
print(z)

# unpacking 

fruits=["mango","banana","orange"]
x,y,z=fruits
print(x)
print(y)
print(z)

fruits=["mango","banana","cherry"]
green,yellow,red=fruits 
print(red)
print(green)
print(yellow)


letters=['m','n','o','x','y','z']

abbo,mabbo,*pappo=letters
print(abbo)
print(mabbo)
print(pappo)

abbo,*mabbo,pappo=letters
print(abbo)
print(mabbo)
print(pappo)


*abbo,mabbo,pappo=letters
print(*abbo)
print(mabbo)
print(pappo)



# output variable 
x="awesome"
print("python is "+x)



x="python is "
y="awesome"
z=x+y
print(z)


x=5
y=10
print(x+y)

"""
x=5
y="doller"
print(x+y)
 this is not allowed in python. 
"""

#Global variable 
#it create outside & inside of function 

#print inside function 
x=300
def function():
  print(x)
function()


# print outside of function 
x=300
def function():
 x=100
 print(x) # 100

function()
print(x) #300


#Global var declare inside function 

def func():
 global x
 x=500
func()
print(x)


x=77
def function():
 global x
 x=99

function()
print(x) # x 99










