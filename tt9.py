### Nine-Board Tic-Tac-Toe ###
	  ### With AI ###
## By Nicola Leonardi ##

# Language Counts #
# Written for python 3 #

# these are for the computer 
import time
import random
		
def main():

	# Start game
	play = titleScreen()
	
	# Program loop
	while play:
		win = 0
		turn = 0
		board = boardEmpty()
		playBoard = 4
		player = turnSel()
		
		# Game loop
		while not win:
		
			# current token decided, board displayed
			token = tokenSel(turn)
			print('\n'*100+' '*11+str(token)+'\'s turn')
			displayBoard(board,playBoard)
			
			# when it's player's turn, get input
			if token == player:
				move = ask(board,playBoard)
			
			# when it's not, computer goes
			else:
				move = com(turn,board,playBoard)
			
			# if ask() outputs 10, ends game	
			if move == 10:
				break
			
			# modify the current board, check for win, change to next board
			board[playBoard][move] = token
			win = winCond(board[playBoard],token)
			playBoard = move
			
			# advance turn 	
			turn += 1
		
		# Win statement
		if win == 1:
			print('\n'*100+' '*11+str(token)+' wins!')
		
		# Tie statement	
		else:
			print('\n'*100+' '*10+'Cat\'s game')
		
		# Show final board and ask for replay	
		displayBoard(board,playBoard)
		time.sleep(1)
		play = playAgain()
		
	return

	
def titleScreen():
## Function presents user with optins and sets parameter play to begin game
	
	play	 = -1
	
	# Title loop
	while play < 0:
		
		# show options
		print('\n'*100+'''
 _________________________________
|                                 |
|  |# # #| |Tic-Tac-Toe| |# # #|  |
|  |# # #| |9x9 Edition| |# # #|  |
|  |# # #|               |# # #|  |
|             |# # #|             |
|             |# # #|             |
|             |# # #|             |
|                                 |
|       (by Nicola Leonardi)      |
|                                 |
|                                 |
|            -Options-            |
|  [Play]-[Instructions]-[Quit]   |
|                                 |
|_________________________________|
''')
		
		# filter input and return play value
		try:
			iput = input('Selection: ')
			if 'P' in iput.upper():
				play = 1
			elif 'Q' in iput.upper():
				play = 0
			elif 'I' in iput.upper():
				instructions()
			else:
				print('Invalid Entry')
				
		except:
			print('Invalid Entry')
			
		time.sleep(.5)
		
	return(play)


def instructions():
##  Gives user the rules of the game

	print('\n'*100+'''
In 9x9 Tic-Tac-Toe, players take turns
entering their token onto a 3x3 play-
board. The space selected also changes
the current play-board to the corresponding
board in the larger space. Players win 
by getting 3-in-a-row either horizantaly,
diagonaly, or verticaly, on a single 
board. If the active board becomes full
without a winner, the game is tied.

To select a space enter a letter and a number
eg... a1, b 2, Cx1, a-3 etc.

Good Luck.
''')
	
	# wait till user is ready
	input('To continue press enter.')
	
	return


def boardEmpty():
##  Sets up a list of 9 lists of 9 empty strings

	board = []
	emptySpace = ' '
	
	for i in range(9):
		boardSingle = []
		
		for i in range(9):
			boardSingle.append(emptySpace)
			
		board.append(boardSingle)
		
	return(board)


def displayBoard(board,playBoard):
##  Extracts useful data from board and makes a visual representation of the game

	b = board
	let = ' ABC'
	
	print(' '+'_'*28)
	print('|'+' '*28+'|')
	for i in range(3):
		for j in range(4):
			if j == 0:
				print('|',end='')
				for k in range(3):
					if playBoard%3 == k and playBoard//3 == i:
						print(' #','1','2','3',end=' ')
					else:
						print('  ',' ',' ',' ',end=' ')
				print(' |')
			else:
				print('|',end='')
				for k in range(3):
					if playBoard%3 == k and playBoard//3 == i:
						print('',let[j],end=' ')
					else:
						print('',' ',end=' ')
					for l in range(3):
						print(b[i*3+k][l+(j-1)*3],end=' ')
				print(' |')
	print('|'+'_'*28+'|')
	
	return


