

class Manager:

    def __init__(self, name, role):
        self.name = name
        self.role = role

    def Introduce(self):
        print(f"{self.name}: My name is {self.name}, and I am the {self.role}.")

    def ShowReport(self, restaurant):
        print(f"{self.name}: Here is the restaurant report.")
        restaurant.ShowReport()

    def CheckStock(self, restaurant):

        print("\n--- STOCK CHECK ---")

        for item, amount in restaurant.stock.items():

            if amount == 0:
                print(f"{item}: OUT OF STOCK")

            elif amount <= 3:
                print(f"{item}: LOW STOCK ({amount} left)")

            else:
                print(f"{item}: {amount} left")

    def AddStock(self, restaurant):

        while True:

            item = input("What item would you like to add stock for? ").strip()

            if item.lower() == "report":
                restaurant.ShowReport()
                continue

            if item not in restaurant.stock:
                print("Invalid choice, please try again.")
                continue

            amount = input("How much would you like to add? ").strip()

            if not amount.isdigit():
                print("Invalid choice, please try again.")
                continue

            if int(amount) <= 0:
                print("Invalid choice, please try again.")
                continue

            restaurant.AddStock(item, int(amount))

            print(f"{amount} {item}(s) have been added.")

            break