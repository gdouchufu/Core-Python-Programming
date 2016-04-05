import gzip

def compress(zipfile, filename):
    obj = gzip.open(zipfile, 'wb')
    with open(filename, 'rb') as f:
        obj.writelines(f)
    obj.close()

def decompress(zipfile, filename):
    obj = gzip.open(zipfile, 'rb')
    content = obj.read()
    with open(filename, 'wb') as f:
        f.write(content)

if __name__ == '__main__':
    compress('compress.gzip', 'test.txt')
    decompress('compress.gzip', 'decompress.txt')
