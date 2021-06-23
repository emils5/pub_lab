class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []
        self.customers = []
        self.drinks_sold = 0
        self.drunkenness_tolerance = 6

    
    def add_drink_to_pub(self, drink):
        self.drinks.append(drink)
    
    def add_customer_to_pub(self, customer_to_add): 
        self.customers.append(customer_to_add)
    
    def find_customer_by_name(self, customer):
        if customer.name:
            return customer.name
    
    def sell_item(self, item):
        self.till += item.price
    
    def check_customer_age(self, customer):
        if customer.age >= 18:
            return True
        else:
            return False
    
    
    def drink_transaction(self, customer, drink):
        if self.check_customer_age(customer) and customer.drunkenness < self.drunkenness_tolerance:
            self.sell_item(drink)
            customer.buy_item(drink)
            customer.drunkenness += drink.alcohol_level
            return True
        else:
            return False
        
    def food_transaction(self,customer, meal):
        if customer.wallet >= meal.price:
            self.sell_item(meal)
            customer.buy_item(meal)
            customer.drunkenness -= meal.rejuvenation










# if class(item) == Drink:
#     if self.check_customer_age and sdflkjsdfl;kasdflkasdf


# elif class(item) == Food:
#     lsdkfjas;ldkfjas;ldkfjasldkfjas



