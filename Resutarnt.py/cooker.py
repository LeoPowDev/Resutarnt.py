class Cooker:

    def __init__(self, name, role):
        self.name = name
        self.role = role

    def Introduce(self):
        print(f"{self.name}: My name is {self.name}, and I am the {self.role}.")

    def MakeOrder(self, order):

        print("\n--- COOKER ---")

        for item in order.items:

            food = item["item"]

            if food == "Burger":
                print(f"{self.name}: Making {food}.")

            elif food == "Chips":
                print(f"{self.name}: Making {food}.")

            elif food == "Chicken":
                print(f"{self.name}: Making {food}.")

            elif food == "Salad":
                print(f"{self.name}: Making {food}.")

            elif food == "Cola":
                print(f"{self.name}: Giving {food}.")

            elif food == "Water":
                print(f"{self.name}: Giving {food}.")

            else:
                print(f"{self.name}: I don't know how to make or give {food}.")

    def FinishOrder(self):
        print(f"{self.name}: The order is ready.")