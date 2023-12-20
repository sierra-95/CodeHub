#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
def add(a,b):
    return (a+b)

class TestAddFunction(unittest.TestCase):

    def test_positive(self):
        result=add(3,5)
        self.assertEqual((result), 8)
    def test_negative(self):
        result=add(-2,-3)
        self.assertEqual(result,-5)    
    def test_combined(self):
        result=add(10,-3)
        self.assertEqual(result,7)

if __name__=="__main__":
    unittest.main()          
