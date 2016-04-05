passwdList = ['aaaa', 'bbb', 'cccc']
valid = False
count = 3
while count > 0:
    input = raw_input("enter password: ")
    # check for valid passwd
    for eachPasswd in passwdList:
        if input == eachPasswd:
            valid = True
            break
    if not valid:    # (or valid == 0)
        print ">>ERROR: invalid input"
        count -= 1
        continue
    else:
        print ">>INFP: password correct!"
        break
