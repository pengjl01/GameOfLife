# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 13:40:03 2019

@author: pjl
"""
class Core:
  
  def __init__(self,r,c):
    self.__now_state = [[False for x in range(c)] for i in range(r)]
    self.__next_state = [[False for x in range(c)] for i in range(r)]
    
  #变更第r行c列细胞的状态
  def change_block(self,r,c):
    try:
      self.__now_state[r][c]^=1
    except IndexError:pass
  
  #获取第r行c列细胞周围存活细胞的个数
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
  
  #获取下一个时刻所有细胞的存活状态
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
          else:
            self.__next_state[r][c]=False
    self.__now_state,self.__next_state=self.__next_state,self.__now_state
    return self.__now_state
  
  #获取当前状态
  def get_now_state(self):
    return self.__now_state
  
  #增加生命
  def add_life(self,r,c,data):
    if r+len(data)<=len(self.__now_state)and c+len(data[0])<=len(self.__now_state[0]):
      for i in range(len(data)):
        for j in range(len(data[0])):
          self.__now_state[r+i][c+j]=data[i][j]
#      self.__now_state[r:r+len(data)][c:c+len(data[0])] = data[:]
#      print(self.__now_state[r:r+len(data)][c:c+len(data[0])])
      
  #将当前时刻所有细胞设置为死亡
  def clear(self):
    for r in range(len(self.__now_state)):
      for c in range(len(self.__now_state[0])):
        self.__now_state[r][c]=False
    return