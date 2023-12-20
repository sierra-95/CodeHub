#!/usr/bin/env python3

from models.my_list import MyList as my
import unittest

class TestList(unittest.TestCase):

    def setUp(self):
        self.my_list = my()
        #cant test random numbers using randint
        self.my_list.append(1)
        self.my_list.append(4)
        self.my_list.append(2)
        self.my_list.append(3)
        self.my_list.append(5)
    def testResult(self):
        self.my_list.print_sorted()
        self.assertEqual(self.my_list,[1,2,3,4,5])    