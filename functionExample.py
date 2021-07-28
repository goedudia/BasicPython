# Syntax of Function

# def function_name(parameters):
# 	"""docstring"""
# 	statement(s)

def welcome():
    """ This is a document string """
    print("Hello Nazmul Good Morning!")

welcome()
print(welcome.__doc__)

def welcome(name):
    """ This is a document string """
    print(f"Hello {name} Good Morning!")

welcome('Rahim')
welcome('Karim')

def welcome(name,msg):
    """ This is a document string """
    print(f"Hello {name} {msg}!")

welcome('Rahim','Good Morning')
welcome('Karim','Good Evening')

def welcome(*name):
    for i in name:
        print("Hello",i)

welcome('Munaz','Ali','Reza','Tuhin')        

#functionName = lambda arguments: expression

double = lambda x: x*2

print(double(5))

myList =[1,5,4,8,11,9,13]
newList = list(filter(lambda x: (x%2!=0),myList))
print(newList)

def describe_pet(animal_type,pet_name):
    print('\nI have a '+ animal_type)
    print('My '+ animal_type + '\'s name is '+ pet_name.title())

describe_pet(animal_type='Dog', pet_name='Tommy')
describe_pet( pet_name='Tommy',animal_type='Dog')

def describe_pet(pet_name,animal_type="Dog"):
    print('\nI have a '+ animal_type)
    print('My '+ animal_type + '\'s name is '+ pet_name.title())

describe_pet('Jimmy','Cow')

def fullName(firstName,lastName):
    return f'{firstName} {lastName}'

print(fullName('Nazmul','Haque'))


def welcome_users(names):

    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['Rahim','Ali','Nazmul']
welcome_users(usernames)

def build_profile(first,last, **user_info):
    profile={}
    profile['first_Name'] = first
    profile['last_Name'] = last

    for key,value in user_info.items():
        profile[key]= value

    return profile

user_profile  = build_profile('Nazmul','Haque', location='Dhaka',field='IT')

print(user_profile)











