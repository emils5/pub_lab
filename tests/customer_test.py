import unittest
from src.customer import *
from src.drink import *
from src.food import *

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer1 = Customer("Frodo", 15.00, 21)
        self.beer = Drink("Beer", 3.50, 3)
        self.burger = Food("Burger", 7.00, 2)

    def test_customer_name(self):
        self.assertEqual("Frodo", self.customer1.name)

    def test_default_drunkenness_level_default(self):
        self.assertEqual(0, self.customer1.drunkenness)

    def test_customer_can_buy_drink(self):
        self.customer1.buy_drink(self.beer)
        self.assertEqual(11.50, self.customer1.wallet)
    
    def test_drunkenness_level_can_increase(self):
        self.customer1.increase_drunkenness_level(self.beer)
        self.assertEqual(3, self.customer1.drunkenness)
    
    def test_customer_can_buy_food(self):
        self.customer1.buy_food(self.burger)
        self.assertEqual(8, self.customer1.wallet)