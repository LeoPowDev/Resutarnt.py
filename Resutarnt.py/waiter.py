class Waiter:
    def __init__(self, name, role, table):
        self.name = name
        self.role = role
        self.table = table

    def Talking(self):
        print(f"{self.name}: Hello there. Welcome to Aura-Maxing Restaurant.")

    def TakeSeat(self):
        print(f"{self.name}: Please take a seat at table {self.table}.")

    def Introduce(self):
        print(
            f"{self.name}: My name is {self.name}, "
            f"and I will be your {self.role} today."
        )

    def TakeOrder(self):
        print(f"{self.name}: I will take your order shortly.")

    def CheckTable(self):
        print(f"{self.name}: I am checking table {self.table}.")

    def ThankCustomer(self):
        print(f"{self.name}: Thank you for dining with us!")