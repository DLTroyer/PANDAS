'''List comprehensions provide a concise way to create lists. 

It consists of brackets containing an expression followed by a for clause, then
zero or more for or if clauses. The expressions can be anything, meaning you can
put in all kinds of objects in lists.

The result will be a new list resulting from evaluating the expression in the
context of the for and if clauses which follow it. 

The list comprehension always returns a result list. '''


'''
new_list = []
for i in original_list:
    if filter(i):
        new_list.append(expressions(i))  '''

#You can obtain the same thing using list comprehension:

# new_list = [expression(i) for i in original_list if filter(i)]


#The list comprehension starts with a '[' and ']', to help you remember that the
#result is going to be a list.

# [ expression for item in list if conditional ]

# This is equivalent to:

'''for item in list:
    if conditional:
        expression '''
		
		


#Which corresponds to:

#*result*  = [*transform*    *iteration*         *filter*     ]

#The * operator is used to repeat. The filter part answers the question if the
#item should be transformed. '''

##side note: this would print out a list from 0-9
x = [i for i in range(10)]

print(x)

#Adding an expression
squares = [x**2 for x in range(10)]

print(squares)


list1 = [3,4,5]
multiplied = [item*3 for item in list1]
print(multiplied)

list_of_words = ['This', 'is', 'a', 'list', 'of', 'words']
items = [word[0] for word in list_of_words]
print(items)

upper = [x.upper() for x in ['a','b','c']]
print(upper)

#adding an if function
##side note: % is the remainder in this case i is being devided by 2 but the answer is the remainder
new_range = [1*1 for i in range(5) if i % 2 == 0]
print(new_range) #this will give you just the even numbers

string = "hello 12345 World"
numbers = [x for x in string if x.isdigit()]

print(numbers)

##side note: isalpha returns the letters
letters = [x for x in string if x.isalpha()]
print(letters)


my_file = open('test.txt','r')
result = [i for i in my_file if "line3" in i]
print(result)

def double(x):
    return x*2

print(double(10))

result1 = [double(x) for x in range(10)]
print(result1)

#this is like a nested loop. Starts in the outer and goes to the inner
result2 = [x+y for x in [10,20,30] for y in [40,50,60]]
print(result2)

## Exercise ##

# 1 Using a list comprehension, create a new list called "newlist" out of the list "numbers", 
# which contains only the positive numbers from the list, as integers.

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]

postives = [num for num in numbers if num > 0]
print(postives)


## 2 create a list of integers which specify the length of each word in
## a sentence except for the word 'the'

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()

length = [len(i) for i in words if i != 'the']
print(length)



## Given dictionary is consisted of vehicles and their weights in kilograms. 
## Contruct a list of the names of vehicles with weight below 5000 kilograms. 
## In the same list comprehension make the key names all upper case.

dict={"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, 
"Semi": 13600, "Bicycle": 7, "Motorcycle": 110}

vehicles = [i.upper() for i in dict if dict[i]< 5000]