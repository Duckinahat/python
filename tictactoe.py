## Tic-Tac-Toe V3.1 ##
## Nicola Leonardi ##
## written for python 3 ##

# Simple tictactoe game playable with 1 or 2 players #



## Import Libraies ##
# random for computer AI
# time for added realism

import random
import time


## Define Functions ##

def main():		# Main function contains title screen setup and initiates play #

	play = 1	#set play to true
		
	while play:		#while loop persists until play false
	
		#present title
	
		print(str('\n' * 100),'   Tic-Tac-Toe   \n','-----------------\n', )
		
		mod = input('Select mode, Human vs. Human, or Human vs. Computer: ')
		
		if 'c' in mod.lower():				#searces for 'c' from 'computer' or 'com' etc.
			mod = input('X\'s or O\'s: ')
			if 'x' in mod.lower():
				mode = 2					#sets mode depending on player choice
			elif 'o' in mod.lower():
				mode = 3
			else:
				print('X it is')
				time.sleep(1)
		elif 'h' in mod.lower():			#if no 'c' checks 'h' presence for 'human'
			mode = 1
		else:								#else re-asks
			print('Invalid entry')
			time.sleep(1)
			mode = 0
		
		if mode != 0:						#if mode not 0:
			tictactoe(mode)					#play
			play = playAgain()				#replay?
			
	print('Goodbye')	#after play bid farewell
	time.sleep(1)		#wait 1 sec before ending

def boardDef():	# Defines a blank play board #
	
	#spaces represented as simple list
	
	board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
	
	return(board)		#return list


def display(board):		# Displays board visually to player #

	b = board			#rename for ease of coding
	
	#clear the screen and print as array
	print(str('\n' * 100),\
'   Tic-Tac-Toe   \n', \
'-----------------\n', \
'#' , '1' , '2' , '3' , '\n' \
'A' , b[0], b[1], b[2], '\n' \
'B' , b[3], b[4], b[5], '\n' \
'C' , b[6], b[7], b[8], '\n' )
	return
	

def ask(board):		# Gets user input #

	entry = input('Enter Co-ordinates: ')
	entry = entry.upper()	#helps uniformity
	coord = 0	#set container for guess
	
	try:		#keps program from crashing
		
		#check input for row, add to container accordingly
		if 'C' in entry:
			coord += 6
		elif 'B' in entry:
			coord += 3
		elif 'A' not in entry:
			print('Invalid entry')
			return(ask(board))
		
		#check input for column, add to container accordingly
		if '3' in entry:
			coord += 2
		elif '2' in entry:
			coord += 1
		elif '1' not in entry:
			print('Invalid entry')
			return(ask(board))
		
		#check space is free
		if board[coord] == ' ':
			return(coord)	#retuns index coordinate
		else:
			print('Space occupied')
			return(ask(board))
	
	except:
		return(ask(board))
		
		
def tokenSel(turn):	# Checks turn num to change X or O #
	if turn % 2 == 0:
		return('X')
	else:
		return('O')


def winCond(board,token):	# Checks board for win #
	b = board	#simplify
	t = token	#simplify
	
	#for loop checks row win, column win, and X wins
	for i in range(3):
		if b[i*3] == b[i*3+1] == b[i*3+2] == t\
		or b[i] == b[i+3] == b[i+6] == t\
		or b[0] == b[4] == b[8] == t\
		or b[6] == b[4] == b[2] == t:
			return(1)	#if win return true
	return(0)	#else false
	
	
def move(board,token,entry):	# Changes board list to move #
	if board[entry] == ' ':		#block illegal moves
		board[entry] = token	#change item
	return(board)				#return board


def testMove(test,token,entry):	# Tests possible move or win #
	if test[entry] == ' ':		#block illegal move
		test[entry] = token		#change item
	return(winCond(test,token))	#return if win
	
	
def playAgain():				# Modifies value of play #

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


def comp(board,turn):	# AI #

	t1 = tokenSel(turn)		#computers token
	t2 = tokenSel(turn+1)	#opponents token
	time.sleep(1)			#wait 1 sec
	
	# Check computer win #
	for i in range(9):	#test all 9 spaces
		b = board[:]	#copy board
		if testMove(b,t1,i):	#check win
			return(i)	#return win index
	
	# Check player win #
	for i in range(9):	#test all 9 spaces
		b = board[:]	#copy board
		if testMove(b,t2,i):	#check win
			return(i)	#return win index
			
	# Check center #
	b = board[:]	#copy board
	if b[4] == ' ':	#check open
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
		if c[1] == ' ':
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
		if s[1] == ' ':
			return(c[0])
		
def tictactoe(mode):	# Gameplay #
	turn = 0
	board = boardDef()
	
	while turn < 9:
		display(board)
		token = tokenSel(turn)
		print(token,'\'s turn\n',sep='')
		
		if mode == 1:
			entry = ask(board)
		
		elif mode == 2:
			if token == 'X':
				entry = ask(board)
			else:
				entry = comp(board,turn)
			
		elif mode == 3:
			if token == 'X':
				entry = comp(board,turn)
			else:
				entry = ask(board)
		
		move(board,token,entry)
		turn += 1
		
		if winCond(board,token):
			display(board)
			print(token,'Wins!')
			turn = 10
	
	if turn == 9:
		print('Cat\'s Game')
		
	return

## Excecute Program ##

main()
