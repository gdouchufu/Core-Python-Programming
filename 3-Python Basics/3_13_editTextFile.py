#!/usr/bin/env python
import os

print "************ Text File Editor ************"
print

line_sum = 0;
all_content = []

# get filename
while True:
    try:
        fname = raw_input('>>> enter filename: ')
        fobj = open(fname, 'r')
        break
    except IOError, e:
        print '>>> [ERROR] file open failed:', e

# get original content
for line in fobj.readlines():    
    all_content.append(line) 
    print line,
    line_sum += 1

def get_new_content():
    while True:
        choose_line_num = raw_input('>>> select one line to edit [1-%d] : ' % line_sum)
        try:
            choose_line_num = int(choose_line_num)
            if not (0 < choose_line_num <= line_sum):
                print '>>> [ERROR] the line number must in [1-%d] !' % line_sum
                continue
            break
        except ValueError, e:
            print '>>> [ERROR] number transform failed: ', e

    print '>>> your choose line is : %d' % choose_line_num
    new_content = raw_input('>>> input new content: ')
    all_content[choose_line_num-1] = new_content + os.linesep

# generate new content
if line_sum > 0:
    get_new_content()
else:
    print '>>> the file is empty, please input new content directly:'
    new_content = raw_input('>>> ')
    all_content.append(new_content)

# save new content
fobj = open(fname, 'w')
for line in all_content:
    fobj.write(line)
fobj.close()
print '>>> save success, bye!'