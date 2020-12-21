# write a python program to sort dictionary items
dict1 = {'car': [7, 6, 3],  
             'bike': [2, 10, 3],  
             'truck': [19, 4]}

print(f"The original dictionary is : {str(dict1)}") 

res = dict() 
for key in sorted(dict1): 
    res[key] = sorted(dict1[key])

print(f"The sorted dictionary : {str(res)}")

# write a program to display date and time
import datetime
now = datetime.datetime.now()
time= now.strftime("%Y-%m-%d %H:%M:%S")
print(f"Current date and time : {time}")

# write a program to return the absolute value
num = -10
print(f'Absolute of {num} is {abs(num)}')

# write a python program to check the length of list
sample_list = ['a','b','c']
print(f'length of sample_list is {len(sample_list)}')

# write a Python program to calculate number of days between two dates.
from datetime import date
f_date = date(2019, 4, 15) # YYYY/MM/DD
l_date = date(2020, 4, 15) # YYYY/MM/DD
delta = l_date - f_date
print(f'No of days between {f_date} and {l_date} is:{delta.days}')

# write a Python program to convert Python objects into JSON strings.
import json
python_dict =  {"name": "David", "age": 6, "class":"I"}
json_dict = json.dumps(python_dict, sort_keys=True, indent=4)
print(f"json dict : {json_dict}")

# write a Python program to get the largest number from a list
def max_num_in_list(list):
    max = list[0]
    for a in list:
        max = a if a > max else max
    return max
print(f'max_num_in_list [1, 10, -8, 0], Ans:{max_num_in_list([1, 10, -8, 0])}')

# write a Python program to remove duplicates from a list
a = [10,20,30,20,10,50,60,40,80,50,40]

dup_items = set()
uniq_items = []
for x in a:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)

print(f'dup_items:{dup_items}')

# write a Python program to flatten a shallow list
import itertools
original_list = [[2,4,3],[1,5,6], [9], [7,9,0], [1,2,3,4]]
new_merged_list = list(itertools.chain(*original_list))
print(f'merged list/flatten:{new_merged_list}')

# write a Python program to create multiple list

obj = {}
for i in range(1, 11):
    obj[str(i)] = []
print(f'create multiple list:{obj}')

# write a Python program to merge two dictionaries

d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}
d = d1.copy()
d.update(d2)
print(f'merge two dictionaries:{d}')

# write a Python program to Sum all the items in a dictionary

my_dict = {'data1':100,'data2':-54,'data3':247}
print(f'Sum all the items in a dictionary:{sum(my_dict.values())}')

# write a python program to Get the maximum and minimum value in a dictionary

my_dict = {'x':500, 'y':5874, 'z': 560}

key_max = max(my_dict.keys(), key=(lambda k: my_dict[k]))
key_min = min(my_dict.keys(), key=(lambda k: my_dict[k]))

print('Maximum Value in a dictionary: ',my_dict[key_max])
print('Minimum Value in a dictionary: ',my_dict[key_min])

# write a python program to do nothing for a condition

if 1 + 1 == 2:
    pass # Nothing

# write a python program to make use of enumerate method

for count, value in enumerate(obj):
    print(count, value)

# write a python program to make use of setdefault for missing dictionary keys
a_dict = {'a':1}
a_dict.setdefault('b',2)
print(f'After appending with new value:{a_dict}')

# write a python program to make use of maps

def square(number):
    return number ** 2

numbers = [1, 2, 3, 4, 5]

squared = map(square, numbers)

print(f'mapped numbers:{list(squared)}')

# write a python program to make use of modulo operator

print(f'modulo 15 % 4: Sol->{15 % 4}')

# write a python program to explain enclosing and global scope

x = 'global'

def f():
    x = 'enclosing'
    def g():
        print(x)
    g()
    return x
obj1 = f()
print('explain global scope:',obj1)

# write a python program to expain local and global scope

def f1():
    x = 'enclosing'
    def g():
        x = 'local'
        return x
    x=g()
    return x
obj2 = f1()
print('explain local scope:',obj2)

# write a python program to make use of regular expression for matching
import re
print('Find the characters in the given string:',re.findall(r'[a-z]+', '123FOO456', flags=re.IGNORECASE))

# write a python program to make use of regular expression for matching
s = 'foo123bar'
m = re.findall('123', s)
print('find the number position:',m)

# write a python program to convert lower string to UPPERCASE
a = 'string'
print(f'convert lowercase to uppercase:{a.upper()}')

# write a python program to convert uppercase string to lower
a = 'STRING'
print(f'convert lowercase to uppercase:{a.lower()}')

# write a Python Program to Find the Square Root
num = 8 

num_sqrt = num ** 0.5
print('The square root of %0.3f is %0.3f'%(num ,num_sqrt))

# write a Python Program to Convert Kilometers to Miles
kilometers = 10.0

conv_fac = 0.621371

miles = kilometers * conv_fac
print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))

