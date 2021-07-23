import sys
class Student:
    def __init__(self):
        self.name = ''
        self.score = 0
        self.llink = None
        self.rlink = None

prev = None
current = None
ptr = None

head = Student()
head.name = ''
head.llink = head
head.rlink = head

def insert_f():
    global ptr
    global head
    global current
    global prev

    ptr = Student()
    ptr.name = input('\n Please enter student name: ')
    ptr.score = eval(input( 'Please enter student score: '))
    print()

    prev = head
    current = head.rlink
    while current != head and current.score >= ptr.score:
        prev = current
        current = current.rlink
    ptr.rlink = current
    ptr.llink = prev
    prev.rlink = ptr
    current.llink = ptr

def delete_f():
    global head
    global current
    global prev

    del_name = ''

    if head.rlink == head:
        print('\n    No student record!! \n')
    else:
        del_name = input('   Delete student name: ')

        prev = head
        current = head.rlink
        while current != head and del_name != current.name:
            prev.current
            current = current.rlink

        if head != current:
            prev.rlink = current.rlink
            current.rlink.llink = prev
            current = None
            print('     Student %s record deleted!!\n' % del_name)
        else:
            print('     Student %s not found!!\n' % del_name)

def modify_f():
    global head
    global current
    global prev

    if head.rlink == head:
        print('\n    No student record!!\n')
    else:
        modify_name = input('   Modify student name: ')

        prev = head
        current = head.rlink
        while current != head and modify_name != current.name:
            prev = current
            current = current.rlink

        if current != head:
            print('\n   Student name: %s' % current.name)
            print('   Student score: %d\n' % current.score)
            prev.rlink = current.rlink
            current.rlink.llink = prev
            current = None
            newscore = eval(input(' Please enter new score: '))
            ptr = Student()
            ptr.next = None
            ptr.name = modify_name
            ptr.score = newscore
            prev = head
            current = head.rlink
            while current != head and current.score >= ptr.score:
                prev = current
                current = current.rlink
            ptr.rlink = current
            ptr.llink = prev
            prev.rlink = ptr
        else:
            print('\n Student %s not found!\n' % modify_name)

def display_f():
    global head
    global current

    count = 0

    if head.rlink == head:
        print('\n     No student record!!\n')
    else:
        print('\n%-15s %-10s' % ('NAME', 'SCORE'))
        print('----------------------------------')
        current = head.rlink
        while current != head:
            print('%015s %-3d' % (current.name, current.score))
            count = count + 1
            current = current.rlink
        print('----------------------------------')
        print('There is(are) %d record(s) found!!\n' % count)

def main():
    option = 0

    while True:
        print('*****Doubly linked list *****')
        print('        <1> Insert           ')
        print('        <2> Delete           ')
        print('        <3> Modify           ')
        print('        <4> List             ')
        print('        <5> Exit             ')
        print('*****************************')

        try:
            option = int(input('      Choice: '))
        except ValueError:
            print()
            print('Not a correct number')
            print('Try again\n')

        if option == 1:
            insert_f()
        if option == 2:
            delete_f()
        if option == 3:
            modify_f()
        if option == 4:
            display_f()
        if option == 5:
            sys.exit(0)

main()
