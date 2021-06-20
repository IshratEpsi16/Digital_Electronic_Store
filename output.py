from tech_product import Tech
from laptop_tech import Laptop
from mobile_tech import Mobile
from sales_person import SalesPerson
from datetime import date

#Tech class
#object/instance of Tech class
t1 = Tech('Asus g14',130000,1.6,'Moonlight Silver')
t2 = Tech('HP',150000,2.6,'Black')

#apply_discount() method
print(f"Before discount {t1.name} price is : ",t1.price)
t1.apply_discount() #calling apply_discount function
print(f"After discount {t1.name} price is : ",t1.price)
#calculate_shipping_cost() method
print("Shipping cost for your product is : ",t1.calculate_shipping_cost(10))
#all_products() method
print(t1.all_products())

#Laptop class
#object of Laptop class
l1 = Laptop('Asus g14',130000,1.6,'Moonlight Silver',16,'Ryzen 4800H',1000)
#set_double_price() method
print("Price : ",l1.price)
print(l1.set_double_price())
#change_specs() method
print(l1.change_specs(19,20000))


#Mobile Class
#object of mobile class
m1 = Mobile('iphone_11',60000,500,'Black',1920-1080,10)
#apply_discount() method
print(m1.apply_discount())
 

#SalesPerson class
#objects of SalesPerson class
s1 = SalesPerson("Ishrat","Jahan",10000,date(2021,10,5))
s1.sell_products(t1)
print(s1.total_products_sold())
print(s1.display_sales())
print(s1.calculate_commission(0.2))
print(s1.calculate_sales())
s1.sort_by_price()




