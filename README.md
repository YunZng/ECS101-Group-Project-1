# ECS101-Group-Project-1
Lahray, Yulun, Sydney, Yuyuan
Yulun: I have commented all the codes, every line of the code. Explained the meaning behind each line to my teammates. 

Our program first initialize a bunch of lists and a dictionary.
The following steps are done in a loop.
	The lists are used to input long and short binary numbers, they will be useful when matching with the characters. 
	The dictionary is used to match characters to their corresponding binary.
The next step is to put everything needed to adjust in two separate lists, with each character in one list corresponds to the binary in another list.
Using a for loop, all of the values in can be updated easily.
Next, ask the user to input their file name, then select a mode, either to convert binary to character or character to binary, for selection just put in the number of the give option.
If the user chose to convert binary to string, then the program will convert segments of the binary one by one, starting with the very first index, convert and generate output as it progresses. 
If the user chose to convert string to binary, then the program will start from the first index of the string and try the maximum length of the string in dictionary to minimum length, check if that segment exists in the dictionary, if yes, then it will add the corresponding binary to the output.

Instruction for this program is not necessary.
Total lines: 77 lines
Comments: 28 lines
Code: 49 lines
