from datetime import datetime
import hashlib, os
import pickle as p
import shelve as s

db = {}

def newuser():
    value = []
    prompt = 'login name desired again: '
    while True:
        name = raw_input(prompt).lower()
        if not name.isalnum() and '' in name:
            print 'name format error'
            continue
        else:
            if db.has_key(name):
                prompt = 'name taken,try another: '
                continue
            else:
                break
    pwd = raw_input('login passwd desired: ')
    m = hashlib.md5()
    m.update(pwd)
    value.append(m.hexdigest())
    value.append(datetime.now())
    db[name] = value
    print 'new user is %s, register time is %s' % (name, db[name][1])


def olduser():
    name = raw_input('login name desired again: ').lower()
    pwd = raw_input('login passwd desired: ')
    m = hashlib.md5()
    m.update(pwd)
    passwd = db.get(name)
    if passwd[0] == m.hexdigest():
        newtime = datetime.now()
        if (newtime - db[name][1]).days == 0 and (newtime - db[name][1]).seconds < 14400:
            print 'you already logged in at %s: ' % (db[name][1])
        else:
            passwd[1] = newtime
            print 'welcome back %s, login time is %s' % (name, passwd[1])

    else:
        print 'login incorrect'


def removeuser():
    print db
    name = raw_input('input a user name to remove: ').lower()
    if name in db:
        db.pop(name)
    else:
        print 'input error'


def userlogin():
    while True:
        name = raw_input('login name desired: ').lower()
        if not name.isalnum() and '' in name:
            print 'name format error'
            continue
        else:
            if not db.has_key(name):
                print 'user name is not in db'
                answer = raw_input('register a new user? y/n').lower()
                if 'y' == answer:
                    newuser()
                    break
                elif 'n' == answer:
                    break
            else:
                print 'user name is already in db'
                olduser()
                break


def output_use_file():
    print db
    f = open('account.txt', 'w')
    for key in db:
        user = key + ':' + db[key][0] + ':' + str(db[key][1]) + os.linesep
        f.write(user)
    f.close()


def output_use_pickle():
    accountfile = 'pickle.data'
    f = open(accountfile, 'w')
    p.dump(db, f)
    f.close()

    f = open(accountfile)
    accountdb = p.load(f)
    print accountdb


def output_use_shelve():
    accountfile = 'shelve.data'
    accountdb = s.open(accountfile, 'c')
    accountdb['data'] = db
    accountdb.close()

    accountdb = s.open(accountfile, 'r')
    print accountdb['data']


def adminlogin():
    while True:
        name = raw_input('login name desired: ').lower()
        if not name.isalnum() and '' in name:
            print 'name format error'
            continue
        else:
            pwd = raw_input('login passwd desired: ')
            if name == 'root' and pwd == 'root':
                print 'welcom admin'
                break
            else:
                print 'user name or passwd is wrong,input again'
    if len(db) == 0:
        print 'there is nothing you can do'
    else:
        answer = raw_input('output all account? y/n').lower()
        if 'y' == answer:
            # output_use_file()
            output_use_pickle()
            # output_use_shelve()
        elif 'n' == answer:
            print 'bye'


def showmenu():
    prompt = """
    (A)dmin Login
    (U)ser Login
    (R)emove a existing user
    (Q)uit
     Enter choice:"""

    done = False
    while not done:
        chosen = False
        while not chosen:
            try:
                choice = raw_input(prompt).strip()[0].lower()
            except (EOFError, KeyboardInterrupt):
                choice = 'q'
            print '\nYou picked: [%s]' % choice
            if choice not in 'aurq':
                print 'invalid option,try again'
            else:
                chosen = True

        if choice == 'q':
            done = True
        if choice == 'r':
            removeuser()
        if choice == 'u':
            userlogin()
        if choice == 'a':
            adminlogin()


if __name__ == '__main__':
    showmenu()
