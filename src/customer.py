
class Customer:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness = 0

    def buy_drink(self, drink):
        self.wallet -= drink.price

    def buy_food(self, food):
        self.wallet -= food.price

    def increase_drunkenness_level(self, drink):
        self.drunkenness += drink.alcohol_level

    def decrease_drunkenness_level(self, food):
        if self.drunkenness == 0:
            pass
        elif self.drunkenness < food.rejuvenation:
            self.drunkenness = 0
        else:
            self.drunkenness -= food.rejuvenation
    



    

        
