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

    def save(self):
        save = input("enter order with parenthesis coma and semicolon:")
        q1 = f"INSERT INTO restaurant(item, price) values {save};" 
        cursor.execute(q1) 
        connection.commit() 
        connection.close()
        print(f'{save} has been saved!')

    def delete(self):
        delete = input("enter name of row you want to delete:")
        q2 = f"DELETE FROM restaurant WHERE {delete};"
        cursor.execute(q2) 
        connection.commit() 
        connection.close()
        print(f'{delete} has been deleted!')

    def update(self):
        update = input("enter your update:")
        update2 = input("enter what you want to update:")
        q3 = f"UPDATE restaurant SET {update} WHERE {update2};"
        cursor.execute(q3) 
        connection.commit() 
        connection.close()
        print(f'{update} has been updated!')

    def all():
          q4 = "SELECT * from restaurant;" 
          cursor.execute(q4) 
          results = cursor.fetchall() 
          print(results)
          connection.close()

item = MenuItem('Burger', 35)
# item.save()
# item.delete()
# item.update()
items = MenuItem.all()

