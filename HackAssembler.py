"""

HACK COMPILER FOR THE HACK ASSEMBLY LANGUAGE

COMPILES A HACK ASSEMBLY LANGUAGE FILE TO A MACHINE CODE FILE


CREATED BY KIRAN SURENDRAN
ON THE 11TH OF JANUARY 2019

"""

hack_filename = input("Enter the desired HACK assembly file");		#Get file name as input

with open("{}.asm".format(hack_filename)) as hack_file:
	content = hack_file.readlines()

#print(len(content))

second_input = []						 	#Initializes a varaible called second_out that will hold the results of the first loop
final_out = []								#Initialize a variable called final_out that will be a list of the output code
curr_line = 0								#Initialize line count
line_count = 0
table = {"R0" : 0, "R1" : 1, "R2" : 2,  "R3" : 3, "R4" : 4, "R5" : 5, "R6" : 6, "R7" : 7, "R8" : 8, "R9" : 9, "R10" : 10, "R11" : 11, "R12" : 12, "R13" : 13, "R14" : 14, "R15" : 15, "SCREEN" : 16384, "KBD" : 24576, "SP" : 0, "LCL" : 1, "ARG" : 2, "THIS" : 3, "THAT" : 4}
next_var = 16
noNewValue = False
#FUNCTIONS

#converts a decimal string to a binary string with a length of 15 bits
def to_binary(num):
	bin = str("{0:b}".format(int(num)))
	while (len(bin) < 15):
		bin = "0" + bin
	return bin
#FUNCTIONS END



#First Loop: Clean Up and Symbol Handling
#Remove whitespaces and some comments

for i in content:							#Loop through every line of code
	#print("line: {}\n".format(i))

	if (i.isspace()):						#Check if a line is empty (whitespace)
		continue						#Continues back to the top of the loop


	if (i[0] + i[1] == "//"):
		continue
	if ("//" in i):
		comment_i = i.find("//")
		i = i[0:comment_i]
		second_input.append(i.replace("\n", "")) 						#Appends current line to first loop output array
		line_count += 1							#Increment Line count
		curr_line += 1							#Increment Current line
		continue

	i = i.replace(" ", "")
	i = i.replace("\t", "")
	i = i.replace("\n ", "")
	if (i[0] == "@"):
		symbol = i[1:]
		symbol = symbol.replace("\n", "")
		try:
			test = int(symbol)
			second_input.append(i) 						#Appends current line to first loop output array
			line_count += 1							#Increment Line count
			curr_line += 1							#Increment Current line
			continue
		except ValueError:
			"""
			for h in table:
				if(h==symbol):
					noNewVar = True
					second_input.append(i) 						#Appends current line to first loop output array
					break
			if (not noNewVar):
				symbol = symbol.replace("(" ,"")
				symbol = symbol.replace(")","")
				symbol = symbol.replace("\n","")
				table[symbol] = next_var
				next_var += 1
				second_input.append(i) 						#Appends current line to first loop output array
			noNewVar = False
			"""
			i = i.replace("\n", "")
			second_input.append(i) 						#Appends current line to first loop output array
			line_count += 1							#Increment Line count
			curr_line += 1							#Increment Current line
			continue

	if(i[0] == "("):
		label = i
		label = label.replace("(" ,"")
		label = label.replace(")","")
		label = label.replace("\n","")
		table[label] = curr_line
		continue
		#second_input.append("@" + label) 						#Appends current line to first loop output array

	if (True):
		second_input.append(i.replace("\t", "")) 						#Appends current line to first loop output array
		line_count += 1							#Increment Line count
		curr_line += 1							#Increment Current line



