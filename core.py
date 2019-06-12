# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 13:40:03 2019

@author: pjl
"""
class Core:
  
  def __init__(self,r,c):
    self.__now_state = [[False for x in range(c)] for i in range(r)]
    self.__next_state = [[False for x in range(c)] for i in range(r)]
    
  def change_block(self,r,c):
    try:
      self.__now_state[r][c]^=1
    except IndexError:pass
    
  def __get_live_num(self,r, c):
    sum=0
    try:
      sum+=self.__now_state[r-1][c-1]
    except IndexError:pass
    try:
      sum+=self.__now_state[r-1][c]
    except IndexError:pass
    try:
      sum+=self.__now_state[r-1][c+1]
    except IndexError:pass
    try:
      sum+=self.__now_state[r][c-1]
    except IndexError:pass
    try:
      sum+=self.__now_state[r][c+1]
    except IndexError:pass
    try:
      sum+=self.__now_state[r+1][c-1]
    except IndexError:pass
    try:
      sum+=self.__now_state[r+1][c]
    except IndexError:pass
    try:
      sum+=self.__now_state[r+1][c+1]
    except IndexError:pass
    return sum
  
  def get_next_state(self):
    for r in range(len(self.__now_state)):
      for c in range(len(self.__now_state[0])):
        num=self.__get_live_num(r, c)
        if self.__now_state[r][c]:
          if num==2 or num==3:
            self.__next_state[r][c]=True
          else:
            self.__next_state[r][c]=False
        else:
          if num==3:
            self.__next_state[r][c]=True
    self.__now_state,self.__next_state=self.__next_state,self.__now_state
    return self.__now_state
  
  def clear(self):
    for r in range(len(self.__now_state)):
      for c in range(len(self.__now_state[0])):
        self.__now_state[r][c]=False
    return