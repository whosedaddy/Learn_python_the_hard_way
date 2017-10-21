import curses
from random import randrange,choice
from collections import defaultdict

actions = ['UP','DOWN','RIGHT','LEFT','EXIT','RESTART']

lettercodes = [ord(ch) for ch in "WSDAQRwsdaqr"]

actions_dict = dict(zip(lettercodes,actions*2))

def main(stdscr):
	
	def init():
		game_field.reset()
		return 'Game'
		
	def not_game(state):
		game_field.draw(stdscr)
		action=get_user_action(stdscr)
		responses=defaultdict(lambda:state)
		responses['RESTART'],responses['EXIT']='Init','Exit'
		return responses[action]
		
	def game():
		game_field.draw(stdscr)
		action=get_user_action(stdscr)
		
		if action=='RESTART':
			return 'Init'
		if action=='EXIT':
			return 'EXIT'
		if game_field.move(action):
			if game_field.is_win():
				return "Win"
			if game_field.is_gameover():
				return "GameOver"
		return "Game"
		
	state_action = {
			'Init':init,
			'Win':lambda:not_game('Win'),
			'GameOver':lambda:not_game('GameOver'),
			'Game':game
			}
	curses.use_default_colors()
	game_field=GameField(win=32)
	
	state='Init'
	while state!='Exit':
		state=state_action[state]()
		
def get_user_action(keyboard):
	char='N'
	while char not in actions_dict:
		char=keyboard.getch()
	return actions_dict[char]
	
def transpose(field):
	return[list(row) for row in zip(*field)]
	
def invert(field):
	return[row[::-1] for row in field]
	
class GameField(object):
	def __init__(self,height=4,width=4,win=2048):
		self.height=height
		self.width=width
		self.win_value=2048
		self.score=0
		self.highscore=0
		self.reset()
		
		
	def spawn(self):
		new_element=4 if randrange(100)>89 else 2
		(i,j)=choice([(i,j)for i in range(self.width) for j in range(self.height) if self.field[i][j]==0])
		self.field[i][j]=new_element
		
	def reset(self):
		if self.score>=self.highscore:
			self.highscore=self.score
		self.score=0
		self.field=[[0 for i in range(self.width)]for j in range(self.height)]
		self.spawn()
		self.spawn()
		
	
	def move(self,direction):
		def move_row_left(row):
			def tighten(row):
				new_row=[i for i in row if i!=0]
				new_row+=[0 for i in range(len(row)-len(new_row))]
				return new_row
				
			def merge(row):
				pair=False
				new_row=[]
				for i in range(len(row)):
					if pair:
						new_row.append(2*row[i])
						self.score+=2*row[i]
					else:
						if i+1<len(row) and row[i]==row[i+1]:
							pair=True
							new_row.append(0)
						else:
							new_row.append(row[i])
				assert len(new_row)==len(row)
				return new_row
				
			return tighten(merge(tighten(row)))
			
		moves={}
		moves['LEFT']=lambda field:[move_row_left(row) for row in field]
		moves['RIGHT']=lambda field:invert(moves['LEFT'](invert(field)))
		moves['UP']=lambda field:transpose(moves['LEFT'](transpose(field)))
		moves['DOWN']=lambda field:transpose(moves['RIGHT'](transpose(field)))
		
		if direction in moves:
			if self.move_is_possible(direction):
				self.field=moves[direction](self.field)
				self.spawn()
				return True
			else:
				return False
				
	def is_win(self):
		return any(any(i>self.win_value for i in row)for row in self.field)
	
	def is_gameover(self):
		return not any(self.move_is_possible(direction) for direction in actions)
		
	def move_is_possible(self,direction):
		def row_is_lefr_movable(row):
			def change(i):
				if row[i]==0 and row[i+1]!=0:
					return True
				if row[i]!=0 and row[i]==row[i+1]:
					return True
				return False
			return any(change(i) for i in range(len(row)-1))
			
		check={}
		check['LEFT']=lambda field:any(row_is_lefr_movable(row)for row in field)
		check['RIGHT']=lambda field:check['LEFT'](invert(field))
		check['UP']=lambda field:check['LEFT'](transpose(field))
		check['DOWN']=lambda field:check['RIGHT'](transpose(field))
		
		if direction in check:
			return check[direction](self.field)
		else:
			return False
			
	def draw(self,screen):
		help_string1=' (W)UP (S)DOWN (A)LEFT (D)RIGHT'
		help_string2='       (R)RESTART (Q)EXIT'
		gameover_string='             GAME OVER'
		win_string='             YOU WIN'
		def cast(string):
			screen.addstr(string+'\n')
			
		def draw_separator():
			line='+'+('+------'*self.width+'+')
			separator=defaultdict(lambda:line)
			if not hasattr(draw_separator,"counter"):
				draw_separator.counter=0
			cast(separator[draw_separator.counter])
			draw_separator.counter+=1
			
		def draw_row(row):
			cast(''.join('|{:^6}'.format(num) if num>0 else '|      'for num in row)+'|')
			
		screen.clear()
		
		cast('SCORE:'+str(self.score))
		if 0!=self.highscore:
			cast('HIGHSCORE:'+str(self.highscore))
		
		for row in self.field:
			draw_separator()
			draw_row(row)
			
		draw_separator()
		
		if self.is_win():
			cast_win(win_string)
		else:
			if self.is_gameover():
				cast(gameover_string)
			else:
				cast(help_string1)
		cast(help_string2)
		
curses.wrapper(main)		