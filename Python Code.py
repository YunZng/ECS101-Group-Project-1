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
    dList[chr(x+97)] = cLongBinary[x]

# Add all the upper case letter to the list
for y in range(27, 53, 1):
    dList[chr(y+38)] = cLongBinary[y-1]

# Print all the items in matching order
for a, b in dList.items():
    print (a,b)
print("")

# Open the text file (input source)
userInput = open("source.txt") 

# Read the file contents into a string
myString = userInput.read()

# Print the input file
print(myString)

# Ask which mode the user prefers
ask = input("Binary to String or String to binary?\n(1)Binary to String\n(2)Character to String\n")

# If answer is 1, then Binary to String, if 0 then otherwise
if ask == "1": 
	# While the string is not fully read, it will keep going, if it detects 1 first, then it will read the next certain digits of binary, same for 0. Then the read piece will be used directly to find the right "key" and add to the outputTextList
	while True:
		if sIndex>len(myString)-7:
			break
		elif myString[sIndex]=="1":
			outputTextList.append(getkey(myString[sIndex:sIndex+6]))
			sIndex+=6
		elif myString[sIndex]=="0":
			outputTextList.append(getkey(myString[sIndex:sIndex+7]))
			sIndex+=7

# Print the outputTextList
print(outputTextList)
# Joins all the pieces in the output list into one single string
print(''.join(outputTextList))
