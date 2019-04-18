filename = input("enter obj file name with .obj: ");
output = open("vertices.txt","w+")
input = open(filename, "r")

value = []
prevChar = ''
count = 0;
for line in input: 
	if (line[0] == 'v' and line[1] != 't' and line[1] != 'n'): 
		for character in line:
			if (character == '\n'):
				output.write("),")
			if (character != ' ' and character != 'v'):
				output.write("%s" % character)
			if (character == ' ' and prevChar == 'v'):
				output.write("vec3(");
			if(character == ' ' and prevChar != 'v' ):
				output.write(",")
				count += 1;
			prevChar = character
