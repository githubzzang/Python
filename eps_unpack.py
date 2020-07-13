import os, zlib, sys

def filename() :
        file_list_eps = [file for file in os.listdir() if file.endswith(".eps")]
        return(''.join(file_list_eps))

count = filename().count('.eps')
if count > 1 :
        print("\nOlny One File_(.eps)\n")
        os.system("pause")
        
elif count == 1 :
        obj1 = open(filename(), 'rb').read()
        obj2 = zlib.decompress(obj1, -15)
        file = open('unpack', 'wb')
        file.write(obj2)
        
else :
        print("\nPath Check\n")
        os.system("pause")
