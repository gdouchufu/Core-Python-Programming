def myopen(path, access='r'):
    try:
        f = open(path, access)
    except (IOError, ValueError):
        return None
    return f

if __name__ == '__main__':
    print myopen("test.txt", 'abc')