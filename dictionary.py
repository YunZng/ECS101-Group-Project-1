inputTextList=[]
outputTextList=[]
compressionChars=[]
compressionShortBinary=[]
compressionLongBinary=[]
counter = 0


my_file = open(input("Enter file name: (example.txt):  "))
inputTextList = my_file.read()
#inputType=int(input("What are you trying to do?\n(1)Text to binary\n(2)Binary to text\n"))

for i in range (64):
	compressionLongBinary.append("{0:{fill}7b}".format(i,fill="0"))
temp = 0
Dlist = {}
for x in range(26):
   # print(compressionLongBinary[x])
    print(chr(x+97))
    Dlist[chr(x+97)] = compressionLongBinary[x] 
    print(Dlist[chr(x+97)]) # to test out if the keys and values are actually in the dictionary verbosely 

for y in range(27, 53, 1):
    print(chr(y+38))
    Dlist[chr(y+38)] = compressionLongBinary[y-1]
    print(Dlist[chr(y+38)]) # to test out if the keys and values are actually in the dictionary verbosely 


#Mods to the ASCII ordered dictionary 
#Dlist[character] = bit value 

