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
	return "No such thing"

# Add all the long binary to the list
for i in range (64):
	cLongBinary.append("{0:{fill}7b}".format(i,fill="0"))

# Add all the lower case letters to the list
for x in range(26):
    dList[cLongBinary[x]] = chr(x+97)

# Add all the upper case letter to the list
for y in range(27, 53, 1):
    dList[cLongBinary[y-1]] = chr(y+38)

# Add the short bits 
for i in range (32):
	cShortBinary.append("1"+"{0:{fill}5b}".format(i,fill="0"))

# First put all the long binary to adjust
blist = ["0000000", "0000010", "0000011", "0000100", "0001000", "0001011","0001101","0001110", "0010001", "0010010", "0010011", "0010100"]
for z in range(52, 64):
    blist.append(cLongBinary[z])

blist.extend(cShortBinary)
# Then put all the values to be assigned to the long binary
clist = ["at", "she", "as", "by", "on", "her", "but", "from", "not", "his", "say", "they", ".", ",", "then", "\'", "\"", "\n", "-", "!", "use", "do", "have", "are", "the", "be", "to", "of", " ", "in", "a", "or", "it", "for", "r", "this", "e", "he", "you", "d", "and", "that", "i", "n", "s", "with", "o", "u", "we", "t", "l", "c", "ate", "ear", "ed", "ion"]

# Replace the definition of the existing binary
for i in range (len(blist)):
	dList[blist[i]]=clist[i]

# Create the short bits

# Add all the short binary and phrases
slist = []
# Print all the items in matching order
for a, b in dList.items():
    print (a,b)
print("")

# Ask for file name
file=input("What is your file name? (Example: type name for name.txt)")
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
		if sIndex>len(myString)-6:
			break
		elif myString[sIndex]=="1":
			outputTextList.append(dList.get(myString[sIndex:sIndex+6]))
			sIndex+=6
		elif myString[sIndex]=="0":
			outputTextList.append(dList.get(myString[sIndex:sIndex+7]))
			sIndex+=7
elif ask == "2":
	# Set a list of number corresponding to the index of each letter
	checkRemain=list(range(len(myString)))
	print (checkRemain)
	for length in range (5,0,-1):
		for key, value in dList.items():
			if len(value)==length:
				for x in range(len(myString)):
					if myString[x:x+length]==value and x in checkRemain and x+length-1 in checkRemain:
						print(value)
						wList[x]=getkey(value)
						print(checkRemain)
						for n in range(x,x+length):
							print(n)
							checkRemain.remove(n)

for a, b in sorted(wList.items()):
    print(a,b)
for a, b in sorted(wList.items()):
    outputTextList.append(b)
# Print the outputTextList
print(outputTextList)

# Joins all the pieces in the output list into one single string
print(''.join(outputTextList))
