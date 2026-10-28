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

                if food in ["Burger", "Chips", "Chicken", "Salad"]:
                    print(f"{self.name}: Making {food}.")
                elif food in ["Cola", "Water"]:
                    print(f"{self.name}: Getting {food}.")
                else:
                    print(f"{self.name}: I don't know how to make {food}.")

    def HelpChef(self, levels):
        print("\n--- HELP THE CHEF ---")
        print("The chef needs help preparing the order.")

        choice = input(
            "Do you want to help the chef? (yes/no): "
        ).strip().lower()

        if choice == "yes":
            print("You helped the chef prepare the order.")
            levels.Achievement("Kitchen Helper", 50)

        elif choice == "no":
            print("You decided not to help the chef.")

        else:
            print("Invalid choice.")

    def FinishOrder(self):
        print(f"{self.name}: The order is finished and ready to be served.")