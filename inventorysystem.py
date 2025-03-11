class Item:
    def __init__(self, id, name, quantity, price):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.price = price

class Inventory:
    def __init__(self):
        self.Item
    
    def AddItem():
        return

def Main():
    inventory = Inventory()
    
    while True:
        print("Inventory Management System \n1. Add Item \n2. Update Quantity \n3. View Inventory \n4.Exit")
        
        choice = input("What function would you like to use?")
        
        if choice == '1' or 'add':
            id = int(input("Enter item ID: "))
            name = input("Enter item name: ")
            quantity = int(input("Enter item quantity: "))
            price = float(input("Enter item price: "))
            inventory.add_item(id, name, quantity, price)
        
        elif choice == '2' or 'update':
            id = int(input("Enter item ID: "))
            quantity = int(input("Enter new item quantity: "))
            inventory.update_quantity(id, quantity)
        
        elif choice == '3' or 'view':
            read(inventory)
            close()
        
        elif choice == '4' or 'exit':
            exit()