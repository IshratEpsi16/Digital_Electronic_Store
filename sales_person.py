class SalesPerson:
    employee_id = 0
    def __init__(self,first_name,last_name,salary,date_joined):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.date_joined = date_joined
        self.list_of_products = []
        self.total_sales = 0
        SalesPerson.employee_id += 1
    def sell_products(self,product):

        self.list_of_products.append(product)
    def display_sales(self):
        print("All the products sold by salesman : ")
        for i in self.list_of_products:
            print("Products are : ",i)
    def calculate_sales(self):
        total = 0
        for j in self.list_of_products:
            total += j.price
        self.total_sales = total
        return total
    def calculate_commission(self,percentage):
        total = self.calculate_sales()
        return f'Total commission {total*percentage}'
    def total_products_sold(self):
        return f'Total number of products {len(self.list_of_products)}'
    def sort_by_price(self):
        def sorting(product):
            return product.price
        self.list_of_products.sort(key=lambda product:product.price, reverse=True)
    def __str__(self):
        return f'First Name : {self.first_name}\nLast Name : {self.last_name}\nSalary : {self.salary}\nJoining date : {self.date_joined}'

