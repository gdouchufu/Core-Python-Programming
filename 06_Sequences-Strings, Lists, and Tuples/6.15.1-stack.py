#!/usr/bin/env python

stack = []

def pushit():
    stack.append(raw_input('Enter new string: ').strip())

def popit():
    if len(stack) == 0:
        print 'Cannot pop from an empty stack!'
    else:
    	'''
    	use single backquotes or backticks ( ` ) to symbolize the repr() command, 
        showing the string complete with quotes, not just the contents of the string.
        '''
        print 'Removed [', `stack.pop()`, ']'         


def viewstack():
    print stack      # calls str() internally

CMDs = {'u': pushit, 'o': popit, 'v': viewstack}

def showmenu():
    pr = """
p(U)sh
p(O)p
(V)iew
(Q)uit

Enter choice: """

    while True:
        while True:
            try:
                choice = raw_input(pr).strip()[0].lower()
            except (EOFError,KeyboardInterrupt,IndexError):
                choice = 'q'

            print '\nYou picked: [%s]' % choice
            if choice not in 'uovq':
                print 'Invalid option, try again'
            else:
                break

        if choice == 'q':
            break
        CMDs[choice]()

if __name__ == '__main__':
    showmenu()
