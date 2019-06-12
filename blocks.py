# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 22:01:24 2019

@author: pjl
"""

import pygame

#block_life_color=(255,255,255)
life_color=(102,204,255)
dead_color=(0,0,0)

class Blocks():
  def __init__(self,r,c,block_size,screen):
    self.block_size=block_size
    self.blocks=[[0]*c for i in range(r)]
    for i in range(len(self.blocks)):
      for j in range(len(self.blocks[0])):
        self.blocks[i][j]=Block(i,j,block_size,screen)
  def draw_board(self):
    for i in range(len(self.blocks)):
      for j in range(len(self.blocks[0])):
        self.blocks[i][j].draw_block()
      
  def set_status(self,status):
    for i in range(len(self.blocks)):
      for j in range(len(self.blocks[0])):
        self.blocks[i][j].set_alive(status[i][j])
  
  def click(self,r,c):
    self.blocks[r][c].click_on()
        
class Block():
  def __init__(self,r,c,block_size,screen):
    self.alive=False
    self.screen=screen
    self.rect=pygame.Rect(c*(block_size+1),r*(block_size+1),block_size,block_size)
      
  def draw_block(self):
    if self.alive: 
      pygame.draw.rect(self.screen,life_color,self.rect)
    else:
      pygame.draw.rect(self.screen,dead_color,self.rect)
      
  def set_alive(self,alive):
    self.alive=alive
    
  def click_on(self):
    self.alive^=1
    self.draw_block()