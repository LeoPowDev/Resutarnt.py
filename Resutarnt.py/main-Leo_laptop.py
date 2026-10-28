from prettytable import PrettyTable

from Reception import Reception
from waiter import Waiters1
from order import Order
from menu import Menu
from cooker import Cooker
from chefs import Chef
from Manager import Manager
from amountofstuff import Restaurant

restaurant = Restaurant()

reception = Reception("TestSubject(Reception)", "Receptionist")

reception.Greeting()
reception.Introduce()
reception.ShowTable()

while True:

    name = input("What is your name? ").strip()

    if name.lower() == "report":
        restaurant.ShowReport()
        continue

    if name == "Name":
        print("You found a secret easteregg the first part of the code is: 1 when u have the full code of 3 type it in the name")
        break

    if name == "53321":
        print("You found, a golden coin: 🪙🪙🪙🪙🪙🪙🪙🪙🪙🪙🪙🪙🪙")



    if not name:
        print("Invalid choice, please try again.")
        continue

    break

while True:

    table_number = input("What table are you sitting at? ").strip()

    if table_number.lower() == "report":
        restaurant.ShowReport()
        continue

    if not table_number.isdigit():
        print("Invalid choice, please try again.")
        continue

    if table_number == "67":
        print("You found a secret easteregg the first part of the code is: 1 when u have the full code of 5 type it in the name")
        break

    break

Gender = ["1", "2","LOL"]

while True:

    table = PrettyTable()

    table.add_column("Sir", ["2"])
    table.add_column("Madam", ["1"])

    print(table)

    gender = input("Are you a madam or sir? Please say: 1 or 2: ").strip()

    if gender == "LOL":
        print("You found a secret easteregg the first part of the code is: 1 when u have the full code of 321 type it in the name")
        break

    

    if gender.lower() == "report":
        restaurant.ShowReport()
        continue

    if gender not in Gender:
        print("Invalid choice, please try again.")
        continue

    break

waiter = Waiters1("TestSubject(Waiter)", "Waiter", table_number)

waiter.Talking()
waiter.Introduce()
waiter.TakeSeat()

print(f"Gender choice: {gender}")
print(f"Welcome, {name}!")

menu = Menu()
order = Order()

while True:

    menu.ShowMenu()

    item = input("\nWhat would you like to order? ").strip()

    if item.lower() == "report":
        restaurant.ShowReport()
        continue

    price = menu.GetPrice(item)

    if price is None:
        print("Sorry, that item is not on the menu.")
        continue

    if not restaurant.CheckStock(item):
        print(f"Sorry, {item} is out of stock.")
        continue

    order.AddItem(item, price)
    restaurant.RemoveStock(item)

    print(f"{item} has been added to your order.")

    while True:

        another = input(
            "Would you like to order anything else? (yes/no): "
        ).strip().lower()

        if another == "report":
            restaurant.ShowReport()
            continue

        if another == "yes":
            break

        if another == "no":
            break

        print("Invalid choice, please try again.")

    if another == "no":
        break

order.ShowOrder()

print(f"\nTotal: £{order.GetTotal():.2f}")

chef = Chef("TestSubject(Chef)", "Chef")

chef.Introduce()
chef.TakeOrder(order)
chef.ShowOrder()
chef.MakeFood()
chef.FinishOrder()

cooker = Cooker("TestSubject(Cooker)", "Cooker")

cooker.Introduce()
cooker.MakeOrder(order)
cooker.FinishOrder()

manager = Manager("TestSubject(Manager)", "Manager")

manager.Introduce()
manager.ShowReport(restaurant)
manager.CheckStock(restaurant)

print(f"Thank you, {name}!")
