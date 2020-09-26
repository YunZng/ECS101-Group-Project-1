# Create all essential lists/dictionary
inputTextList=[]
outputTextList=[]
cChars=[]
cShortBinary=[]
cLongBinary=[]

# This is dictionary, it is a good way to match one value to another, a : 'b', now a has the value 'b'
dList = {}

# Create a function that fetches the key of a value
# Print the key of that value:  print(getkey("0110011"))
def getkey(want):
	for key, value in dList.items():
		if value == want:
			return key
	return "No such thing"

#call this func to print the whole library
def printalldic(dList): 
    for a, b in dList.items():
       print (a,b)
    print("")

def printList(l): 
    for i in range(len(l) -1):
        print(l[i])

# Add all the long binary to the list
for i in range (64):
	cLongBinary.append("{0:{fill}7b}".format(i,fill="0"))
# add the short bits 
for i in range (32):
	cShortBinary.append("{0:{fill}5b}".format(i,fill="0"))


# Add all the lower case ascii letters to the list
for x in range(26):
    dList[chr(x+97)] = cLongBinary[x]
# Add all the upper case ascii letter to the list
for y in range(27, 53, 1):
    dList[chr(y+38)] = cLongBinary[y-1]
# Print all the items in matching order
#------------------------------------------------------
#mods to the ascii ordered compression table: 
blist = ["0000000", "0000010", "0000011", "0000100", "0001000", "0001011","0001101","0001110", "0010001", "0010010", "0010011", "0010100"]
for z in range(52, 64, 1):
    blist.append(cLongBinary[z])
clist = [" that ", " she ", " you ", " with ", " this ", " her ", " but ", " from ", " not ", " his ", " say ", " they ", ".", ",", " then ", "\'", "\"", "\n", "-", "!", " the ", " and ", " have ", " are "]
temp = []

for i in range(len(blist)-1): 
    for k, v in dList.items():
        if v == blist[i]: 
            temp.append(k)

for i in range(len(temp)-1):
   dList[clist[i]] = dList[temp[i]]
   del dList[temp[i]]

for i in range(13,24,1):
    dList[clist[i]] = blist[i]

slist = ["use", " be ", " to ", " of ", " ", " in ", "a", " or ", " it ", " for ", "r", " on ", "e", " he ", " as ", "d", " do ", " at ", "i", "n", "s", " by ", "o", "u", " we ", "t", "l", "c", "ate", "ear", "ed", "ion"]
for i in range(len(cShortBinary)):
    dList[slist[i]] = "1"+ cShortBinary[i]
#-----------------------------------------------------

def makeReadFile(): #this function reads the input file and 
    #return the list of chars
    my_file = open(input("Enter file name: (example.txt):  "))
    inputTextList = my_file.read()
    if len(inputTextList) == 0:
        print("Read failed; TXT file wrong or empty")
    else:
        print("Read successful; now returning binary... \n")
        return inputTextList

inputTextList = makeReadFile()

#this collects all the special phrases that 
# are not single chars into a list
specialStr = []
for item in clist:
    if len(item) > 1:
        specialStr.append(item)
for item in slist:
    if len(item) > 1:
        specialStr.append(item)


for item in inputTextList:
    print(item, dList[item])
