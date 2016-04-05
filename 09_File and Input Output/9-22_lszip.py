import zipfile, os, time

filename = raw_input('zip file name:')
print 'zip file size: %d bytes' % (os.stat(filename).st_size)

z = zipfile.ZipFile(filename, 'r')
print 'filename\tdatetime\tsize\tcompress size\trate'
for info in z.infolist():
    t = time.ctime(time.mktime(tuple(list(info.date_time) + [0, 0, 0])))
    print '%s\t%s\t%d\t%d\t%.2f%%' % (
    info.filename, t, info.file_size, info.compress_size, float(info.compress_size) / info.file_size * 100)

z.close()
