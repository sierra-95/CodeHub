#!/usr/bin/env python3
import unittest
#add = __import__('0-add_integer').add_integer
from models.add_integer import add_integer as add
class TestAdd(unittest.TestCase):

    def testPositive(self):
        result=add(2,3)
        self.assertEqual(result,5)
    def testnegative(self):
        result=add(-2,-3)
        self.assertEqual(result,-5)
    def testStrings(self):
        self.assertRaises(TypeError,add,"mike","mike")        