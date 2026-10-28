class Menu:

    def __init__(self):
        self.items = {
            "Burger": 8.99,
            "Chips": 3.50,
            "Chicken": 9.50,
            "Salad": 5.99,
            "Cola": 2.00,
            "Water": 1.50
        }

    def ShowMenu(self):
        print("\n--- MENU ---")

        for item, price in self.items.items():
            print(f"{item}: £{price:.2f}")

    def GetPrice(self, item):
        return self.items.get(item)