#!/usr/bin/env python3
from models.add_numbers import add
import unittest
class TestAddition(unittest.TestCase):

    def test_add_positive(self):
        result=add(3,5)
        self.assertEqual(result,8)
    def test_add_negative(self):
        result=add(-2,-5)
        self.assertEqual(result,-7)


        
