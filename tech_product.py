class Tech:
    #class variable
    total_products = 0
    discount = 0.5
    #creating 
    def __init__(self,name,price,weight,color):
        self.name = name
        self.price = price
        self.weight = weight
        self.color = color
        Tech.total_products = Tech.total_products + 1
    #creating all the methods
    #method-1
    def apply_discount(self):
        self.price = int(self.price - (self.price * self.discount))
    #method-2
    def calculate_shipping_cost(self,rate):
        shipping_cost = self.weight * rate
        return shipping_cost
    #method-3(classmethod)
    @classmethod
    def all_products(cls):
        return 'Total number of products are : '+ str(cls.total_products)
    def __str__(self):
        return f'Name : {self.name}\nPrice : {self.price}\nWeight : {self.weight}\nColor : {self.color}'

    