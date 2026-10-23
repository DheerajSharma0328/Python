f = open("/home/dheeraj-sharma/1. All Mighty Push/10.Python/01.helloworld.py")
data = f.read()
print(data)
f.close()

# open take two argument 1. File Path 2.Operation on file 
# By default operation is read i.e "r" we do not need to write it explicitly
# Second is write to make a file writable we can write "w" as second argument

# once a line is readed it is not again read by the readline or readlines again
# once all the lines are readed and if we stll use readline it return "" empty string
# print("checking line 7 output: ", lines7 == "") ===> Output ==>True

# And we no line left and we use readlines it return empty list
# print("checking line 6 output: ", lines6 == []) ===> Output ==>True

str = "I am create a file name myfiles.txt from 23.files_io.py and this is the string i am copying into it"
mydata = open("myfiles.txt", "w")
mydata.write(str)
mydata.close()

newfile = open("/home/dheeraj-sharma/1. All Mighty Push/newfile.txt")
# readline line read only one line and return string
lines1 = newfile.readline()
lines2 = newfile.readline()
lines3 = newfile.readline()
lines4 = newfile.readline()
# readliines read all the line in the file and return a list of all line
lines5 = newfile.readlines()
lines6 = newfile.readlines()
lines7 = newfile.readline()
print("Line1: ", lines1)
print("Line2: ", lines2)
print("Line3: ", lines3)
print("Line4: ", lines4)
print("Line5: ", lines5)
print("Line6: ", lines6)
print("Line7: ", lines7)
print("checking line 5 output: ", lines5 == [])
print("checking line 6 output: ", lines6 == [])
print("checking line 7 output: ", lines7 == "")
print("Checking Readline Output: ", type(lines1))
print("Checking Readlines Output: ", type(lines6))
newfile.close()


whilefile = open("/home/dheeraj-sharma/1. All Mighty Push/newfile.txt")
i = 1
newfileline = whilefile.readline()
# Printing line using while loop

while(newfileline != ""):
    print(f"While Loop line {i}: {newfileline}")
    newfileline = whilefile.readline()
    i += 1

f.close()