//Interactive program that fills the screen when any screen is pressed
//Created by Kiran Surendran
//On the 6th of January 2019


//Keyboard Address
@24576
D=A
@keyboard
M=D


//Screen Address
@16384
D=A
@screen
M=D

//Counter Variable
@i
M=0

//Check if any key on keyboard is being pressed and continue if so
(IF_KEY_PRESSED)
        @i
	M=0	
	@24576
	D=M
	@WHITE_SCREEN
	D;JEQ
	@DARK_SCREEN
	0;JMP

(WHITE_SCREEN)
	
	@8192
	D=A
	@i
	D=D-M
	@IF_KEY_PRESSED	
	D;JEQ

	//Otherwise:
	
	@screen
	D=M
	@i
	A=D+M				//Change to next address
	M=0				//Change pixels to white
	
	@i
	M=M+1				//Increment i

	@WHITE_SCREEN
	0;JMP	
	

(DARK_SCREEN)
	
	@8192
	D=A
	@i
	D=D-M
	@IF_KEY_PRESSED	
	D;JEQ

	//Otherwise:
	
	@screen
	D=M
	@i
	A=D+M				//Change to next address
	M=-1				//Change pixels to black
	
	@i
	M=M+1				//Increment i

	@DARK_SCREEN
	0;JMP	
