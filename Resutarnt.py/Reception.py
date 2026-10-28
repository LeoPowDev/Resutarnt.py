from prettytable import PrettyTable

class Reception:

    def __init__(self, name, role):
        self.name = name
        self.role = role

    def Greeting(self):
        print(f"{self.name}: Hello and welcome to Aura-Maxing Restaurant.")

    def Introduce(self):
        print(f"{self.name}: My name is {self.name}, and I am the {self.role}.")

    def Registration(self):

        while True:

            name = input("What is your name? ").strip()

            if not name:
                print("Invalid choice, please try again.")
                continue

            table_number = input("What table are you sitting at? ").strip()

            if not table_number.isdigit():
                print("Invalid choice, please try again.")
                continue

            return name, table_number

    def ShowTable(self):

        table = PrettyTable()

        table.add_column("Reception", ["Welcome"])

        print(table)