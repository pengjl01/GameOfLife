# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 14:54:09 2019

@author: pjl
"""

import unittest

from core import get_live_num
from core import next_state

class TestCore(unittest.TestCase):
 
  def test_get_live_num(self): 
    pre=[[0,0,0],[1,1,1],[0,0,0]]
    self.assertEqual(get_live_num(0,0,pre),2)
    self.assertEqual(get_live_num(0,1,pre),3)
    self.assertEqual(get_live_num(0,2,pre),2)
    self.assertEqual(get_live_num(1,0,pre),1)
    self.assertEqual(get_live_num(1,1,pre),2)
    self.assertEqual(get_live_num(1,2,pre),1)
    self.assertEqual(get_live_num(2,0,pre),2)
    self.assertEqual(get_live_num(2,1,pre),3)
    self.assertEqual(get_live_num(2,2,pre),2)
  def test_next_state(self):
    pre = [[0 for x in range(5)] for i in range(5)]
    pre[2][1] = 1
    pre[2][2] = 1
    pre[2][3] = 1
    after =[[0 for x in range(5)] for i in range(5)]
    ans =[[0 for x in range(5)] for i in range(5)]
    ans[1][2] = 1
    ans[2][2] = 1
    ans[3][2] = 1
    next_state(pre,after)
    self.assertEqual(ans,after)
    
if __name__ == '__main__':
    unittest.main()