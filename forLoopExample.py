x= list(range(10))
print(x)

x= list(range(5,10))
print(x)

x= list(range(1,10,2))
print(x)

for p in range(10):
    print(p,end ='\t')
print('\n')

for p in range(1,10):
    print(p,end ='\t')
print('\n')

for p in range(1,100,5):
    print(p,end ='\t')
print('\n')

sum=0
for w in range(1,11):
    sum = sum + w
    print(w,end='+')

print(chr(8) + '=' + str(sum),end='\t')
print('\n')

# c=input('Enter a character : ')
# print('The ASCII value of %s is %s' % (c,ord(c)))
# print('\n')

# i= int(input('Enter ASCII Value : '))
# print('The Character of  of %s is %s' % (i,chr(i)))
# print('\n')

for x in range(65,91):
    print(chr(x),end='\t')
print('\n')

for x in range(97,123):
    print(chr(x),end='\t')
print('\n')

for x in range(1,101):
    if x % 2 == 0:
        print(x,end='\t')
print('\n')
