from os import O_NDELAY


x = 100
y = 8.8
z = 'hello world'
#In python, there's no need to declare data type, and no need to add semicolons (;) at the end of each line
#Python operations: +, -, *, // (divide and take integer), / (divide and take float), % (divide and take remainder)
#More operations: ==, !=, <, >, <=, >=
#Python does not have the operators ++ and -- (what a bummer)
#Python does not use && || !. Instead, we use and or not.

#print
print('x = %d, y = %d' %(x,y))

#if elif else
num = 2
if num==1:
    print('x=1\n')
elif x==2:
    print('x=2\n')
else:
    print('x>2\n')

#while loop
i = 1
total = 0
while i <= 100:
    total += i
    i+= 1
print('total = ', total)

#for loop
j = 1
total = 0
for i in range(101):
    total += i
print('total = ', total)

#array
numbers = [1, 2, 3]
#2Darray
moreNumbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#Call-by-value: See Call_by_value.py
#Call-by-reference: See Call_by_reference.py

#Python % formatting
one_number = eval(input('Please insert a number: '))
print('number = %d' % one_number)
print('number = %5d' % one_number)
print('number = %-5d' % one_number)
print('number = %05d' % one_number)
print('number = %.2e' % one_number)
print('number = %.2f' % one_number)
print('number = %s' % one_number)
print('number = %-20s' % one_number)

#List comprehension in Python
longlist = [221, -10, 94, 'no data', 3.4]
new_longlist = [i if isinstance(i, int) else 0 for i in longlist]
#if i is not an instance of integer, it will append 0 into new_longlist.
#Otherwise, it will append the original vaulue
print(new_longlist)

#Functions and Classes: See functionAndClass.py

#File processing in python
with open("notes.txt") as myfile:
    #if today file is stored somewhere else, you will need to specify the location
    #Ex: files/notes.txt if it is under a folder "files"
    content = myfile.read()
    myfile.seek(0) #Cursor returns to the top of the file
    print(content)

#Create new .txt file and write on it
with open("newnotes.txt", "w") as newfile:
    newfile.write("This is a new note\nYay I'm on the next line")

#Append new things onto a created file
with open("notes.txt", "a") as myfile:
    myfile.write("\nbanana")

#Modules in Python: See modules.py and calc.py

#Lambda functions (anonymous function) for python
first_lambda = lambda a: a + 10
#reads the value of a, and returns a + 10
print(first_lambda(5)) #prints 15

second_lambda = lambda a: 'green' if a < 10 else 'orange' if 10 <= a < 20 else 'red'
#reads the value of a, green if a is less than 10, orange if a is between 10 and 20, or red otherwise
print(second_lambda(15)) #prints orange

#Pandas in Python: See Pandas.py
