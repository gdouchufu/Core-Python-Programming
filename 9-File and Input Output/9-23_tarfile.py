import tarfile

def create_tarfile(tarname, filename1, filename2):
    t = tarfile.open(tarname, 'w:bz2')  # w:gz
    t.add(filename1)
    t.add(filename2)
    t.close()

def extract_tarfile(tarname, des_dir):
    t = tarfile.open(tarname, 'r')
    t.extractall(des_dir)
    t.close()

if __name__ == '__main__':
    create_tarfile(r'test.tar.bz2', r'test.txt', r'test1.txt')
    extract_tarfile(r'test.tar.bz2', r'F:\extract_tarfile')