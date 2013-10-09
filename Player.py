import pygame
from random import randrange
import threading
import time
import app


lock= threading.Lock()
class Player(threading.Thread):
	def __init__(self,app,maze,Or,inicio,fin,recorrido,img_list):

		threading.Thread.__init__(self)
		self.maze=maze
		self.Or=Or
		self.inicio=inicio
		self.fin=fin
		self.recorrido=recorrido
		self.img_list=img_list
		self.img_current=self.img_list[self.Or][0]
		self.chg=0
		self.Y=self.inicio[0]*32
		self.X=self.inicio[1]*32
		self.alive=True
		self.move_pos=0
		self.pos=inicio
		self.app=app

	def move(self):

		if self.Or==2:
			self.move_pos+=8
			self.Y+=8
			if self.chg==0:
				self.img_current=self.img_list[self.Or][1]
				self.chg=1
			elif self.chg==1:
				self.img_current=self.img_list[self.Or][0]
				self.chg=0
			if self.move_pos==32:
				print "llegue"
				self.pos[0]+=1
				if self.maze[self.pos[0]][self.pos[1]+1]==0:
					self.llamarHijo(1,self.pos)
				if self.maze[self.pos[0]][self.pos[1]-1]==0:
					self.llamarHijo(1,self.pos)	
				if self.maze[self.pos[0]+1][self.pos[1]]==1:
					self.Die()
				self.move_pos=0
		if self.Or==1:
			print self.move_pos
			self.move_pos+=8
			self.X+=8
			if self.chg==0:
				self.img_current=self.img_list[self.Or][1]
				self.chg=1
			elif self.chg==1:
				self.img_current=self.img_list[self.Or][0]
				self.chg=0
			if self.move_pos==32:
				print "llegue"
				lock.acquire()
				self.pos[1]+=1
				# if self.maze[self.pos[0]][self.pos[1]+1]==0:
				# 	self.llamarHijo(1,self.pos)
				# if self.maze[self.pos[0]][self.pos[1]-1]==0:
				# 	self.llamarHijo(1,self.pos)
				print `self.pos[0]`+" " +`self.pos[1]+1`
				if self.maze[self.pos[0]][self.pos[1]+1]==1:
					self.Die()
				lock.release()
				self.move_pos=0


	def Die(self):
		self.alive=False

	def get_curr_img(self):
		return self.img_current

	def llamarHijo(self,Or,inicio):
		print "nacio mi hijo"
		player=Player(self.app,self.maze,Or,inicio,self.fin,self.recorrido,self.img_list)
		self.app.PlayerList.append(player)
		self.app.PlayerList[-1].start()



	def run(self):

		while self.alive==True:
			self.move()
			time.sleep(.7)
				






