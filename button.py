# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 23:14:09 2019

@author: pjl
"""
import pygame.font
button_width=80
button_height=40
class Button():
  def __init__(self,left,top,screen,msg):
    self.msg=msg
    self.screen=screen
    self.button_color=(192,255,62)
    self.text_color=(125,38,205)
    self.rect=pygame.Rect(left,top,button_width,button_height)
    self.font=pygame.font.SysFont(None,25)
    self.deal_msg(msg)
    
  def deal_msg(self,msg):       
    self.msg_img=self.font.render(msg,True,self.text_color,self.button_color)
    self.msg_img_rect=self.msg_img.get_rect()
    self.msg_img_rect.center=self.rect.center
      
  def draw_button(self):
    self.screen.fill(self.button_color,self.rect)
    self.screen.blit(self.msg_img,self.msg_img_rect)
