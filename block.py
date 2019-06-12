# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 21:41:28 2019

@author: pjl
"""

import pygame
#block_life_color=(255,255,255)
life_color=(102,204,255)
dead_color=(0,0,0)
class Block():
  def __init__(self,r,c,alive,block_size):
      self.alive=alive
      self.rect=pygame.Rect(c*(block_size+1),r*(block_size+1),block_size,block_size)
      
  def draw_block(self,screen):
    if self.alive: 
      pygame.draw.rect(screen,life_color,self.rect)
    else:
      pygame.draw.rect(screen,dead_color,self.rect)
      
  def set_alive(self,alive):
    self.alive=alive