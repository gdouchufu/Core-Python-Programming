num = int(raw_input('Enter total number of names: '))
i = 0
error_count = 0
names = []
while i < num:
    name = raw_input('Please enter name %d: ' % i)
    if ', ' not in name:
        print '>> Wrong format... should be Last, First.'
        error_count += 1
        print '>> You have done this %d time(s) already. Fixing input. . .' % error_count
        nameTmp = name.split()
        name = nameTmp[0] + ', ' + nameTmp[1]
    names.append(name)
    i += 1
else:
    print 'The sorted list (by last name) is:'
    names.sort()
    for name in names:
        print '\t%s' % name