from tech_product import Tech
class Mobile(Tech):
    def __init__(self,name,price,weight,color,screen,camera):
        super().__init__(name,price,weight,color)
        self.screen = screen
        self.camera = camera
    #overriding apply_discount() method from Tech class
    def apply_discount(self):
        self.price = int(self.price - (self.price * (super().discount/2)))
        print("After Overrinding : ",self.price)
    def __str__(self):
        return f'Name : {self.name}\nPrice : {self.price}\nWeight : {self.weight}\nColor : {self.color}\nScreen : {self.screen}\nCamera : {self.camera}'
