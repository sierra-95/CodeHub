#!/usr/bin/env python3
from models.nokia_users import Users
import unittest

class TestNokia(unittest.TestCase):

    def setUp(self):
        self.user1=Users("Michael","Machohi","Lumia","5.0")

    def testGetname(self):
        self.assertEqual(self.user1.get_name(),'Confirmed Michael Machohi')  
    def testresponse(self):
        self.assertEqual(self.user1.response(),'Your phone is Lumia version:5.0')

    def testSetname(self):
        self.user2 = Users('Joseph','Kimani', 'Samsung', 4)
        self.assertEqual(self.user2.get_name(),'Confirmed Joseph Kimani')