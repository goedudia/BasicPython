#Syntax of Python open file function
#file_object  = open("filename", "mode") 

# File Modes in Python
# Following are the various File Modes in Python:

# Mode	Description
# 'r'	This is the default mode. It Opens file for reading.
# 'w'	This Mode Opens file for writing.
# If file does not exist, it creates a new file.
# If file exists it truncates the file.
# 'x'	Creates a new file. If file already exists, the operation fails.
# 'a'	Open file in append mode.
# If file does not exist, it creates a new file.
# 't'	This is the default mode. It opens in text mode.
# 'b'	This opens in binary mode.
# '+'	This will open a file for reading and writing (updating)

#Syntax of Python open file function
#file_object  = open("filename", "mode") 

f = open("dia.txt","w+")

#Enter data into the file
for i in range(10):
    f.write("This is line %s\n" % (i+1))

f.close()

#Append a new line to existing file
f= open("dia.txt","a+")

for i in range(2):
    f.write("Appended line %s\n" % (i+1))

f.close()

#Open the file in read mode
f= open("dia.txt","r")

if f.mode=='r':
    contents = f.read()
    print(contents)
f.close()

#Read line by line
f= open("dia.txt","r")

lines = f.readlines()
#print(lines)

for x in lines:
    print(x)
f.close()
