import os
file_path = "D:/test/test.py"
(filepath,tempfilename) = os.path.split(file_path)
(filename,extension) = os.path.splitext(tempfilename)
print(filename)