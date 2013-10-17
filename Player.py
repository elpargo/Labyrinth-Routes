import pygame
from random import randrange
import threading
import time
import pickle


lock= threading.Lock()
class Player(threading.Thread):
	def __init__(self,app,maze,Or,inicio,fin,recorrido,img_list,n):

		super(Player, self).__init__()
		self.maze=maze
		self.Or=Or
		self.inicio=inicio
		self.fin=fin
		self.recorrido=pickle.loads(pickle.dumps((recorrido)))
		self.img_list=img_list
		self.img_current=self.img_list[self.Or][0]
		self.chg=0
		self.Y=self.inicio[0]*32
		self.X=self.inicio[1]*32
		self.alive=True
		self.move_pos=00
		self.posX=inicio[1]
		self.posY=inicio[0]
		self.app=app
		self.n=n
		self.lapida_path="./Images/lapida.png"
		self.lapida=pygame.image.load(self.lapida_path).convert_alpha(self.app.background)
		print self.name

	def move(self):


		if self.Or==0:
			self.move_pos+=-8
			self.Y-=8
			if self.chg==0:
				self.img_current=self.img_list[self.Or][1]
				self.chg=1
			elif self.chg==1:
				self.img_current=self.img_list[self.Or][0]
				self.chg=0
			if self.move_pos==-32:
				if self.name=="Thread-1":
					self.maze[self.inicio[0]][self.inicio[1]]=1
				self.posY-=1
				self.move_pos=0
				self.recorrido.append((self.posX*32,self.posY*32))
				if(self.posX==self.fin[1] and self.posY==self.fin[0]):
					self.MazeOut()
				if 	self.posX<self.n-1 and self.posX>=0:
					if self.maze[self.posY][self.posX+1]==0:
						self.llamarHijo(1,((self.posX+1)*32,self.posY*32))
				if 	self.posX>0:
					if self.maze[self.posY][self.posX-1]==0:
						self.llamarHijo(3,((self.posX-1)*32,self.posY*32))	
				if 	self.posY>0:
					if self.maze[self.posY-1][self.posX]==1:
						self.Die()
				
				


		elif self.Or==2:
			self.move_pos+=8
			self.Y+=8
			if self.chg==0:
				self.img_current=self.img_list[self.Or][1]
				self.chg=1
			elif self.chg==1:
				self.img_current=self.img_list[self.Or][0]
				self.chg=0
			if self.move_pos==32:
				if self.name=="Thread-1":
					self.maze[self.inicio[0]][self.inicio[1]]=1
				self.posY+=1
				self.move_pos=0
				self.recorrido.append((self.posX*32,self.posY*32))
				if(self.posX==self.fin[1] and self.posY==self.fin[0]):
					
					self.MazeOut()
				if 	self.posX<self.n-1 and self.posX>=0:
					if self.maze[self.posY][self.posX+1]==0:
						self.llamarHijo(1,((self.posX+1)*32,self.posY*32))
				if 	self.posX>0:
					if self.maze[self.posY][self.posX-1]==0:
						self.llamarHijo(3,((self.posX-1)*32,self.posY*32))
				if 	self.posY<self.n and self.posY>=0:
					if self.maze[self.posY+1][self.posX]==1:
						self.Die()
					
				

				
				
		elif self.Or==1:
			self.move_pos+=8
			self.X+=8
			if self.chg==0:
				self.img_current=self.img_list[self.Or][1]
				self.chg=1
			elif self.chg==1:
				self.img_current=self.img_list[self.Or][0]
				self.chg=0
			if self.move_pos==32:
				if self.name=="Thread-1":
					self.maze[self.inicio[0]][self.inicio[1]]=1
				self.posX+=1
				self.move_pos=0

				self.recorrido.append((self.posX*32,self.posY*32))
				if(self.posX==self.fin[1] and self.posY==self.fin[0]):
					self.MazeOut()
				if 	self.posY<self.n and self.posY>=0:
					if self.maze[self.posY+1][self.posX]==0:
					 	self.llamarHijo(2,(self.posX*32,(self.posY+1)*32))
				if 	self.posY>0:
					if self.maze[self.posY-1][self.posX]==0:
					 	self.llamarHijo(0,(self.posX*32,(self.posY-1)*32))
				if 	self.posX<self.n and self.posX>=0:
					if self.maze[self.posY][self.posX+1]==1:
						self.Die()
				
				

		elif self.Or==3:
			self.move_pos-=8
			self.X-=8
			if self.chg==0:
				self.img_current=self.img_list[self.Or][1]
				self.chg=1
			elif self.chg==1:
				self.img_current=self.img_list[self.Or][0]
				self.chg=0
			if self.move_pos==-32:
				if self.name=="Thread-1":
					self.maze[self.inicio[0]][self.inicio[1]]=1
				self.posX-=1
				self.move_pos=0
				self.recorrido.append((self.posX*32,self.posY*32))
				if(self.posX==self.fin[1] and self.posY==self.fin[0]):
					self.MazeOut()
				if 	self.posY<self.n and self.posY>=0:
					if self.maze[self.posY+1][self.posX]==0:
					 	self.llamarHijo(2,(self.posX*32,(self.posY+1)*32))
				if 	self.posY>0:
					if self.maze[self.posY-1][self.posX]==0:
					 	self.llamarHijo(0,(self.posX*32,(self.posY-1)*32))
				if 	self.posX>0:
					if self.maze[self.posY][self.posX-1]==1:
						self.Die()
				
	def Die(self):
		print "mori"
		self.img_current=self.lapida
		self.alive=False

	def get_curr_img(self):
		return self.img_current

	def llamarHijo(self,Or,dupla):
		print "nacio mi hijo"
		cantMove=True
		for i in range(len(self.recorrido)):
			if dupla==self.recorrido[i]:
				print "no puede"
				cantMove=False
		if cantMove==True:
			
			player=Player(self.app,self.maze,Or,[self.posY,self.posX],self.fin,self.recorrido,self.img_list,self.n)
			self.app.PlayerList.append(player)
			self.app.PlayerList[-1].start()
		#player.start()

	def MazeOut(self):
		color=(randrange(256),randrange(256),randrange(256))
		print "estoy en la meta"
		self.app.AllRoutes.append(self.recorrido)
		self.app.drawRoutes(color)
		self.alive=False



	def run(self):

		while self.alive==True:
		
			self.move()
			time.sleep(.2)


			
				






