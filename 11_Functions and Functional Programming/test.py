person = ['name',['savings',100.00]]
hubby = person[:]
wifey = list(person)
hubby[0] = 'joe'
wifey[0] = 'jane'

def count(who):
    def cost(f,*args,**kargs):
        if len(args) != 2:
            print 'paras num error'
        elif args[0] == 'joe':
            hubby[1][1] -= args[1]
            print hubby,wifey,person
        elif args[0] == 'jane':
            wifey[1][1] -= args[1]
            print hubby,wifey,person
        else:
            print 'paras error'

    def hubby_cost(f):
        def wrapper(*args,**kargs):
            cost(f,*args,**kargs)
            return f(*args,**kargs)
        return wrapper

    def wife_cost(f):
        def wrapper(*args,**kargs):
            cost(f,*args,**kargs)
            return f(*args,**kargs)
        return wrapper

    try:
        return {'joe':hubby_cost,'jane':wife_cost}[who]
    except KeyError,e:
        raise ValueError(e),'must be "joe" or "jane"'

@count('joe')
def changehubby(name,money):
    print 'change count of %s, minus %f' % (name,money)

@count('jane')
def changewifey(name,money):
    print 'change count of %s, minus %f' % (name,money)

changehubby('joe',10.0)
changewifey('jane',20.0)