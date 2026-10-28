class Chef:

    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.orders = []

    def Introduce(self):
        print(f"{self.name}: My name is {self.name}, and I am the {self.role}.")

    def TakeOrder(self, order):

        self.orders.append(order)

        print(f"{self.name}: I have received the order.")

    def ShowOrder(self):

        print("\n--- CHEF ORDER ---")

        if not self.orders:
            print("There are no orders.")
            return

        for order in self.orders:

            for item in order.items:

                print(f"{item['item']}: £{item['price']:.2f}")

    def MakeFood(self):

        print("\n--- CHEF ---")

        if not self.orders:
            print("There are no orders to make.")
            return

        for order in self.orders:

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
                    print(f"{self.name}: Getting {food}.")

                elif food == "Water":
                    print(f"{self.name}: Getting {food}.")

                else:
                    print(f"{self.name}: I don't know how to make {food}.")

    def FinishOrder(self):

        print(f"{self.name}: The order is finished and ready to be served.")