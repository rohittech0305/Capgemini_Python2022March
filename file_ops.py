'''
Modes:
r (read)-> To open the file for reading. If the file does not exists then we will get
        FileNotFound Error.
w (write) -> To open the file to write. If the file is not there, then it will
            create the file and write into it. if the file is there, then it will
            cleanup existing file content and start write as a fresh file
a (append) -> To open the file to write along with the existing content. If the
            file is there it will start appending to the existing data. if the
            file is not there it will create ana write into it
r+(read-wrire) -> open the file for both read and write.
                    First we must read the existing content and start writing into
                    it at the end of the line

w+ (write-read) -> if the exists already the existing content will get removed
                and only the new content gets written. and we can also read
                whatever we have written now
rb (read binary data) -> non text data (image, audio, video)
wb (write binary data) -> non text data (image, audio, video)

'''
#READ
    #readline, readlines, read
# with open("days.txt",'r') as fo:
#     #print(fo.read())
#     #print(fo.readline(),end='')
#     #print(fo.readline())
#     for day in fo.readlines()[1:-1]:
#         print(day.upper(),end='')

#WRITE, APPEND
#write,writelines

# with open("myfile.txt","w") as fo:
#     fo.writelines(["PYTHON\n","SPARK\n","MACHINE LEARNING\n","AWS\n","SNOWFLAKES\n","SQL\n"])

# with open("myfile.txt","a") as fo:
#     fo.writelines(["PYTHON\n","SPARK\n","MACHINE LEARNING\n","AWS\n","SNOWFLAKES\n","SQL\n"])

# with open("myfile_new.txt","r+") as fo:
#     fo.write("END OF THE FILE")
#     fo.seek(0,0)
#     print(fo.read())

# with open("days.txt","w+") as fo:
#     fo.writelines(["ROHIT\n","Pallavi\n","Chandra\n","Aveek\n","BILAL\n"])
#     fo.seek(0,0)
#     print(fo.read())

# with open(r"D:\Users\rkandasamy\Pictures\puppy.jpg","rb") as fo:
#     with open(r"D:\Users\rkandasamy\Pictures\mypet.jpg","wb") as wfo:
#         wfo.write(fo.read())