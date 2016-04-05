import zipfile

def create_zipfile(zipname, filename1, filename2):
    z = zipfile.ZipFile(zipname, 'w')
    z.write(filename1)
    z.write(filename2)
    z.close()

def add_zipfile(zipname, filename):
    z = zipfile.ZipFile(zipname, 'a')
    z.write(filename)
    z.close()

def extract_zipfile(zipname, filename):
    z = zipfile.ZipFile(zipname, 'r')
    z.extract(filename)
    z.close()

def zipfile_filelist(zipname):
    z = zipfile.ZipFile(r'test.zip', 'r')
    z.printdir()
    z.close()

if __name__ == '__main__':
    create_zipfile(r'test.zip', r'test.txt', r'test1.txt')
    add_zipfile(r'test.zip', r'test2.txt')
    extract_zipfile(r'test.zip', r'test1.txt')
    zipfile_filelist(r'test.zip')

