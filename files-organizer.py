import os
import shutil

#Path to directory containing the files
dirpath = 'C:\\path\\to\\directory'

try:
    files = os.listdir(dirpath)
    for filename in files:
        #Checks if it is a file or folder
        if os.path.isfile(os.path.join(dirpath, filename)):
            extension = os.path.splitext(filename)[1][1:]
            folderPath = os.path.join(dirpath, extension)
            filePath = os.path.join(folderPath, filename)

            #Check if a folder already exists for the given file type
            if os.path.exists(folderPath):
                shutil.move(os.path.join(dirpath, filename), filePath)
            else:
                os.mkdir(os.path.join(dirpath, extension))
                shutil.move(os.path.join(dirpath, filename), filePath)
except:
    print('Directory doesn\'t exist')
