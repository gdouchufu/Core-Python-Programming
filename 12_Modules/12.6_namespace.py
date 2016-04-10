def foo():
    print '\ncalling foo()...'
    aString = 'bar'
    anInt = 42
    print "foo()'s globals:", globals().keys()
    print "foo()'s locals:", locals().keys()

print "__main__'s globals:", globals().keys()
print "__main__'s locals:", locals().keys()
foo()

'''
__main__'s globals: ['__builtins__', '__file__', '__package__', '__name__', 'foo', '__doc__']
__main__'s locals: ['__builtins__', '__file__', '__package__', '__name__', 'foo', '__doc__']

calling foo()...
foo()'s globals: ['__builtins__', '__file__', '__package__', '__name__', 'foo', '__doc__']
foo()'s locals: ['anInt', 'aString']
'''