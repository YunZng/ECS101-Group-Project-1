# Create all essential lists
inputTextList=[]
outputTextList=[]
cChars=[]
cShortBinary=[]
cLongBinary=[]
# This variable will be used later in the function to help slice the string into smaller pieces
sIndex=0

# This is dictionary, it is a good way to match one value to another, a : 'b', now a has the value 'b'
dList = {}
wList={}

# Create a function that fetches the key of a value
def getkey(want):
	for key, value in dList.items():
		if value == want:
			return key

# Add all the long binary to the list
for i in range (64):
	cLongBinary.append("{0:{fill}7b}".format(i,fill="0"))

# Add the short bits 
for i in range (16):
	cShortBinary.append("1"+"{0:{fill}4b}".format(i,fill="0"))

# Add all the lower case letters to the list
for x in range(26):
    dList[chr(x+97)] = cLongBinary[x]

# Add all the upper case letter to the list
for y in range(27, 53, 1):
    dList[chr(y+38)] = cLongBinary[y-1]

# First put all the long binary to adjust
blist = ["0000000","0000011","0000100","0000111","0001000","0001101","0001110","0010001","0010011"]

# Add the rest of the long binarys from 53 to 64
for z in range(52, 64):
    blist.append(cLongBinary[z])

# Adds adds all the short binary to blist
blist.extend(cShortBinary)
# Then put all the values to be assigned to the long binary blist
clist = ["have","it","that","for","not","on","he","ea","as",".",",","this","\'","\"","\n","-","!","you","do","at","but"," ","e","t","a","o","i","n","h","r","d","the","to","be","ate","and","ion"]

# Replace the definition of the existing binary
for i in range (len(clist)):
	dList[clist[i]]=blist[i]

# Create the short bits

# Add all the short binary and phrases
slist = []
# Print all the items in matching order
for a, b in dList.items():
    print (a,b)
print("")

# Ask for file name
file=input("What is your file name? (Example: type name for name.txt)\n")
# Open the text file (input source)
userInput = open(file+".txt")

# Read the file contents into a string
myString = userInput.read()

# Print the input file
print(myString)

# Ask which mode the user prefers
ask = input("Binary to String or String to binary?\n(1)Binary to String\n(2)String to Binary\n")

# If answer is 1, then Binary to String, if 0 then otherwise
if ask == "1": 
	# While the string is not fully read, it will keep going, if it detects 1 first, then it will read the next certain digits of binary, same for 0. Then the read piece will be used directly to find the right "key" and add to the outputTextList
	while True:
		if sIndex>len(myString)-5:
			break
		elif myString[sIndex]=="1":
			outputTextList.append(getkey(myString[sIndex:sIndex+5]))
			sIndex+=5
		elif myString[sIndex]=="0":
			outputTextList.append(getkey(myString[sIndex:sIndex+7]))
			sIndex+=7
elif ask == "2":
	# Set a list of number corresponding to the index of each letter
	s=0
	outputs=""
	while (s<len(myString)):
		for length in range(4,0,-1):
			if myString[s:s+length] in dList:
				outputs+=dList[myString[s:s+length]]
				s+=length

# Print the outputTextList
print(outputTextList)

# Joins all the pieces in the output list into one single string
if ask=="1":
	print(''.join(outputTextList))
else:
	print(len(outputs),'.',outputs)	
