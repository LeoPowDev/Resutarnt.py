class Waiters1:

    def __init__(self, name, role, table):
        self.name = name
        self.role = role
        self.table = table

    def Talking(self):
        print(f"{self.name}: Hello there.")

    def TakeSeat(self):
        print(f"{self.name}: Please take a seat at table {self.table}.")

    def Introduce(self):
        print(f"{self.name}: My name is {self.name}, and I will be your {self.role} today.")