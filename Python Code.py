# Create all essential lists/dictionary
inputTextList=[]
outputTextList=[]
cChars=[]
cShortBinary=[]
cLongBinary=[]

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

# Print the key of that value
print (getkey("0110011"))
