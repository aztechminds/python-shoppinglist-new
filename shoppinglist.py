from Database_functions import add_item, select_items, update_item, delete_item, create_table
shoppinglist = []

def add():
     add_item("Cherry", 1, 2.50)
     return
     item = input("please enter the articel you would like to add to the list:")
     if item:
        shoppinglist.append(item)
        print(f"your item {item} has been successfull added")
     else:
        print("empty input, please enter a articel")

def show_shoppinglist():
     shoppinglist = select_items()
     if shoppinglist:
          print("your shoppinglist:")
     for item in shoppinglist:
          print(item)
     else:
          print("shoppinglist is empty")

def update():
     select = input("Please enter id")
     
     try:
          id = int(select)
          name = input("Please enter item name")
          price_input = input("please enter a price")
          price = float(price_input)
          amount_input = input("please enter an amount")
          amount = int(amount_input)

          update_item(id, name, amount, price)
     except:
          print("Please enter a number")

def delete():
     select = input("Please enter id")

     try:
          id = int(select)
          delete_item(id)
     except:
          print("Please enter a number")

def main():
     create_table()
     while True:
          print("\n --- shoppinglist ---")
          print("\n 1. add article")
          print("\n 2. show shoppinglist")
          print("\n 3. update shoppinglist")
          print("\n 4. delete an article")
          print("\n 5. stop programm")

          choice = input("please choose an option: \n")
          
          print(type(choice)) 
          
          if choice == "1":
               print("Please type the following details: ")
               name = input("name: ")
               amount = input("amount: ")
               price = input("price: ")
               add_item(name, amount, price)
                         
          elif choice == "2":
                show_shoppinglist()

          elif choice == "3":
               print("Bitte gib die aktualisierten Daten mit id ein: ")
               id = input("id: ")
               name = input("name: ")
               amount = input("amount: ")
               price = input("price: ")
               update_item(id, name, amount, price)
          
          elif choice == "4":
                print("Please insert the ID number to delete the article: ")
                id = input("id: ")
                delete_item(id)

          elif choice == "5":
               print("Good Bye!")
               break
          else:
               print("Choose an option from 1 to 5: ")

# Starte das Programm nur, wenn dieses Skript direkt ausgeführt wird
if __name__ == "__main__":
    main()

