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
    
    def test_pub_till_balance(self):
        self.assertEqual(100.00, self.pub.till)
    
    def test_add_drink_to_pub(self):
        drink = Drink("Beer", 3.50)
        self.pub.add_drink_to_pub(drink)
        self.assertEqual(1, len(self.pub.drinks))

    



# test pub till
# test pub drinks
# test customer by name
# test customer's wallet


    