import pygame
import thread
import time
from random import randrange
import Player



class App:
	def __init__(self,n,lab,inicio,final):
		self.game=pygame
		self.game.init()
		self.n=n
		self.background_path ="./Images/background.png"
		self.block_path="./Images/block.png"
		self.screen=pygame.display.set_mode( (n*32,n*32),0,32)
		self.background = self.game.image.load(self.background_path).convert()
		self.block=self.game.image.load(self.block_path).convert()
		self.lab=lab
		self.inicio=inicio
		self.final=final
		self.setPlayer_img()
		self.PlayerList=[]

	def draw(self):
		j=0
		m=0
		for y in range(0,self.n*32,32):
		 	for x in range(0,self.n*32,32):
		 		if self.lab[j][m]==0:
		 			self.screen.blit( self.background,(x,y))
		 		else:
		 			self.screen.blit( self.block,(x,y))
		 		m+=1
		 	j+=1
		 	m=0
		
		#print len(PlayerList)
		#print len(PlayerList)
		for player in self.PlayerList:
			# print PlayerList[i].X
			# print PlayerList[i].Y
			#print player
			self.screen.blit( player.get_curr_img() ,(player.X, player.Y ))
		 
		#self.screen.blit( self.background, (0,0) )
		#self.screen.blit( self.background, (96,0) )


	def setPlayer_img(self):
		self.Player_path = "./Images/sprites/"
		
		
		self.Player_walk_n = [self.Player_path + "walk1-n.png", self.Player_path + "walk2-n.png"]
		self.Player_walk_s = [self.Player_path + "walk1-s.png", self.Player_path + "walk2-s.png"]
		self.Player_walk_e = [self.Player_path + "walk1-e.png", self.Player_path + "walk2-e.png"]
		self.Player_walk_w = [self.Player_path + "walk1-w.png", self.Player_path + "walk2-w.png"]
		
		

		self.Player_lst = [[],[],[],[],[]]
		
		
		self.Player_lst = [ list(self.Player_walk_n) , list(self.Player_walk_e), list(self.Player_walk_s), list(self.Player_walk_w) ]
		
		self.Player_img_n = []
		self.Player_img_e = []
		self.Player_img_s = []
		self.Player_img_w = []


		self.Player_w = 17
		self.Player_h = 25
		self.Player_area = pygame.Rect((0,0),(self.Player_w,self.Player_h))


		for i in range(0,2):
			self.Player_img_n.append(self.game.image.load(self.Player_lst[0][i]).convert_alpha(self.background))
			self.Player_img_e.append( self.game.image.load(self.Player_lst[1][i]).convert_alpha(self.background) )
			self.Player_img_s.append( self.game.image.load(self.Player_lst[2][i]).convert_alpha(self.background) )
			self.Player_img_w.append( self.game.image.load(self.Player_lst[3][i]).convert_alpha(self.background) )

		
		self.Player_img = [ list(self.Player_img_n), list(self.Player_img_e),list(self.Player_img_s), list(self.Player_img_w)]
	# @staticmethod	
	# def llamarHijo(Or,inicio,maze,fin,recorrido,img_list):
	# 	print "nacio mi hijo"
	# 	player=Player.Player(maze,Or,inicio,fin,recorrido,img_list)
	# 	print len(PlayerList)
	# 	PlayerList.append(player)
	# 	print len(PlayerList)
	# 	PlayerList[-1].start()	

def main():
	lab=[[1,0,1,1,1,1,1,1,1,1],
		[1,0,0,0,0,0,0,0,0,1],
		[1,0,1,1,1,1,1,1,0,1],
		[1,0,1,1,1,1,0,0,0,1],
		[1,0,1,1,1,1,0,1,0,1],
		[1,0,1,1,1,1,0,1,0,1],
		[1,0,1,0,0,1,0,1,0,1],
		[1,0,1,1,1,1,0,1,0,1],
		[1,0,0,0,0,0,0,1,0,1],
		[1,1,1,1,1,1,1,1,0,1]]

	inicio=[0,1]
	final=[9.8]
	juego = App(10,lab,inicio,final)
	recorrido=[]
	player=Player.Player(juego,lab,2,inicio,final,recorrido,juego.Player_img)
	juego.PlayerList.append(player)
	juego.PlayerList[0].start()
	while True:
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit_game()
		juego.draw()
		
		pygame.display.update()

if __name__ == "__main__":
	main()