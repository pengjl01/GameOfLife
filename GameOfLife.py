# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 15:45:41 2019

@author: pjl
"""

import sys
import pygame
def draw_block(r,c,dead):
  if dead==0:
    pygame.draw.rect(screen,block_dead_color,[c*(block_size+1),r*(block_size+1),block_size,block_size],0)
  else:
    pygame.draw.rect(screen,block_life_color,[c*(block_size+1),r*(block_size+1),block_size,block_size],0)
def draw_data():
  for r in range(len(data)):
    for c in range(len(data[0])):
      draw_block(r,c,data[r][c])
def draw_buttom():
  buttom_width=30
  buttom_height=20
def draw():
  screen.fill(bg_color)
  draw_buttom()
  draw_data()
  pygame.display.flip()
def click_block(mouse_x,mouse_y):
  r=int(mouse_y/(block_size+1))
  c=int(mouse_x/(block_size+1))
  print("clicked "+str(r)+" "+str(c)+" "+str(data[r][c]))
  if data[r][c]==0:
    data[r][c]=1
  else:
    data[r][c]=0
#  draw()
  draw_block(r,c,data[r][c])
  pygame.display.flip()
def run_game():
  global bg_color
  global screen
  global data
  global block_size
  global block_dead_color
  global block_life_color
#  global block_area
  r=160
  c=240
  block_size=4
  data= [[0 for x in range(c)] for i in range(r)]
  data[100][100]=1
  data[100][101]=1
  data[100][102]=1
  bg_color=(230,230,230)
#  block_life_color=(255,255,255)
  block_life_color=(102,204,255)
  block_dead_color=(0,0,0)
  pygame.init()  #初始化背景设置
  screen_width=1200
  screen_height=800
  screen=pygame.display.set_mode((screen_width,screen_height)) #调用属性设置屏幕的宽高
  pygame.display.set_caption("Game Of Life")  #设置标题
  while True:
      for event in pygame.event.get():  #检测键盘鼠标事件
          if event.type==pygame.QUIT:
              sys.exit() #退出程序
          elif event.type==pygame.MOUSEBUTTONDOWN:#检测鼠标点击事件
                mouse_x,mouse_y=pygame.mouse.get_pos() #get_pos()返回一个单击时鼠标的xy坐标
                click_block(mouse_x,mouse_y)
          draw()
if __name__ == '__main__':
  run_game() 