#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from models.say_my_name import say_my_name as say
import unittest
class testSayName(unittest.TestCase):
    
    def testStrings(self):
        self.assertEqual(say("Michael","Machohi"),"My name is Michael Machohi")
    def testNon_strings(self):
        self.assertRaises(TypeError,say,1,2)
    def testcombined(self):
        self.assertRaises(TypeError,say,"mike",2)    


if __name__=="__main__":
    unittest.main()        