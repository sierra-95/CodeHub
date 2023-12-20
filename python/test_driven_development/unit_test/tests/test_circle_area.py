#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from models.circle_area import circle_areas
from math import pi
import unittest

class Test_circle_area(unittest.TestCase):

    def test_positive_numbers(self):
        result= circle_areas(2)
        self.assertAlmostEqual(result,pi*2*2)

    def tes_negative_numbers(self):
        result2=circle_areas(-2)
        self.assertRaises(ValueError,circle_areas,-2)

    def test_non_int(self):
        self.assertRaises(TypeError,circle_areas,"name")