def ask(board,playBoard):
##	Recievs input and filters it

	valid = 0
	let = 'ABC'
	num = '123'
	
	print()
	
	while not valid:
		move = input('Enter co-ordinates: ')
		MOVE = move.upper()
		
		try:
			
			if 'Q' in MOVE:
				coord = 10
				valid = 1
				
			elif MOVE[0] in let and MOVE[-1] in num:
				coord = let.index(MOVE[0])*3 + num.index(MOVE[-1])
				
				if board[playBoard][coord] == ' ':
					valid = 1
				
				else:
					print('Space taken')
					
			else:
				print('Invalid input')
				
		except:
			print('Invalid input')
			
	return(coord)


def winCond(boardCur,token):
## Checks board for win #

	b = boardCur	#simplify
	t = token		#simplify
	
	#for loop checks row win, column win, and X wins
	for i in range(3):
		if b[i*3] == b[i*3+1] == b[i*3+2] == t\
		or b[i] == b[i+3] == b[i+6] == t\
		or b[0] == b[4] == b[8] == t\
		or b[6] == b[4] == b[2] == t:
			return(1)	#if win return true
			
	if ' ' not in b:
		return(2)
		
	return(0)	#else false

def tokenSel(turn):
## Checks turn num to change X or O 

	if turn % 2 == 0:
		return('X')
		
	else:
		return('O')


def turnSel():
##

	print('\n'*100)
	inp = input('X\'s or O\'s? ')
	
	if 'X' in inp.upper():
		player = 'X'
		
	else:
		player = 'O'
		
	return(player)


def com(turn,board,playBoard):
##

	t1 = tokenSel(turn)		#computers token
	t2 = tokenSel(turn+1)	#opponents token
	time.sleep(1)
	
	# Check computer win #
	for i in range(9):	#test all 9 spaces
		b = board[playBoard][:]	#copy board
		if b[i] == ' ':
			b[i] = t1
		if winCond(b,t1):	#check win
			return(i)	#return win index
	
	# Check player win other board#
	noGo = []
	for j in range(9):
		bor = board[j][:]
		for i in range(9):	#test all 9 spaces
			b = bor[:]
			if b[i] == ' ':
				b[i] = t2
			if winCond(b,t2):	#check win
				noGo.append(j)	#set bad spaces
	
	# Check Player win current board #
	for i in range(9):
		b = board[playBoard][:]
		if b[i] == ' ':
			b[i] = t2
		if winCond(b,t2):
			if i not in noGo:
				return(i)
	
	# Check center possibly take #
	b = board[playBoard][:]	#copy current board
	if b[4] == ' ':	#check open
		prob = random.randint(0,5)
		if prob == 2 and 4 not in noGo:
			return(4)	#return index
	
	# Check coners #
	c1 = 0,b[0]
	c2 = 2,b[2]
	c3 = 6,b[6]
	c4 = 8,b[8]
	corners = [c1,c2,c3,c4]
	random.shuffle(corners)
	for c in corners:
		corners.pop(0)
		if c[1] == ' ' and c[0] not in noGo:
			return(c[0])
	
	# Check sides #
	s1 = 1,b[1]
	s2 = 3,b[3]
	s3 = 5,b[5]
	s4 = 7,b[7]
	sides = [s1,s2,s3,s4]
	random.shuffle(sides)
	for s in sides:
		sides.pop(0)
		if s[1] == ' ' and s[0] not in noGo:
			return(s[0])
	
	# If no good moves, random #
	moveList = []
	for i in range(9):
		if b[i] == ' ':
			moveList.append(i)
	random.shuffle(moveList)
	return(moveList[0])
	
	
def playAgain():
# Modifies value of play #

	play = input('Play again?\n')	#user input
	play = play.lower()		#normalize
	
	#check for 'y', 'ok', 'sure'
	if 'y' in play\
	or play == 'ok'\
	or play == 'sure'\
	and play != 'nay':	#only negative containing 'y'
		return(1)
		
	else:
		return(0)

## RUN THE PROGRAM ##

main()

# say goodbye exit
print('\n'*100+'''
	Goodbye
	''')
time.sleep(3)
