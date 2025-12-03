# function defining
# def function_name():
#   body of the function  

# function calling
# function_name()

#def say_hello():
#    print('Welcome to Kerala')
#    print("Where do you want to stay?")

def say_hello(name):
    print(f"Hello {name}, Welcome to Kerala")
    print("Where do you want to stay?")

def cube(n):
    return(n**3)

N=5
c=cube(N)
print(c)

#say_hello()
say_hello('Sandeep')

def product(x,y):
    product=x*y
    print(f"The Product of {x} and {y} is {product}")

product(5,10)

def greet(name,age,location):
    print(f"Hello {name}, You are {age} years old and You are from {location}")

greet('Asha',34,'Kollam')

#can we write function with same name with different argument?

def pos_or_negative(num):
    if num>0:
        print(f"{num} is a +ve number")
    elif num<0:
        print(f"{num} is a -ve number")
    else:
        print(f"{num} is zero")
pos_or_negative(-2)

#using return 
def total_Score(x,y,z):
    total=x+y+z
    print(f"Total Mark is {total}")
    return total

final_Score=total_Score(10,10,10)
if final_Score>40:
    print('Passed')
else:
    print('Failed')
# Types of Python Function Arguments
# Default args:
def greet(name,age,location="Kochi"):
    print(f"Hello {name}, You are {age} years old and You are from {location}")

greet('Asha',34,"Kollam")
# calling without third args:
greet('Asha',34)

# create a function ti calculate price of the product.
# tha arguments are price, quantity and tax 
# above 500 10% dicount else 5% discount

def total_Price(price,qty,tax=0.05):
    rate=price*qty
    tax_rate=rate*tax
    rate_Withtax=rate+tax_rate
    print(f"Toal ammount wittout discount {rate_Withtax}")
    return rate_Withtax

product_Price=total_Price(250,3)
if product_Price>500:
    discount=product_Price*.1
    product_Price=product_Price-discount
    print(f"{product_Price} with 10% discount")
else:
    discount=product_Price*.05
    product_Price=product_Price-discount
    print(f"{product_Price} with 5% discount")

# Keyword args

def calulate_score(math=50,english=50,science=50):
    total=math+english+science
    print(total)
    return total

calulate_score()
calulate_score(10,20)
calulate_score(10,20,30)
calulate_score(math=20,science=40)

# Arbitrary args (variable lenght args *arg and **kwargs)
# used when the input args count changes
# *args type will be tuple
def sum_of_numbers(*args):
    total=0
    print(type(args))
    for num in args:
        total=total+num
    return total
total=sum_of_numbers(5,6,7,9,10)
print(total)
total=sum_of_numbers(15,16,110)
print(total)
total=sum_of_numbers(15,16,110,21,12,32,35,56,76)
print(total)

# **kwargs type will be dictionary
def display_info(**kwargs):
    print(type(kwargs))
    # dictionary itration
    for key,val in kwargs.items():
        print(f"{key} : {val}")
    return

display_info(name="Deeps",age=40,location="Kochi")
display_info(name="Sam",age=40)
display_info(name="Sandeep",graduation="BCA",cgpa=4.3,year=2021)

# Library functions
import statistics as stats
def createStatSummary(data):
    print(type(data))
    # mean
    Mean_value = round(stats.mean(data))
    # median
    Median_value = stats.median(data) 
    # mode
    Mode_value = stats.mode(data)
    
    return Mean_value,Median_value,Mode_value

numbers=[10,20,30,23,34,45,12,21,32,54,66,53,67,54]
meanNew,medianNew,modeNew = createStatSummary(numbers)
print(f'Mean is {meanNew}, Median is {medianNew} and Mode is {modeNew}')

# Lambda Functions 
# single line execution

def square(x):
    sq=x*x
    return sq
op=square(4)
print(op)

square=lambda x:x*x

oplambda=square(5)
print(oplambda)

add = lambda x,y:x+y
opadd=add(10,13)
print(opadd)
is_pass = lambda marks: "pass" if marks>40 else "fail"

print(is_pass(50))

# map - function and iterative fucnctions 
numbers=[1,2,3,4,5]
double_number = map(lambda x:x*2,numbers)
print(list(double_number))

# substration of each element
list_a =[1,2,3]
list_b=[10,20,30]

final_list= map(lambda x,y:x-y,list_a,list_b)
print(list(final_list))
# o/p : [-9, -18, -27]

# find first char of each fruits
fruits=['Applel','Cherry','Grapes']
res = list(map(lambda x: x[0],fruits))
print(res)
# o/p : ['A', 'C', 'G']

