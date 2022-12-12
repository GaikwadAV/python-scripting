import os

file_exists = os.path.exists("abc.txt")

if file_exists != True:
    # create file using open
    file = open("abc.txt",'w')
    file.write("abcdefg")
    file.close()
    print("file created")
else:
    print("file already exists")


#removing file in current working dir
# os.remove("abc.txt")