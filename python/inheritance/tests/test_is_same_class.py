#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from models.is_same_class import is_same_class as same
import unittest
class TestSameClass(unittest.TestCase):
    def setUp(self):
        self.a=1
        self.b=2.5
        self.c="mike"
    def testInt(self):
        self.assertEqual(same(self.a,int),True)
    def testFloat(self):
        self.assertEqual(same(self.b,float),True)
    def testString(self):
        self.assertEqual(same(self.c,str),True)


