import unittest

from src.pub import *
from src.customer import *
from src.drink import *
from src.food import *

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)
        self.customer1 = Customer("Frodo", 15.00, 21)
        self.customer2 = Customer("Samwise", 10.00, 16)
        self.beer = Drink("Beer", 3.50, 3)
        self.burger = Food("Burger", 7, 2)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)
    
    def test_pub_till_balance(self):
        self.assertEqual(100.00, self.pub.till)
    
    def test_add_drink_to_pub(self):
        self.pub.add_drink_to_pub(self.beer)
        self.assertEqual(1, len(self.pub.drinks))
    
    def test_add_customer_to_pub(self):
        self.pub.add_customer_to_pub(self.customer1)
        self.assertEqual(1, len(self.pub.customers))
    
    def test_find_customer_by_name(self):
        self.pub.add_customer_to_pub(self.customer1)
        self.assertEqual("Frodo", self.pub.find_customer_by_name(self.customer1))
    
    def test_sell_drink(self):
        self.pub.sell_drink(self.beer)
        self.assertEqual(103.50, self.pub.till)
    
    def test_check_customer_age(self):
        self.assertEqual(True, self.pub.check_customer_age(self.customer1))
        self.assertEqual(False, self.pub.check_customer_age(self.customer2))

    def test_drink_transaction_for_age(self):
        customer = self.customer1
        drink = self.beer
        self.assertEqual(True, self.pub.drink_transaction(customer, drink))
    
    def test_refused_transaction_for_age(self):
        customer = self.customer2
        drink = self.beer
        self.assertEqual(False, self.pub.drink_transaction(customer, drink))

    def test_refused_transaction(self):
        customer = Customer("David", 15, 31)
        self.assertEqual(True, self.pub.drink_transaction(customer, self.beer))
        self.assertEqual(True, self.pub.drink_transaction(customer, self.beer))
        self.assertEqual(False, self.pub.drink_transaction(customer, self.beer))
        
    def test_rejuvenation(self):
        customer = Customer("David", 15, 31)
        self.assertEqual(True, self.pub.drink_transaction(customer, self.beer))
        self.assertEqual(True, self.pub.drink_transaction(customer, self.beer))
        self.pub.food_transaction(customer, self.burger)     
        self.assertEqual(True, self.pub.drink_transaction(customer, self.beer))
       
        




# function to sell drink - inside the pub
    # remove money from customer, give to the pub




# test pub till
# test pub drinks
# test customer by name
# test customer's wallet

# test add money to till
# test remove money from customer


    