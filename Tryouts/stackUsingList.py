import sys

class Student:
    def __init__(self):
        self.name = ''
        self.score = 0
        self.next = None

ptr = None
current = None
prev = None

head = Student()
head.next = None

def insert_f():
    global ptr
    global head

    ptr = Student()
    ptr.next = None
    ptr.name = input('Student name: ')
    ptr.score = eval(input('Student score: '))
    print()

    ptr.next = head.next
    head.next = ptr

def delete_f():
    global head
    global current
    global prev

    def_name = ''
    if head.next == None:
        print(' Stack is empty!\n')
    else:
        current = head.next
        head.next = current.next
        print('%s has been deleted!\n' % current.name)

def display_f():
    global head
    global current

    count = 0
    if head.next == None:
        print(' No student record\n')
    else:
        print('%-15s %-15s' % ('NAME', 'SCORE'))
        for i in range (25):
            print('-', end = '')
        print()
        current = head.next
        while current != None:
            print('%-17s %-15d' % (current.name, current.score))
            count += 1
            current = current.next
        for i in range(25):
            print('-', end = '')
        print()
        print('Total %d record(s) found\n' % count)

def main():
    option = 0
    while True:
        print('****** Single list operation ******')
        print('          <1> Insert               ')
        print('          <2> Delete               ')
        print('          <3> Display              ')
        print('          <4> Exit                 ')
        print('***********************************')

        try:
            option = int(input('     Choice: '))
        except ValueError:
            print('Not a correct number.')
            print('Try again\n')

        print()
        if option == 1:
            insert_f()
        elif option == 2:
            delete_f()
        elif option == 3:
            display_f()
        elif option == 4:
            sys/exit(0)

main()
