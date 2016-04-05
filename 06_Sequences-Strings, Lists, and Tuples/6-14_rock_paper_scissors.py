#!usrbinenv python
import random

def rps(arg1, arg2):
    # ['rock','paper','scissors']
    rule = {'rp':-1,'rs':1,'rr':0, 'pr':1,'ps':-1,'pp':0, 'sr':-1,'sp':1,'ss':0}
    return rule[arg1[0] + arg2[0]]

user_value = raw_input('your choose: [rock|paper|scissors] ')
app_value = ['rock','paper','scissors'][random.randint(0,2)]
print 'app chooses ' + app_value

res = rps(user_value, app_value)
if res == 1:
    print 'user win'
elif res == 0:
    print 'equals'
else:
    print 'application win'
