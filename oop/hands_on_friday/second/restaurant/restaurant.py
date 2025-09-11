class Restaurant:


    menu = ["Salad", "Eba", "Semo", "Chips"]
    tables = 4
    tableassigned = 0


    def __init__(self, name, location):
        self.name = name
        self.location = location

class Nana(Restaurant):
    def __init__(self,res, customer, amount):
        Restaurant.__init__(self, res.name, res.location)
        self.res = res
        self.customer = customer
        self.amount = amount
        self.name=res.name

    def p_order(self, order):
        if order in Restaurant.menu:
            print("Oder passed")
            if Restaurant.tables > 0:
                Restaurant.tables -= 1
                Restaurant.tableassigned += 1
                return f"User ordered {order} and was assigned table {Restaurant.tableassigned} in {self.name}!"
            else:
                return "We are out of tables"
        else:
            return f"{self.order} is not on the Menu"


resss = Restaurant("Jade", "Masa")
customer1 = Nana(resss, "Steve", "Eba")
print(customer1.p_order("Eba"))
