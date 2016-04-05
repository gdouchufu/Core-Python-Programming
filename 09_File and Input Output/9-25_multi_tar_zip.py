import tarfile
import zipfile
import os

def extract(path, filename):
    if filename.endswith('.zip'):
        with zipfile.ZipFile(filename, 'r') as f:
            f.extractall(path)
    elif filename.endswith(('.tgz', '.tar.gz', '.bz2', '.tbz', 'tar')):
        with tarfile.open(filename, 'r') as f:
            f.extractall(path)

def decompress(target, *files):
    if not os.path.exists(target):
        os.mkdir(target)
    extract(target, files[0])
    for name in files[1:]:
        dirname = os.path.splitext(os.path.basename(name))[0]
        dirname = '.\\' + target + '\\' + dirname
        os.mkdir(dirname)
        extract(dirname, name)

if __name__ == '__main__':
    os.chdir(r'.\wx')
    decompress('test', 'test.zip', 'test2.tar.gz', 'test.tar.bz2')
