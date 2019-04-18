filename = input("enter obj file name with .obj: ");
output = open("normalvertices.txt","w+")
input = open(filename, "r")

value = []
prevChar = ''
count = 0;
for line in input: 
	if (line[0] == 'v' and line[1] == 'n'): 
		for character in line:
			if (character == '\n'):
				output.write("),")
			if (character != ' ' and character != 'n' and character != 'v'):
				output.write("%s" % character)
			if (character == ' ' and prevChar == 'n'):
				output.write("vec3(");
			if(character == ' ' and prevChar != 'n' ):
				output.write(",")
				count += 1;
			prevChar = character
