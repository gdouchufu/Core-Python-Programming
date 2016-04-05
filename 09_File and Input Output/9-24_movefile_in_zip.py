import tarfile
import zipfile
import os

def movefile(src, dst, filename):
    if src.endswith('.zip') and dst.endswith(('.tar.gz', '.tgz', '.tbz', '.tar.bz2')):
        zipobj = zipfile.ZipFile(src, 'r')
        content = zipobj.read(filename)
        zipobj.close()

        with open(filename, 'w') as f:
            f.write(content)

        tar = tarfile.open(dst, 'r')
        ls = tar.getnames()
        tar.extractall()
        tar.close()

        mode = 'w:gz' if dst.endswith(('tar.gz', '.tgz')) else 'w:bz2'
        tar = tarfile.open(dst, mode)
        for name in ls + [filename]:
            tar.add(name)
            os.remove(name)
        tar.close()
    elif src.endswith(('.tar.gz', '.tgz', '.tbz', '.tar.bz2')) and dst.endswith('.zip'):
        tar = tarfile.open(src, 'r')
        tar.extract(filename)
        tar.close()

        zipobj = zipfile.ZipFile(dst, 'a')
        zipobj.write(filename)
        zipobj.close()
        os.remove(filename)

if __name__ == '__main__':
    movefile(r'test.zip', r'test2.tar.gz', r'test2.txt')
    movefile(r'test2.tar.gz', r'test.zip', r'test2.txt')
