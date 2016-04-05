def copyfile(src, dst):
    with open(dst, 'a') as f:
        with open(src) as s:
            for item in s:
                f.write(item)

if __name__ == '__main__':
    src = raw_input('copy from: ')
    dst = raw_input('copy to: ')
    copyfile(src, dst)