# write a Python Program to Convert Celsius To Fahrenheit
celsius = 37.5
fahrenheit = (celsius * 1.8) + 32
print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(celsius,fahrenheit))

# write a Python Program to Check if a Number is Positive, Negative or 0
num = 10
if num > 0:
   print("Positive number")
elif num == 0:
   print("Zero")
else:
   print("Negative number")

# Python Program to Check if a Number is Odd or Even
num = 100
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))

# Python Program to Display the multiplication Table
num = 12
for i in range(1, 11):
   print(num, 'x', i, '=', num*i)

# write a program for Rolling the dices
import random
min = 1
max = 6

print("Rolling the dices...and the values are",random.randint(min, max))
print("Rolling the dices...and the values are",random.randint(min, max))

# write a python program to calculate the average
list1 = [1,3,4,5]
average = (sum(list1)) / len(list1)
print(f"the average score is:  {average} ")

# write a python program to print reverse list
print(f'reverese the given list elements:{list1[::-1]}')

# write a python program for creating the thread
import threading
from threading import Thread
import time

def print_time( threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s: %s" % ( threadName, time.ctime(time.time()) ))

# try:
#     Thread(target=print_time, args=("Thread-1", 2, )).start() 
#     Thread(target=print_time, args=("Thread-1", 4, )).start() 
# except:
#     print("Error: unable to start thread")

# write a python program to check a num is less than 1000
def near_thousand(n):
      return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))
print('near to 1000',near_thousand(1000))
print('near to 1300',near_thousand(1300))

# write a python program to convert lower case to upper for list of elements

x = ['ab', 'cd']
for i in x:
    print(i.upper())

# write a python program to break when the num is perfectly divisible
i = 1
while True:
    if i%3 == 0:
        break
    print(i)
 
    i+= 1

# write a python program to check name exists in given list
names1 = ['Amir', 'Bala', 'Chales']
for n in names1:
    name = n.lower()
    if 'amir' == name:
        print('Yes name exists:',name)
    else:
        print('No')

# write a python program to print a matrix as output
matrix = [[1, 2, 3, 4],
       [4, 5, 6, 7],
       [8, 9, 10, 11],
       [12, 13, 14, 15]]
 
for i in range(0, 4):
    print(matrix[i][1], end = " ")

# write a python program to calculate the time taken

from time import localtime

activities = {8: 'Sleeping',
              9: 'Commuting',
              17: 'Working',
              18: 'Commuting',
              20: 'Eating',
              22: 'Resting' }

time_now = localtime()
hour = time_now.tm_hour

for activity_time in sorted(activities.keys()):
    if hour < activity_time:
        print (activities[activity_time])
        break
else:
    print ('Unknown, AFK or sleeping!')


# write a python program to search a key in the text file
fname = 'sample.txt'
l='keyword' # Enter letter to be searched
k = 0
 
with open(fname, 'r') as f:
    for line in f:
        words = line.split()
        for i in words:
            if(i==l):
                k=k+1
print("Occurrences of the letter:",k)

# write a python program to expalin list comprehension and print alternative values
t = (1, 2, 4, 3, 8, 9)
print([t[i] for i in range(0, len(t), 2)])

# write a python program to sort tuple values
a=(2,3,1,5)
tuple_sorted = sorted(a)
print(tuple(tuple_sorted))

# write a python program to multiple two list values
l1=[1,2,3]
l2=[4,5,6]
print('multiply two list values:',[x*y for x in l1 for y in l2])

# write the list comprehension to pick out only negative integers from a given list ‘l’.
l1=[1,2,3,-4,-8]

print('negative integers:', [x for x in l1 if x<0])

# write a python program to convert all list elements to upper case
s=["pune", "mumbai", "delhi"]
print([(w.upper(), len(w)) for w in s])

# write a python program to expalin python zip method
l1=[2,4,6]
l2=[-2,-4,-6]
for i in zip(l1, l2):
	print(i)

# write a python program to add two list using python zip method

l1=[10, 20, 30]
l2=[-10, -20, -30]
l3=[x+y for x, y in zip(l1, l2)]
print('added two list:',l3)

# write a list comprehension for number and its cube 
l=[1, 2, 3, 4, 5, 6, 7, 8, 9]
print([x**3 for x in l])

# write a list comprehension for printing rows into columns and vv

l=[[1 ,2, 3], [4, 5, 6], [7, 8, 9]]
print([[row[i] for row in l] for i in range(3)])

# write a list comprehension for printing rows into columns and vv

def unpack(a,b,c,d):
    print(a+d)
x = [1,2,3,4]
unpack(*x)

# write a python program to use python lambda function
lamb = lambda x: x ** 3
print(lamb(5))

# write a python program to multiply a string n times
a = 'python'
print(a*5)

# write a python to check two numbers are greater than or equal or less than
def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return 'The numbers are equal'
    else:
        return y
 
