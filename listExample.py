motocyles =['Honda','Yamaha','Suzuki']
print(motocyles)

print(motocyles[0])
print(motocyles[1])
print(motocyles[2])

motocyles[1]='Dukati'
print(motocyles)

motocyles[2]='Hero'
print(motocyles)

fruits=[]
fruits.append('Mango')
fruits.append('Banana')
fruits.append('Orange')
print(fruits)

fruits.insert(1,'Mango')
print(fruits)

fruits.insert(3,'Grape')
print(fruits)

fruits.extend(['Orange','Banana','Jackfruit'])
print(fruits)

del fruits[4]
print(fruits)

fruits.pop()
print(fruits)

fruits.remove('Mango')
print(fruits)

cars = ['bmw','audi','subaru','toyota','audi','toyota','audi']
print(cars)

cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

print(sorted(cars))
print(cars)

cars.reverse()
print(cars)

print('Total Number of Cars :',len(cars))

print(cars[-1])
print(cars[-3])
print(cars[0:3])
print(cars[2:5])
print(cars[2:]) 
print(cars[:3]) 

print(cars.index('audi'))
#print(cars.index('Audi'))
print(cars.count('audi'))
print(cars.count('toyota'))

cars.extend(['audi', 'audi', 'bmw', 'subaru',])
print(cars)

nums=list(range(10))
print(nums)

print(min(nums))
print(max(nums))
print(sum(nums))

