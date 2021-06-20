from tech_product import Tech
class Laptop(Tech):
    def __init__(self,name,price,weight,color,ram,cpu,storage):
        super().__init__(name,price,weight,color)
        self.ram = ram
        self.cpu = cpu
        self.storage = storage
    #method-1
    def set_double_price(self):
        self.price = self.price * 2
        print("Double Price : ",self.price)
    #method-2
    def change_specs(self,ram,storage):
        if ram > self.ram or storage > self.storage:
            self.price = self.price + 10000
            print("Higher ram & storage price : ",self.price)
            #self.ram = ram
            #self.storage = storage
        else:
            print("Cheaper ram & storage price : ",self.price)
    def __str__(self):
        return f'Name : {self.name}\nPrice : {self.price}\nWeight : {self.weight}\nColor : {self.color}\nRam : {self.ram}\nStorage : {self.storage}'



