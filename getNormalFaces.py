filename = input("enter obj file name with .obj: ");
output = open("normalfaces.txt","w+")
input = open(filename, "r")

value = []
prevChar = ''
flag = 1
for line in input: 
	if (line[2] == 'C'):
		output.write("\n%s" % line)
	if (line[0] == 'f'): 
		for character in line:
			if (character != ' ' and character != 'f' and flag == 0 and character != '/' and character != '\n'):
				output.write("%s" % character)
			if (character == ' ' and prevChar != 'f' or character == '\n'):
				output.write(",")
			if (character == '/' and prevChar == '/'):
				flag = 0
			if ((flag == 0 and character == '\n') or (flag == 0 and character == ' ') ):
				flag = 1
				
			prevChar = character
		