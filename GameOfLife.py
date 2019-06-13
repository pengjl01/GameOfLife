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
import time
import rle
#设置行数/列数/块大小
r=80
c=120
block_size=10
#r=40
#c=70
#block_size=20
bg_color=(230,230,230)
class GameOfLife:
  def __init__(self):
    pygame.init()  #初始化背景设置
    self.blocks_right=c*(block_size+1)#计算方格区右边界
    height=r*(block_size+1)
    if height<300:
      height=300 #保证按键显示完全
    self.screen=pygame.display.set_mode((self.blocks_right+100,height))
    pygame.display.set_caption("Game Of Life")  #设置标题
    self.screen.fill(bg_color)
    self.core=Core(r,c)
    self.__init_lives()
    self.blocks=Blocks(r,c,block_size,self.screen,self.core.get_now_state())
    self.blocks.draw_board()
    self.running=False
    self.time=time.time()
    self.__add_buttons()
    self.speed=1
    
    return
  #添加初始生命
  def __init_lives(self):
    self.core.add_life(1,1,rle.glider)
    self.core.add_life(15,10,rle.blinker)
    self.core.add_life(20,10,rle.toad)
    self.core.add_life(10,80,rle.HWSS)
    self.core.add_life(30,0,rle.glider_generater)
    self.core.add_life(30,40,rle.glider_generater)
  #添加按键
  def __add_buttons(self):
    self.next_button=Button(self.blocks_right+10,20,self.screen,'next')
    self.start_button=Button(self.blocks_right+10,80,self.screen,'start')
    self.stop_button=Button(self.blocks_right+10,140,self.screen,'stop')
    self.speed_up_button=Button(self.blocks_right+10,200,self.screen,'speed up')
    self.speed_down_button=Button(self.blocks_right+10,260,self.screen,'speed down')
    self.next_button.draw_button()
    self.start_button.draw_button()
    self.stop_button.draw_button()
    self.speed_up_button.draw_button()
    self.speed_down_button.draw_button()
  #点击方格区
  def click_block(self,mouse_x,mouse_y):
    r=int(mouse_y/(block_size+1))
    c=int(mouse_x/(block_size+1))
    self.core.change_block(r,c)
    self.blocks.click(r,c)
  #点击按键区
  def click_button(self,mouse_x,mouse_y):
    if self.next_button.rect.collidepoint(mouse_x,mouse_y):
      self.blocks.set_status(self.core.get_next_state())
    if self.start_button.rect.collidepoint(mouse_x,mouse_y):
      self.running=True
    if self.stop_button.rect.collidepoint(mouse_x,mouse_y):
      self.running=False
    if self.speed_up_button.rect.collidepoint(mouse_x,mouse_y):
      if self.speed<20:
        self.speed+=1
    if self.speed_down_button.rect.collidepoint(mouse_x,mouse_y):
      if self.speed>1:
        self.speed-=1
    return
  #添加按键
  def draw(self):
    self.blocks.draw_board()
    pygame.display.flip()
  #运行游戏
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
      if self.running:
        nowtime=time.time()
        if nowtime-self.time>(1/self.speed):
          self.time=nowtime
          self.blocks.set_status(self.core.get_next_state())
      self.draw()
if __name__ == '__main__':
  gol=GameOfLife()
  gol.run_game()