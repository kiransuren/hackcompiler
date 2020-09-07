//Multiplication Program for the Hack Assembly Language
//Created by Kiran Surendran
//On the 5th of January 2019
//Usage: put a number into RAM[0]] and RAM[1] and the result
//       will be stored in RAM[2]

//Variable Declerations

//Load RAM[0] into variable called num
@R0
D=M
@num
M=D

//Load RAM[1] into variable called i
@R1
D=M
@i
M=D

//Load value of 0 to variable called 0
@sum
M=0


(LOOP)
	@i
	D=M
	@END				//Skip to END label if i is equal to 0
	D;JEQ
	
	@num				//Add num to total sum 
	D=M
	@sum
	M=M+D
	
	@i				//Decrement i by 1
	M=M-1	

	@sum				//Put sum into RAM[3]
	D=M
	@R3
	M=D

	@LOOP
	0;JMP

(END)	
	@END
	0;JMP
