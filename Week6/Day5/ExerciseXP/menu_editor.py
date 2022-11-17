import psycopg2

HOSTNAME =  'localhost'
USERNAME =  'postgres'
PASSWORD =  '123456789'
DATABASE =  'restaurant '

connection = psycopg2.connect(host = HOSTNAME, user = USERNAME, password = PASSWORD, dbname = DATABASE)
cursor = connection.cursor()

class MenuItem:

    def __init__(self, item, price):
        self.price = price
        self.item = item

    def add_item_to_menu(self):
        save = input("enter order with parenthesis coma and semicolon:")
        q1 = f"INSERT INTO restaurant(item, price) values {save};" 
        cursor.execute(q1) 
        connection.commit() 
        connection.close()
        print(f'{save} has been saved!')

    def remove_item_from_menu(self):
        delete = input("enter name of row you want to delete:")
        q2 = f"DELETE FROM restaurant WHERE {delete};"
        cursor.execute(q2) 
        connection.commit() 
        connection.close()
        print(f'{delete} has been deleted!')

    def show_restaurant_menu():
          q4 = "SELECT * from restaurant;" 
          cursor.execute(q4) 
          results = cursor.fetchall() 
          print(results)
          connection.close()

    def menu():
        while True: 
        
            answer = input('menu \n add item to menu enter: add\n remove item from menu enter: remove\n show restaurant menu enter: menu\n or enter exit to exit:')
        
            if answer == 'add':
                item.add_item_to_menu()
            if answer == 'remove':
                item.remove_item_from_menu()
            if answer == 'menu':
                MenuItem.show_restaurant_menu()
            if answer == 'exit':
                print('thank you see you next time!')
                return False

item = MenuItem('hamburger', 25)
MenuItem.menu()



