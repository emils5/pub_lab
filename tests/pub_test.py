import unittest

from src.pub import *
from src.customer import *
from src.drink import *

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)
        self.customer1 = Customer("Frodo", 15.00)
        self.customer2 = Customer("Samwise", 10.00)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)
    
    def test_pub_till_balance(self):
        self.assertEqual(100.00, self.pub.till)
    
    def test_add_drink_to_pub(self):
        drink = Drink("Beer", 3.50)
        self.pub.add_drink_to_pub(drink)
        self.assertEqual(1, len(self.pub.drinks))
    
    def test_add_customer_to_pub(self):
        self.pub.add_customer_to_pub(self.customer1)
        self.assertEqual(1, len(self.pub.customers))
    
    def test_find_customer_by_name(self):
        self.pub.add_customer_to_pub(self.customer1)
        self.assertEqual("Frodo", self.pub.find_customer_by_name(self.customer1))


    # def test_find_customer_by_name(self):
        

    

# add customer to the pub [list]
# find customer by name [for loop]
# find number of customers in the pub len()

# test pub till
# test pub drinks
# test customer by name
# test customer's wallet

# test add money to till
# test remove money from customer


    