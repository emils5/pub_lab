class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []
        self.customers = []
    
    def add_drink_to_pub(self, drink):
        self.drinks.append(drink)
    
    def add_customer_to_pub(self, customer_to_add):
        self.customers.append(customer_to_add)




