# define adding a new item

# a list of inventory
inventory=[]

# adding a item
def add_item(name):
    quantity=int(input("what is its quantity(Kgs): "))
    price=float(input("How much does it cost per Kg: "))
    item={
        "name":name,
        "quantity":quantity,
        "price":price
    }
    inventory.append(item)
    return name


def view_item():
    item_num=1
    print("-" * 50) 
    print(f"| {'No.':<4} | {'Item Name':<20} | {'Qty(Kg)':<5} | {'Price':<8} |")
    print("-" * 50)

    if len(inventory)<1: 
        print("| No items in inventory.         |")
    else:
        for item in inventory:
            print(f"| {item_num:<4} | {item['name']:<20} | {item['quantity']:<5} | Ksh{item['price']:<7.2f} |")
            item_num+=1


def status_item():
    while True:
        try:
            item_num_str = input("Enter the number of the item to edit the item (or 'stop' to go back): ")
            if item_num_str.lower() == 'stop':
                break 

            item_num = int(item_num_str)
            

            
            if 1 <= item_num <= len(inventory):
                
                inventory[item_num - 1]['quantity'] = input("what is the new quantity: ")
                print(f"item '{inventory[item_num - 1]['name']}' quantity was edited to {inventory[item_num - 1]['quantity']}!")
                break

            else:
                print("Invalid item number. Please enter a number from the list.")

        except ValueError:
            print("Invalid input. Please enter a number or 'stop'.")

        

def deleting_item():
    while True:
        try:
            item_num_str = input("Enter the number of the item you want to delete (or 'stop' to go back): ")
            if item_num_str.lower() == 'stop':
                break 

            item_num = int(item_num_str)
            

            
            if 1 <= item_num <= len(inventory):
                
                del  inventory[item_num - 1]
                print(f"item deleted!")
                break

            else:
                print("Invalid item number. Please enter a number from the list.")

        except ValueError:
            print("Invalid input. Please enter a number or 'stop'.")


def search_item():
    
    while True:
        try:
            item_name = input("Enter the name of the item you want to search (or 'stop' to go back): ")
            if item_name.lower() == 'stop':
                break 

            found_items = []
            for item in inventory:
                if item_name.lower() in item['name'].lower():
                    found_items.append(item)

            if len(found_items)>=1:
            # Display found items in a table format, similar to view_item
                print("-" * 50)
                print(f"| {'No.':<4} | {'Item Name':<20} | {'Qty(Kg)':<5} | {'Price':<8} |")
                print("-" * 50)
            
                item_num = 1
                for item in found_items:
                    print(f"| {item_num:<4} | {item['name']:<20} | {item['quantity']:<5} | Ksh{item['price']:<7.2f} |")
                    item_num += 1
                print("-" * 50)
            
            else:
                print("| No items in inventory.         |")
            

            
        except ValueError:
            print("Invalid input. Please enter a number or 'stop'.")




def main():
    print("\n menu")
    print()
    print("Type 1 to add a item")
    print("Type 2 to view inventory")
    print("Type 3 to update the stock level of the item")
    print("Type 4 to delete an item")
    print("Type 5 to search for an item")
    print("Type 6 to exit")
    
    while True:
        menu=input("> ")
        if menu not in ["1", "2", "3", "4", "5","6"]: 
            print("Kindly enter a valid input")

        if menu =="6":
            print("see you another day")
            break
        
        elif menu == "1":
            while True:
                user_input=input("input the name of the item (or stop to finish): ")
                

                if user_input=="stop":
                    break
                else:
                    add_item(user_input)

        elif menu=="2":
            view_item()

        elif menu=="3":
            status_item()

        elif menu=="4":
            deleting_item()

        elif menu =="5":
            search_item()

    
        
main()
    


