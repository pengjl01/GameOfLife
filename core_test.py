# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 14:54:09 2019

@author: pjl
"""

import unittest

from core import Core
import rle

class TestCore(unittest.TestCase):
  
  def test_init(self):
    core=Core(3,4)#构造函数应该为core创建2个相同规格的数组
    self.assertEqual(len(core._Core__now_state),3)
    self.assertEqual(len(core._Core__now_state[0]),4)
    self.assertEqual(len(core._Core__next_state),3)
    self.assertEqual(len(core._Core__next_state[0]),4)
    
  def test_change_block(self):
    core=Core(2,2)
    core.change_block(0,0)
    core.change_block(1,1)
    self.assertTrue(core._Core__now_state[0][0])#反转后的值应该为True
    self.assertTrue(core._Core__now_state[1][1])
    core.change_block(1,1)
    self.assertFalse(core._Core__now_state[1][1])#2次反转后的值应该为False
    self.assertFalse(core._Core__next_state[0][0])#_Core__next_state不应该受到影响
    core.change_block(3,1)
    
  def test_get_live_num(self): 
    core=Core(3,3)
    core.change_block(0,1)
    core.change_block(1,0)
    core.change_block(1,1)
    self.assertEqual(core._Core__get_live_num(0,0),3)
    self.assertEqual(core._Core__get_live_num(0,1),2)
    self.assertEqual(core._Core__get_live_num(0,2),2)
    self.assertEqual(core._Core__get_live_num(1,0),2)
    self.assertEqual(core._Core__get_live_num(1,1),2)
    self.assertEqual(core._Core__get_live_num(1,2),2)
    self.assertEqual(core._Core__get_live_num(2,0),2)
    self.assertEqual(core._Core__get_live_num(2,1),2)
    self.assertEqual(core._Core__get_live_num(2,2),1)
    
  def test_clear(self):
    core=Core(2,2)
    core.change_block(0,1)
    core.change_block(1,0)
    core.clear()
    ans =[[0 for x in range(2)] for i in range(2)]
    self.assertEqual(core._Core__now_state,ans)#清空测试
    
  def test__Core__next_state(self):
    ans =[[0 for x in range(5)] for i in range(5)]
    ans[1][2] = True
    ans[2][2] = True
    ans[3][2] = True
    core=Core(5,5)
    core.change_block(2,1)
    core.change_block(2,2)
    core.change_block(2,3)
    self.assertEqual(core.get_next_state(),ans)#信号灯测试
  
  def test_add_life(self):
    ans =[[False for x in range(5)] for i in range(5)]
    ans[1][3] = True
    ans[2][1] = True
    ans[2][3] = True
    ans[3][2] = True
    ans[3][3] = True
    core=Core(5,5)
    core.add_life(1,1,rle.glider)
    self.assertEqual(core.get_now_state(),ans)#glider添加测试
    
    
if __name__ == '__main__':
    unittest.main()