#print(second_input)
for i in second_input:
	#print("yeetus")
	noNewValue = False
	i = i.replace(" ", "")
	i = i.replace("\n", "")
	inst = i
	#print("Current Instruction: {}\n".format(inst))
	if(i[0] == "@"):						#A-Type Instruction
		#print("A-type instruction")
		aValue = i[1:]
		aValue = aValue.replace("\n", "")
		try:
			test = int(aValue)
			binNum = to_binary(aValue)
			finInst= "0" + str(binNum)
			final_out.append(finInst)
			continue
		except ValueError:
			for h in table:
				if aValue == h:
					aInstVal = table[aValue]
					aInstVal = to_binary(aInstVal)
					finInst= "0" + str(aInstVal)
					final_out.append(finInst)
					noNewValue = True
			if (not noNewValue):
				aValue = aValue.replace("\n","")
				table[aValue] = next_var
				next_var += 1
				binA = to_binary(table[aValue])
				final_out.append("0" + binA) 						#Appends current line to first loop output array
			noNewVar = False

	else:
		inst = i.replace("\t", "")
		#print("C-type instruction")				#C-Type Instruction
		aBit = "0"
		cBits = "000000"
		destBits = "000"
		jumpBits = "000"

		if ("=" in inst):						#Destination Instruction
			#print("Above instruction is a Destination instruction\n\n\n")
			dest = inst.split("=")
			arrDest = []
			#Calculating Destination bits

			if ("A" in dest[0]):
				arrDest.append(1)
			else:
				arrDest.append(0)
			if ("D" in dest[0]):
				arrDest.append(1)
			else:
				arrDest.append(0)
			if ("M" in dest[0]):
				arrDest.append(1)
			else:
				arrDest.append(0)
			destBits = ''.join(str(e) for e in arrDest)

			if(True):
				comp = dest[1]
				if ("M" in comp):
					aBit = "1"
				#Comp logic
				if(comp == "0"):
					cBits="101010"
				elif(comp == "1"):
					cBits="111111"
				elif(comp =="-1"):
					cBits="111010"
				elif(comp == "D"):
					cBits="001100"
				elif( (comp == "A") or (comp == "M")):
					cBits = "110000"
				elif (comp == "!D"):
					cBits = "001101"
				elif((comp=="!A") or (comp=="!M")):
					cBits = "110001"
				elif(comp == "-D"):
					cBits = "001111"
				elif((comp=="-A") or (comp=="-M")):
					cBits = "110011"
				elif(comp == "D+1"):
					cBits = "011111"
				elif((comp=="A+1") or (comp=="M+1")):
					cBits = "110111"
				elif(comp=="D-1"):
					cBits = "001110"
				elif((comp=="A-1") or (comp=="M-1")):
					cBits = "110010"
				elif((comp=="D+A") or (comp=="D+M")):
					cBits = "000010"
				elif((comp=="D-A") or (comp=="D-M")):
					cBits = "010011"
				elif((comp=="A-D") or (comp=="M-D")):
					cBits = "000111"
				elif((comp=="D&A") or (comp=="D&M")):
					cBits = "000000"
				elif((comp=="D|A") or (comp=="D|M")):
					cBits = "010101"
			instruction = ("111" + aBit + cBits + destBits + jumpBits)
			final_out.append(instruction)

		if(";" in inst):								#Jump Instruction
			#print("Above instruction is a Jump instruction\n\n\n")
			new_inst = inst.split(";")
			jump = new_inst[1]

			if(jump == "JGT"):
				jumpBits = "001"
			elif(jump == "JEQ"):
				jumpBits = "010"
			elif(jump == "JGE"):
				jumpBits = "011"
			elif(jump == "JLT"):
				jumpBits = "100"
			elif(jump == "JNE"):
				jumpBits = "101"
			elif(jump == "JLE"):
				jumpBits = "110"
			elif(jump == "JMP"):
				jumpBits = "111"

			if(True):
				comp = new_inst[0]
				if ("M" in comp):
					aBit = "1"

				#Comp logic

				if(comp == "0"):
					cBits="101010"
				elif(comp == "1"):
					cBits="111111"
				elif(comp =="-1"):
					cBits="111010"
				elif(comp == "D"):
					cBits="001100"
				elif( (comp == "A") or (comp == "M")):
					cBits = "110000"
				elif (comp == "!D"):
					cBits = "001101"
				elif((comp=="!A") or (comp=="!M")):
					cBits = "110001"
				elif(comp == "-D"):
					cBits = "001111"
				elif((comp=="-A") or (comp=="-M")):
					cBits = "110011"
				elif(comp == "D+1"):
					cBits = "011111"
				elif((comp=="A+1") or (comp=="M+1")):
					cBits = "110111"
				elif(comp=="D-1"):
					cBits = "001110"
				elif((comp=="A-1") or (comp=="M-1")):
					cBits = "110010"
				elif((comp=="D+A") or (comp=="D+M")):
					cBits = "000010"
				elif((comp=="D-A") or (comp=="D-M")):
					cBits = "010011"
				elif((comp=="A-D") or (comp=="M-D")):
					cBits = "000111"
				elif((comp=="D&A") or (comp=="D&M")):
					cBits = "000000"
				elif((comp=="D|A") or (comp=="D|M")):
					cBits = "010101"
			instruction = ("111" + aBit + cBits + destBits + jumpBits)
			final_out.append(instruction)
		line_count += 1							#Increment Line count
		curr_line += 1							#Increment Current line


#print(final_out)


f = open("{}.hack".format(hack_filename), "w+")
for i in final_out:
	f.write((i + "\n"))
f.close()


print("\n\n\n\n\n\n")
print(table)
