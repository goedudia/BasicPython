
students={1:'Ali',2:'Rahim',3:'Karim',4:'Tahmid',6:'Nazmul'} # key Value
print(students)
print(students[4])
print(students[2])

employees=students.copy()
print(employees)

#  modify data using 'key'
employees.update({4:'Mahadi Hasan'})
print(employees)

employees.update({5:'Nasheed'})
print(employees)

# Delete Data using 'Del' Command

del employees[4]
print(employees)

print(dir(employees))
print('Display Items')
print('Employee Name %s'%(employees.items()))
print('Employee Name %s'%(list(employees.items())))

print('Display Only Keys')
for k in employees.keys():
    print(k)

print('Display Only Values')
for k in employees.values():
    print(k)

print('Key With Values')
for k in employees.keys():
    print(str(k)+'-'+str(employees[k]))

print('total Item '+str(len(employees)))

for k,v in employees.items():
    print(k,v)

for k,v in employees.items():
    print(f'id:{k}name:{v}')

print(employees.get(3))
employees[9]='Kormokar'
print(employees)

emp=list(employees.keys())
print(emp)

emp.sort()
print(emp)

if 5 in employees:
    print('Has Found')
else:
    print('Not Found')

x=1
while x <4:
    print(employees[x])
    x=x+1

print(type(employees))
print(dir(dict))
"""
'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 
'popitem', 'setdefault', 'update', 'values']
"""


plants = {}

# Add three key-value tuples to the dictionary.
plants["radish"] = 2
plants["squash"] = 4
plants["carrot"] = 7

# Get syntax 1.
print(plants["radish"])

# Get syntax 2.
print(plants.get("tuna"))
print(plants.get("tuna", "no tuna found"))
print(plants.get("carrot"))

print(len(plants))
print(sorted(plants))

# Dictionary Comprehension
# squares = {x: x*x for x in range(6)}
# print(squares)

# # Dictionary Built-in Functions
# squares = {0: 0, 1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

# # Output: 6
# print(len(squares))

# # Output: [0, 1, 3, 5, 7, 9]
# print(sorted(squares))


