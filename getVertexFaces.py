filename = input("enter obj file name with .obj: ");
output = open("vertexfaces.txt","w+")
input = open(filename, "r")

value = []
prevChar = ''
flag = 0
for line in input: 
	if (line[2] == 'C'):
		output.write("\n%s" % line)
	if (line[0] == 'f'): 
			
		for character in line:
			if (character != ' ' and character != 'f' and flag == 0 and character != '/' and character != '\n'):
				output.write("%s" % character)
			if (character == ' ' and prevChar != 'f' or character == '\n'):
				output.write(",")
			if (character == '/'):
				flag = 1
			if ((flag == 1 and character == ' ') or (flag == 1 and character == '\n')):
				flag = 0
				
			prevChar = character
		