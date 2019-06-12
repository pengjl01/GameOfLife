# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 13:40:03 2019

@author: pjl
"""
def get_live_num(r, c, pre):
  sum=0
  if r == 0 and c == 0:
    sum += pre[r][c+1]
    sum+= pre[r+1][c]
    sum +=pre[r+1][c+1]
  elif r == 0 and c == len(pre[0]) - 1:
    sum+=pre[r][c-1]
    sum+=pre[r+1][c-1]
    sum+=pre[r+1][c]
  elif r==len(pre)-1 and c==0:
    sum+=pre[r-1][c]
    sum+=pre[r-1][c+1]
    sum+=pre[r][c+1]
  elif r==len(pre)-1 and c==len(pre[0])-1:
    sum+=pre[r-1][c-1]
    sum+=pre[r-1][c]
    sum+=pre[r][c-1]
  elif r==0:
    sum+=pre[r][c-1]
    sum+=pre[r][c+1]
    sum+=pre[r+1][c-1]
    sum+=pre[r+1][c]
    sum+=pre[r+1][c+1]
  elif r==len(pre)-1:
    sum+=pre[r-1][c-1]
    sum+=pre[r-1][c]
    sum+=pre[r-1][c+1]
    sum+=pre[r][c-1]
    sum+=pre[r][c+1]
  elif c==0:
    sum+=pre[r-1][c]
    sum+=pre[r-1][c+1]
    sum+=pre[r][c+1]
    sum+=pre[r+1][c]
    sum+=pre[r+1][c+1]
  elif c==len(pre[0])-1:
    sum+=pre[r-1][c-1]
    sum+=pre[r-1][c]
    sum+=pre[r][c-1]
    sum+=pre[r+1][c-1]
    sum+=pre[r+1][c]
  else:
    sum+=pre[r-1][c-1]
    sum+=pre[r-1][c]
    sum+=pre[r-1][c+1]
    sum+=pre[r][c-1]
    sum+=pre[r][c+1]
    sum+=pre[r+1][c-1]
    sum+=pre[r+1][c]
    sum+=pre[r+1][c+1]
  return sum


def next_state(pre,after):
  for r in range(len(pre)):
    for c in range(len(pre[0])):
      num=get_live_num(r, c, pre)
      if pre[r][c]==0:
        if num==3:
          after[r][c]=1
      else:
        if num==2 or num==3:
          after[r][c]=1
        else:
          after[r][c]=0
        
if __name__ =='__main__':
  pre = [[0 for x in range(5)] for i in range(5)]
  pre[2][1] = 1
  pre[2][2] = 1
  pre[2][3] = 1
  after =[[0 for x in range(5)] for i in range(5)]
  for i in range(10):
    next_state(pre,after)
    temp=pre
    screen=after
    after=temp
    for i in range(len(screen)):
      print(screen[i])
    print('\n')