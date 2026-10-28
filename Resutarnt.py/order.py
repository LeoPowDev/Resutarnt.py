class Order:

    def __init__(self):
        self.items = []

    def AddItem(self, item, price):
        self.items.append({
            "item": item,
            "price": price
        })

    def ShowOrder(self):
        print("\nYour order")

        for order in self.items:
            print(f"{order['item']}: £{order['price']:.2f}")

    def GetTotal(self):
        total = 0

        for order in self.items:
            total += order["price"]

        return total