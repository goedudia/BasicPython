num = 10

print(num)

a,b,c = 13, 2.88, "Hello"
print(a,b,c)

print(type(a))
print(type(b))
print(type(c))

strings = "This is Python"
char = "C"
multiline_str = """This is a multiline string with more than one line code."""
unicode = u"\u00dcnic\u00f6de"
raw_str = r"raw \n string"

print(strings)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)

fruits = ["apple", "mango", "orange"] #list
numbers = (1, 2, 3) #tuple
alphabets = {'a':'apple', 'b':'ball', 'c':'cat'} #dictionary
vowels = {'a', 'e', 'i' , 'o', 'u'} #set

print(fruits)
print(numbers)
print(alphabets)
print(vowels)

print(a,b,c,sep="*")
print(a,b,c,sep="*",end="#")

print("\n %s %s %s" % (a,b,c))
print("\n a={0} b={1} c={2}".format(a,b,c))
print(f"\n a={a} b={b} c={c}")


