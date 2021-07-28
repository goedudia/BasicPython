"""
Python Recursion
learn to create a recursive function (a function that calls itself).
----------------------------
What is recursion?

Recursion is the process of defining something in terms of itself.

A physical world example would be to place two parallel mirrors facing each other. 
Any object in between them would be reflected recursively.
"""

#Factorial using Loop
# 3! = 1x2x3 = 6

num =5
fact=1

for i in range(1,num+1):
    fact= fact*i

print("The factorial of ",num,"is",fact)

#Factorial using Recursive Method

def factorial(n):
    if n==0:
        return 1
    else:
        return n* factorial(n-1)

print("The factorial of ",num,"is",factorial(num))        

#Fibonacci Series Using Loop
# fibo[n] = fibo[n-1]+fibo[n-2]
# fibo[i] = fibo[i-1]+fibo[i-2]

n=8
fibo= [0,1]

for i in range(2,n+1):
    nextElement = fibo[i-1]+fibo[i-2]
    fibo.append(nextElement)

print('The fibonacci series ',fibo)

#Fibonacci Series Using Recursive
def fibonacci(n):
    if n==0:
        return [0]
    elif n==1:
        return [0,1]
    else:
        fibo=fibonacci(n-1)
        nextElement = fibo[n-1]+fibo[n-2]
        fibo.append(nextElement)
        return fibo
num = 8
print('The fibonacci series ',fibonacci(num))


#Prime Number using Loop

def isPrime(n):
    for i in range(2,n):
        if n%i==0:
            return " Not a prime number"
        else:
            return " prime number"

num =7
print("The number ",num,"is",isPrime(num))

#Prime Number using Recursive Method

def checkPrime(num,i=2):
    if num==i:
        return True
    else:
        if num%i==0:
            return False
        else:
            return checkPrime(num,i+1)

num=20

if checkPrime(num):
    print("The number ", num,"is a Prime Number")
else:
    print("The number ", num,"is not a Prime Number")