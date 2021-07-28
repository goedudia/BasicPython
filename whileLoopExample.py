x=0

while x<=10 :
    print(x)
    x= x+1

n=70
while n<=200 :
    if n%2==0:
        print(n, end='\t')

    n= n+1
print('\n')

while True:
    ch = input('Enter your name : ')
    if ch=='quit':
        break
print('\n')

i=65
while i<=90:
    print(chr(i),end='\t')
    i= i+1
print('\n')

i=97
while i<=122:
    print(chr(i),end='\t')
    i= i+1
print('\n')

rev = 0
n= int(input('Enter a Number : '))
while n!=0:
    rem = n%10
    rev = rev*10 + rem

    n = n//10

print('The Reverse is : %s' % (rev))