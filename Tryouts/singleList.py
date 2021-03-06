import sys

class Student:
    def __init__(self):
        self.name = ' '
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
    global current
    global prev

    ptr = Student()
    ptr.next = None
    ptr.name = input('Student name: ')
    ptr.score = eval(input('Student score: '))
    print()

    prev = head
    current = head.next
    while current != None and current.score >= ptr.score:
        prev = current
        current = current.next
    ptr.next = current
    prev.next = ptr

def delete_f():
    global head
    global current
    global prev

    del_name = ''
    if head.next == None:
        print(' No student record\n')
    else:
        del_name = input(' Delete student name: ')
        prev = head
        current = head.next
        while current != None and del_name != current.name:
            prev = current
            current = current.next
        if current != None:
            prev.next = current.next
            current = None
            print('\n Student %s record deleted\n' % del_name)
        else:
            print('\n Student %s not found\n' % del_name)

def modify_f():
    global head
    global current
    global prev
    global ptr

    if head.next == None:
        print(' No student record\n')
    else:
        modify_name = input(' Modify student name: ')
        prev = head
        current = head.next
        while current != None and modify_name != current.name:
            prev = current
            current = current.next
        if current != None:
            print('\n Student name: %s' % current.name)
            print(' Student score: %d\n' % current.score)
            prev.next = current.next
            current = None

            newscore = eval(input(' Please enter new score: '))
            ptr = Student()
            ptr.next = None
            ptr.name = modify_name
            ptr.score = newscore
            prev = head
            current = head.next
            while current != None and current.score >= ptr.score:
                prev = current
                current = current.next
            ptr.next = current
            prev.next = ptr
            print(' Data updated successfully!\n')
        else:
            print('\n Student %s not found!\n' % modify_name)

def display_f():
    global head
    global current

    count = 0
    if head.next == None:
        print(' No student record\n')
    else:
        print('%-15s %-15s' % ('NAME', 'SCORE'))
        for i in range(25):
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
        print('          <3> Modify               ')
        print('          <4> Display              ')
        print('          <5> Exit                 ')
        print('***********************************')

        try:
            option = int(input('        Choice : '))
        except ValueError:
            print('Not a correct number.')
            print('Try again\n')

        print()
        if option == 1:
            insert_f()
        elif option == 2:
            delete_f()
        elif option == 3:
            modify_f()
        elif option == 4:
            display_f()
        elif option == 5:
            sys.exit(0)

main()
