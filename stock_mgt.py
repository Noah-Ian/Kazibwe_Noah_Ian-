inventory = {}

def display_items():
     print("_Current Stock_")
     for item,quantity in inventory.items():
        print(f"{item}:{quantity}units")
def add_items():
    item = input("enter item name: ")
    if item in inventory:
        print("item already exists, Use the update option")
    else:
        quantity = int(input("enter quantity: "))
        inventory[item]=quantity
        print(f"{quantity}units of {item} were added")
        
def remove_items():
    item = input("enter item to remove: ")
    if item in inventory:
         quantity = int(input("enter quantity: "))
         if quantity <= inventory[item]:
             inventory[item]-=quantity
             print(f"{quantity}units of {item} were removed sucessfully")
         else:
             print("low stock detected")
    else:
        print("Item not found...")
        
def update_items():
    item = input("enter item to update: ")
    quantity = int(input("enter quantity to update: "))
    if item in inventory:
        inventory[item]+=quantity
    else:
        print("Item not found,Use the Add Option")
                       
while True:
        print("~~Inventory Management Menu~~")
        print("1.Display Items")
        print("2.Add Items")
        print("3.Remove Items")
        print("4.Update")
        print("5.Exit")
         
        choice = input("Enter your choice: ")
        
        if choice == "1":
            display_items()
        elif choice == "2":
            add_items()
        elif choice == "3":
            remove_items()
        elif choice == "4":
            update_items()
        elif choice == "5":
            print("Exiting Program")
            break
        else:
            print("please select valid choice!!!")