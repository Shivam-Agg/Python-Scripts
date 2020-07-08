import os

#Directory path where files are to be renamed
dirpath = 'C:\\path\\to\\directory'

count = 1

for filename in os.listdir(dirpath):
    newFile = 'File_' + str(count) + os.path.splitext(filename)[1]
    src = os.path.join(dirpath, filename)
    dest = os.path.join(dirpath, newFile)
    os.rename(src, dest)
    count+=1