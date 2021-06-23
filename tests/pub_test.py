import unittest

from src.pub import *
from src.customer import *
from src.drink import *

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)
        self.customer = Customer("Frodo", 15.00)
        self.customer = Customer("Samwise", 10.00)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    
    