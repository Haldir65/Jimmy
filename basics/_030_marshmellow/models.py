class Factory():
    def __init__(self, name, location,products):
        self.name = name
        self.location = location
        self.registed_time = dt.datetime.now()
        self.products= products


class Product():
    def __init__(self,name,price):
        self.name= name
        self.price = price        


class Computer():
    def __init__(self,name,model):
        self.name= name
        self.model = model