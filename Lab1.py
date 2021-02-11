"""
Lab #1 - Coding Questions in Python (1208-FIU01-COP-4814-SECU03-85809)
R.E
<<<<<<< Updated upstream
PID: ######
=======
PID: #####
>>>>>>> Stashed changes
Date: 2020

"""


# Question #1
arr1 = []  # Creating array to store the values (Integers)
for i in range(2000, 3201):  # This is to create a range between this two numbers
    if (i % 7 == 0) and (i % 5 != 0):  # if X is divisible by 7 but not by 5 with 0 as reminder
        arr1.append(str(i))  # i (integers Calculation)  is added to the array
print(arr1)  # Printing the array with the values

# Question #2
n = int(input("Enter a Number: "))  # Creating a number (n)
d = dict()  # Creating a dictionary variable

for i in range(1, n + 1):  ## for i in range or list, iterate each element
    d[i] = i * i
print(d)


# Question #3

def ageMessage():  ##  Creating the method
    name = str(input("Enter your name: "))  ##  Creating the variables for the calculation
    age = int(input("Enter your age: "))
    old: str = str((100 - age) + 2020)  ##  Solving the Calculation
    print(name + ", You will be 100 years on " + old)


ageMessage()  ## Returning /  closing function


# Question #4
def divisor():
    num = int(input("Enter a integer number: "))  ##  Asking for integer number
    print("This number is divisible by: ")  ##  Print
    for i in range(1, num + 1):  ##  range for loop to go through the numbers
        if (num % i == 0):  ##  Divisible by
            print(i)  ##  Print number in the loop


divisor()


# Question #5

def evenList():
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]  ## a(list)
    b = [i for i in a if i % 2 == 0]  ## new b list [element for element in A list if only is divisible by 2
    print("Previous list was: " + str(a) + " and New list with only even numbers " + str(b))
    ##  Concatenated strings with integers by using str(element)


evenList()


# Question #6

def noDuplicates():  ##  Creation of a function
    list1 = [1, 2, 3, 4, 6, 10, 0]  ##  Creation of a list 1
    list2 = [1, 9, 3, 8, 7, 2, 3, 1]  ##  Creation of a list 2
    common = list(set(list1) & set(list2))  ##  Creation of new list with no duplicates
    ## newList(set(element1) and set(element2))--Variable to store the values
    print(common)


noDuplicates()


# Question #7

def sumValues(myDictionary):
    sum = 0  ##  Intiation of the sum == 0
    for i in myDictionary:  ## for each element in dictonary
        sum = sum + myDictionary[i]  ## add to the variable sum -- sum (0) + elements in dictionary one by one
        print(sum)  ## Print Each time that is added to the list
    return sum


dictionary: [str, int] = {'A': 100, 'B': 80, 'C': 70}  ## Fuction
print("The total of the Sum is: ", sumValues(dictionary))

sumValues(dictionary)

# Question #9

def primeNumber():
    num: int = 2020  ##  variable
    if not num <= 1:  ##  If number is greater than 1
        for i in range(2, num):  ##  For loop to go repeatedly from 2 to n /2
            if (num % i) == 0:  ##  To check the number if divisible by 2 and equal to 0
                print(num, "This number is not prime number because is divisible by 2")
            break
        else:  ##  second if statement
            print(num, "This number is a prime number because is greater than 1 and not divisible by 2")
    else:  ##  first if statement
        print(num, "This number is not a prime number because is not greater than 1")


primeNumber()


# Question #10

def asciiNum():  ##  Function
    character = input("Type a character: ")  ##  input character
    ##  the ord() function in python accepts a string of length 1 as an argument and return the unicode code
    print("This character |{0}| has ASCII number of: ".format(character), ord(character))


asciiNum()


# Question #11

def fibonacci():
    ##  Input variable, to get the range of the fibonacci sequence
    n = int(input("Type an integer number to return the first n fib numbers: "))
    if n == 1:  ## first step to find out if the number is one: first fibonacci number is 1
        fib = [1]
    elif n == 2:
        fib = [1, 1]
    else:
        fib = [1, 1]
        for i in range(2, n):  ## for i in range of 2 and number
            fib.append(fib[i - 1] + fib[i - 2])
    print(fib)


fibonacci()

# Question #12

def max(a, b, c):  ## function with  3 pararmeters
    if (a >= b) and (a >= c):
        largest = a
    elif (b >= a) and (b >= c):
        largest = b
    else:
        largest = c
    return largest


a = input("Type a integer number : ")  ##  input character
b = input("Type second integer number : ")  ##  input characterb
c = input("Type third integer number : ")  ##  input character
print("The largest number from the three input integer numbers is: ", max(a, b, c))

max(a, b, c)


"""
Sources:
https://www.w3schools.com/python/python_comments.asp
https://www.python.org/
https://beginnersbook.com/2018/03/python-tutorial-learn-programming/

"""
