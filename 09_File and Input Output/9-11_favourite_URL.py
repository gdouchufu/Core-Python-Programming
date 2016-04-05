import re, os

def checkurl(url):
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    if regex.match(url):
        return True
    else:
        return False

def geturl():
    name = raw_input('pls input a url name:')
    while 1:
        url = raw_input('pls input a url address:')
        if checkurl(url):
            break
        else:
            print 'wrong url format,pls input again'
    mark = raw_input('pls input a url mark:')
    folder = raw_input('pls input a url folder:')
    return (name, url, mark, folder)

def load(filename):
    f = open(filename, 'a+')
    bmlist = f.readlines()
    f.close()
    return bmlist

def save(bmlist, filename):
    f = open(filename, 'w+')
    for line in bmlist:
        if len(line) == 0:
            continue
        f.write(line)
    f.close()

def add(bmlist, name, url, mark, folder='default'):
    bookmark = name + ';' + url + ';' + mark + ';' + folder + os.linesep
    if bookmark not in bmlist:
        bmlist.append(bookmark)

def modify(bmlist, index, name, url, mark, folder):
    bmlist[index] = name + ';' + url + ';' + mark + ';' + folder + os.linesep

def delbm(bmlist, index):
    bmlist.pop(index)

def findbk(bmlist, fname, furl):
    for i, item in enumerate(bmlist):
        (name, url, mark, folder) = item.split(';')
        if fname and furl:
            if (fname in name) and (furl in url):
                return i
        if fname and (fname in name):
            return i
        if furl and (furl in url):
            return i
    else:
        return -1

def output2html(bmlist):
    for i, item in enumerate(bmlist):
        (name, url, mark, folder) = item.split(';')
        os.mkdir(folder.strip())
        filename = name.strip() + '.html'
        f = open(filename, 'w+')
        fmt = '%d\t%s\t<a href=%s>%s</a>\t%s\t%s<br>'
        f.write('<html><head><title>bookmark</title></head><body>')
        content = fmt % (i + 1, name, r'http:\\' + url, url, mark, folder)
        f.write(content)
        f.write('</body></html>')
        f.close()
        os.rename(filename, folder.strip() + os.sep + filename)

def show_menu():
    bmlist = load(r'url.txt')
    while True:
        print '0. quit'
        print '1. add a url bookmark'
        print '2. modify a url bookmark'
        print '3. delete a url bookmark'
        print '4. find a url bookmark'
        print '5. output url bookmark as html'
        print '\n'

        iInput = input("please input operation num: ")

        if iInput < 0 or iInput > 5:
            print 'Error input operation, try again.\n'
            continue
        elif 0 == iInput:
            save(bmlist, r'url.txt')
            break
        elif 1 == iInput:
            data = geturl()
            add(bmlist, *data)
        elif 2 == iInput:
            index = int(raw_input('bookmark index:'))
            data = geturl()
            modify(bmlist, index, *data)
        elif 3 == iInput:
            index = int(raw_input('bookmark index:'))
            delbm(bmlist, index)
        elif 4 == iInput:
            name = raw_input('url name:')
            url = raw_input('url address:')
            index = findbk(bmlist, name, url)
            if index == -1:
                print 'not found'
            else:
                print bmlist[index]
        elif 5 == iInput:
            output2html(bmlist)

if __name__ == '__main__':
    show_menu()


