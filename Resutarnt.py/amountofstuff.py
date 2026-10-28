class Restaurant:

    def __init__(self):
        self.stock = {
            "Burger": 10,
            "Chips": 15,
            "Chicken": 10,
            "Salad": 8,
            "Cola": 20,
            "Water": 20
        }

    def ShowReport(self):

        print("\n--- RESTAURANT REPORT ---")

        for item, amount in self.stock.items():

            if amount == 0:
                print(f"{item}: OUT OF STOCK")
            else:
                print(f"{item}: {amount} left")

    def CheckStock(self, item):

        if item not in self.stock:
            return False

        if self.stock[item] <= 0:
            return False

        return True

    def RemoveStock(self, item):

        if self.CheckStock(item):
            self.stock[item] -= 1
            return True

        return False

    def AddStock(self, item, amount):

        if item in self.stock:
            self.stock[item] += amount