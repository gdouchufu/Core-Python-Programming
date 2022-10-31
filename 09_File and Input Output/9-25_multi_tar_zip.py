import tarfile
import zipfile
import os

def extract(path, filename):
    if filename.endswith('.zip'):
        with zipfile.ZipFile(filename, 'r') as f:
            f.extractall(path)
    elif filename.endswith(('.tgz', '.tar.gz', '.bz2', '.tbz', 'tar')):
        with tarfile.open(filename, 'r') as f:
            def is_within_directory(directory, target):
                
                abs_directory = os.path.abspath(directory)
                abs_target = os.path.abspath(target)
            
                prefix = os.path.commonprefix([abs_directory, abs_target])
                
                return prefix == abs_directory
            
            def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
            
                for member in tar.getmembers():
                    member_path = os.path.join(path, member.name)
                    if not is_within_directory(path, member_path):
                        raise Exception("Attempted Path Traversal in Tar File")
            
                tar.extractall(path, members, numeric_owner=numeric_owner) 
                
            
            safe_extract(f, path)

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
