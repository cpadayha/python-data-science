#Run it: ipython -i basic.py

""" LIST []"""
# List: mutable, homogenous, ordered []
odds = [5,7,9]
sum(odds)

total = 0
for num in odds:
    total = total + num
    #total =+ num

"""Enumerate"""
#Unpacks a tuple
total = 0
for i, num in enumerate(odds): #enumerate returns a tuple of the index
    total = total + (i * num)

"""List comprehension"""
#square values
squares = [n**2 for n in odds]

#square root
square_roots = [n**0.5 for n in odds]

#Sum of the square roots
sum_sq_root = sum([n**0.5 for n in odds])

#List of all odd values
odder = [n for n in range (31) if n % 2 == 1] #ranges goes up to but does not include

#Sum of the cube root of numbers divisible by 5
divisibleby5 = sum([n**(1/3) for n in range (31) if n % 5 == 0]) #range of numbers divible by 5


"""Map"""
list(map(lambda n: n**(1/3, odds)))
#map takes a list from odds and is the input to the fuction.
#function is returned: n**(1/3)
#lambda is a function. in line function. function without a name.
#could also use any function. Ex: list(map(square, odds))
#map takes an old list, transforms and creates a new list

"""Filters"""
lessthan5 = list(filter(lambda n: n < 5, [3, 4, 5, 6, 7]))


"""Reduce"""
from functools import reduce
#takes a bunch of values and reduces to 1
reducefcn = reduce(lambda total, n: total + n, odds)
#see picture

""" TUPLE ()"""
#Tuple (): immutable, heterogenous (read only list cannot add to), ordered
tup1 = (3,4)

""" SET {}"""
#Set {} : unordered, distinct values, hashable, mutable but only takes immutable objects, order doesn’t matter, iterable
#intersection
s1 & s2 #intersection - what is in common
s1 | s2 #union - all values
s1 ^ s2 #disjoint - what is not in common

""" DICTIONARY {}"""
#Dictionary (dict): mapping object (key/object), maps hashable values to arbitrary objects, keys are hashable, mappings are mutable, unordered

#create a dictionary where the value is the square
d = {}
for n in range(5):
    d[n] = n ** 2

#pull just the keys
d.keys()

#split key and values
for k in d.keys():
    print(k, 'values', d[k])

#Check for key, if not present then 0
d.get(5,0)

"""Dictionary comprehension"""
dc = {n: n**0.5 for n in range(100) if n%10 ==0}
