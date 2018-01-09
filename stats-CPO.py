from collections import defaultdict

#Add two numbers
def add (num1, num2):
    return num1 + num2

print (add(5,2))

#Commute volume of a cube
def rectvol(length, width, height):
    return (length * width * height)

#Find the mean of a list of numbers
def mean(numbers):
    return sum(numbers)/len(numbers)

def median(numbers):
    """
    Computes the median of a list of numbers.

    Argument: list of numbers
    Return:   the median

    >>> median([2,1,6])
    2
    >>> median([3,5,4,9])
    4.5
    """
    numbers = sorted(numbers)
    middle = (len(numbers))// 2

    if (len(numbers) % 2 == 1): # if odd
        return numbers[middle]
    else: #if even
        return sum(numbers[middle -1:middle + 1])/2.0

def mode(numbers):
    """
    Find the most common frequent value in the list

    Argument: list of numbers
    Return: the mode

    >>> mode([6,6,6,8,8,7])
    6
    """
    d = defaultdict(int)
    for num in numbers:
        d[num]+=1
    return sorted(d, key = lambda k: d[k])[-1]
    #return sorted(d, key = lambda key: d[key], reverse = True)[0]