print(maximum(2, 3))

# write a python to dict to zip and print as dictionary elements in original form

a={"a":1,"b":2,"c":3}
b=dict(zip(a.values(),a.keys()))
print(b)


# write a python program to delete an dictionary element
a={1:5,2:3,3:4}
a.pop(3)
print(a)

# write a python program to check two dictionary are equal or not
d1 = {"john":40, "peter":45}
d2 = {"john":466, "peter":45}
d1 == d2

# write a python program to print only dictionary keys as list

d = {"john":40, "peter":45}
print(list(d.keys()))

#write a python program to check two lists are equal or not

a=[1, 4, 3, 5, 2]
b=[3, 1, 5, 2, 4]
print(a==b)

#write a python program to check two lists are equal or not

a=frozenset(set([5,6,7]))
print(a)

#write a python program to sum the set of unqiue elements

a={5,6,7}
print(sum(a,5))

#write a python program to implement try catch code

try:
    s={5,6}
    s*3
except Exception as e:
    print(e)


#write a python program to count the len of unique elements

nums = set([1,1,2,3,3,3,4,4])
print(len(nums))

#write a python program to split in python

print('abcdefcdghcd'.split('cd', 2))

# write a python program to add title to string
print('ab cd-ef'.title())

# write a python program to print equal lenght of string
print('ab'.zfill(5))

# write a python program to use string replace
print('abcdef12'.replace('cd', '12'))

#  write a python program to check string istitle
str1 = 'Hello!2@#World'
if str1.istitle():
    print('Yes string is title')

#  write a python program to do lstrip on string

print('xyyzxxyxyy'.lstrip('xyy'))

#  write a python program to check identifier/keyword
print('for'.isidentifier())

#  write a python program to check is an num/int
print('11'.isnumeric())

#  write a python program to check is an variable is printable
print('1@ a'.isprintable())

#  write a python program to check it contains any space
print(''''''.isspace())

#  write a python program to check is an title
print('HelloWorld'.istitle())

#  write a python program to check is all are num/int
print('ab,12'.isalnum())

#  write a python program to check is all are alphanumeric
print('ab'.isalpha())

#  write a python program to check is all are digit
print('0xa'.isdigit())

#  write a python program to use f string
var1 = 'python language'
print(f'f-string is an good feature in {var1}')

#  write a python program to iterate an dict and concatenate

D=dict(p='san', q='foundry')
print('{p}{q}'.format(**D))

# write a python program to replace blank space to 1
a='1 0 0 1'
print(a.replace(' ', '1'))

# write a python program to explain the generator
def f11(x):
    yield x+1
g=f11(8)
print(next(g))

# write a python program to replace blank space to 1
def f12(x):
    yield x+1
    print("test")
    yield x+2
g=f12(9)
print(next(g))

# write a python program to replace blank space to 1
a = re.compile('[0-9]')
z= a.findall('3 trees')
print(z)

# write a python program to print current working directory
import os
print(os.getcwd())

# write a python program to print the ascii value of a string
print([ord(ch) for ch in 'abc'])

# write a python program to use extend in list/ append to a list
a=[13,56,17]
a.append([87])
a.extend([45,67])
print(a)

# write a python program to replace blank space to 1
my_string = 'balaji'
k = [print(i) for i in my_string if i not in "aeiou"]
print('Not a vowel',k)

# write a python program to add and square a range of number
x = [i**+1 for i in range(3)]; print(x)

# write a python program to replace blank space to 1
print([i+j for i in "abc" for j in "def"])

# write a python program to multiply two list with list comprehensive
l1=[1,2,3]
l2=[4,5,6]
print([x*y for x in l1 for y in l2])

# write a python program to print only digit or only apha charac in a given list
l=["good", "oh!", "excellent!", "#450"]
print([n for n in l if n.isalpha() or n.isdigit()])

# write a python program to print todays date
tday=datetime.date.today()
print(tday)

# write a python program to check tuple are immutable
a=(1,2,3)
try:
    a = a+1
except Exception as e:
    print(e)

# write a python program to calculate factorial sum using list comprehensive
import functools 
n =5
print(functools.reduce(lambda x, y: x * y, range(1, n+1)))

# write a python program to print len of each characters
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))
    
# write a python program to make increment on each call of method using lambda function
def make_incrementor(n):
    return lambda x: x + n
f = make_incrementor(42)
f(0)
print(f(1))

# write a python program to sort using list comprehensive
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)

# write a python program to del the first element of the array/list
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)
# write a python program to replace the first character of a given word
word = "goal"
word = "f" + word[1:]
print(word)
# write a python program to find a string in a given phrase
phrase = "the surprise is in here somewhere"
print(phrase.find("surprise"))
# write a python program to expalin the use of f-string
n = 3
m = 4
print(f"{n} times {m} is {n*m}")
# write a python program to explain the use of assert
# x=1
# y=8
# assert x>y, 'X too small'









