#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test file for base_geometry.py"""
from models.base_geometry import BaseGeometry as base
from models.base_geometry import Rectangle as r
from models.base_geometry import square as s
import unittest
class TestData_types(unittest.TestCase):
    def setUp(self):
        #you must create an object instance of a class to test it
        #note the () of base()
        #this is because base_geometry function lacks def __init__
        self.test=base()
        self.object1=r(5,6)
        self.object2=s(13)
    def testAreaException(self):
        self.assertRaises(Exception,self.test.area)    
    def testString(self):
        self.assertRaises(TypeError,self.test.integer_validator,"mike","john")
    def testZero(self):
        self.assertRaises(ValueError,self.test.integer_validator,"mike",0)
        self.assertRaises(ValueError,self.test.integer_validator,"mike",-2)
    def testRectangle_neg_str(self):
        self.assertRaises(ValueError,r,-2,3)
        self.assertRaises(TypeError,r,2,"Frashia")
    def testRectangle(self):
        #str() will always check for the response
        #for __str__ eg print(s) --> to print __str__ in terminal
        #or str(self.object1) during testing--> self.assertEqual()
        self.assertEqual(self.object1.area(),30)
        self.assertEqual(str(self.object1),"[Rectangle] 5/6")
    def testSquare_neg_str(self):
        self.assertRaises(ValueError,s,-2)
        self.assertRaises(TypeError,s,"Frashia")
    def testSquare(self):
        self.assertEqual(self.object2.area(),169)
        self.assertEqual(str(self.object2),"[Square] 13/13")                