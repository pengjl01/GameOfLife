# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 15:45:41 2019

@author: pjl
"""

import sys
import pygame
from core import Core
from blocks import Blocks
from button import Button

#r=160
#c=240
#block_size=5
r=40
c=70
block_size=20
bg_color=(230,230,230)
class GameOfLife:
  def __init__(self):
    pygame.init()  #初始化背景设置
    self.blocks_right=c*(block_size+1)
    self.screen=pygame.display.set_mode((self.blocks_right+100,r*(block_size+1)))
    pygame.display.set_caption("Game Of Life")  #设置标题
    self.screen.fill(bg_color)
    self.blocks=Blocks(r,c,block_size,self.screen)
    self.blocks.draw_board()
    self.core=Core(r,c)
    self.next_button=Button(self.blocks_right+10,20,self.screen,'next')
    self.start_button=Button(self.blocks_right+10,80,self.screen,'start')
    self.stop_button=Button(self.blocks_right+10,140,self.screen,'stop')
    self.running=False
    self.next_button.draw_button()
    self.start_button.draw_button()
    self.stop_button.draw_button()
    pygame.display.flip()
  def click_block(self,mouse_x,mouse_y):
    r=int(mouse_y/(block_size+1))
    c=int(mouse_x/(block_size+1))
    self.core.change_block(r,c)
    self.blocks.click(r,c)
    pygame.display.flip()
  def click_button(self,mouse_x,mouse_y):
    if self.next_button.rect.collidepoint(mouse_x,mouse_y):
      self.blocks.set_status(self.core.get_next_state())
    if self.start_button.rect.collidepoint(mouse_x,mouse_y):
      self.running=True
    if self.stop_button.rect.collidepoint(mouse_x,mouse_y):
      self.running=False

  def draw(self):
    self.blocks.draw_board()
    pygame.display.flip()
  def run_game(self):
    while True:
        for event in pygame.event.get():  #检测键盘鼠标事件
            if event.type==pygame.QUIT:
                sys.exit() #退出程序
            elif event.type==pygame.MOUSEBUTTONDOWN:#检测鼠标点击事件
                  mouse_x,mouse_y=pygame.mouse.get_pos() #get_pos()返回一个单击时鼠标的xy坐标
                  if(mouse_x<self.blocks_right):
                    self.click_block(mouse_x,mouse_y)
                  else:
                    self.click_button(mouse_x,mouse_y)
            self.draw()
if __name__ == '__main__':
  gol=GameOfLife()
  gol.run_game()