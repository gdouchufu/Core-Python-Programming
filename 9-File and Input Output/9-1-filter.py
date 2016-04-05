f = open('test.txt')
for line in f:
    if line is not None and line[0] != '#':
        print line,

