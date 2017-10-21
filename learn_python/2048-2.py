import curses
from random import randrange,choice
from collections import defaultdict

actions=["Up","Down","Left","Right","Exit","Restart"]

codes=[ord(ch) for ch in"WSADQRwsadqr"]

directions=dict(zip(codes,actions*2))#create a new dictionary to change input

def main(stdscr):
	
	def Init():#It's the first step
		game_field.reset()
		game_field.draw(stdscr)
		return "Game"
		
	def Still(state):#It's the ceased screen
		game_field.draw(stdscr)
		action=get_action(stdscr)
		response=defaultdict(lambda:state)
		response['Restart'],response['Exit']='Init','Exit'
		return response[action]
		
	def Game():#It's the game screen
		game_field.draw(stdscr)
		action=get_action(stdscr)
		if action=='Restart':
			return 'Init'
		if action=='Exit':
			return 'Exit'
		if game_field.move(action):
			if game_field.win():
				return 'Win'
			if game_field.over():
				return 'Over'
		return 'Game'
		
	state1={
		'Init':Init,
		'Win':lambda:Still('Win'),
		'Over':lambda:Still('Over'),
		'Game':Game
		}
		
	curses.use_default_colors()
	game_field=Games()
	
	state='Init'
	
	while state!='Exit':#change the screen
		state=state1[state]()

def get_action(keyboard):
	char='n'
	while char not in directions:
		char=keyboard.getch()
	return directions[char]
	
def transpose(field):
	return [list(row) for row in zip(*field)]
	
def invert(field):
	return [row[::-1] for row in field] #??? 
	
class Games(object):

	def __init__(self):
		self.width=4
		self.height=4
		self.scores=0
		self.highscore=0
		self.reset()
		
	def rand(self):
		num=4 if randrange(100)>90 else 2
		(i,j)=choice([(i,j) for i in range(self.width) for j in range(self.height) if self.field[i][j]==0])
		self.field[i][j]=num
		
	def reset(self):
		if self.scores>self.highscore:
			self.highscore=self.scores
		self.scores=0
		self.field=[[0 for i in range(self.width)]for j in range(self.height)]
		self.rand()
		self.rand()
	
	def move(self,action):
		def move_row_left(row):
			def tight(row):
				while 0 in row:
					row.remove(0)
				for i in range(4-len(row)):
					row.append(0)
				return row
			
			def moving(row):
				for i in range(len(row)):
					if i+1<len(row) and row[i]==row[i+1]:
						row[i]=2*row[i]
						row[i+1]=0
						self.scores+=row[i]
				return row
			
			return tight(moving(tight(row)))
		
		moves={}
		moves['Left']=lambda field:[move_row_left(row) for row in field]
		moves['Right']=lambda field:invert(moves['Left'](invert(field)))
		moves['Up']=lambda field:transpose(moves['Left'](transpose(field)))
		moves['Down']=lambda field:transpose(moves['Right'](transpose(field)))
		
		if action in moves:
			if self.movable(action):
				self.field=moves[action](self.field)
				self.rand()#show a new number in the field
				return True
			else:
				return False
				
	def movable(self,action):
		def movable_left(row):
			def change(i):
				if row[i]==0 and row[i+1]!=0:
					return True
				if row[i]==row[i+1] and row[i]!=0:
					return True
				return False
			return any(change(i) for i in range(len(row)-1))
		
		movables={}
		movables['Left']=lambda field:any(movable_left(row) for row in field)
		movables['Right']=lambda field:movables['Left'](invert(field))
		movables['Up']=lambda field:movables['Left'](transpose(field))
		movables['Down']=lambda field:movables['Right'](transpose(field))
		
		if action in movables:
			return movables[action](self.field)
		else:
			return False
		
	def win(self):
		return any(any(i>=2048 for i in row)for row in self.field)
		
	def over(self):
		return not any(self.movable(action) for action in actions)
		
	def draw(self,screen):
		string1="(W)UP (S)DOWN (A)LEFT (D)RIGHT"
		string2="       (R)RESTART (Q)EXIT"
		win_string="         You Win!!!"
		over_string="        Game Over"
		def cast(string):
			screen.addstr(string+'\n')
		
		def horsep():#define a horizontal line
			line='+'+('------+'*self.width+'+')
			separator=defaultdict(lambda:line)
			if not hasattr(horsep,'counter'):
				horsep.counter=0
			cast(separator[horsep.counter])
			horsep.counter+=1
			
		def data(row):
			cast(''.join('|{:^6}'.format(num) if num >0 else '|      '  for num in row)+'|')
			
		screen.clear()
		cast("SCORES:"+str(self.scores))
		
		if self.highscore!=0:
			cast("HIGHSCORE:"+str(self.highscore))
		
		for row in self.field:
			horsep()
			data(row)
			
		horsep()
		
		if self.win():
			cast(win_string)
		elif self.over():
			cast(over_string)
		else:
			cast(string1)
			
		cast(string2)
		
curses.wrapper(main)