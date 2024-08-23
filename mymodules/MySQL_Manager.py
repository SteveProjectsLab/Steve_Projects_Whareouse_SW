import mysql.connector
import time
import sys

class DataBase_SteveProjectWharehouse:#data base
    def __init__(self,host,username,password,database):
        self.host=host
        self.username=username
        self.password=password
        self.database=database

        try:
            self.mydb = mysql.connector.connect(
                host=self.host,
                user=self.username,
                password=self.password,
                database=self.database
                )
            print('Connected to database!')
            self.mycursor = self.mydb.cursor()
        except:
            print("failed to connect the database..\n")
            print("\nclosing the program...")
            time.sleep(3)
            sys.exit()
    def create_table(self,command):
        #exeample of command
        #mycursor.execute("CREATE TABLE items (name VARCHAR(255), quantity VARCHAR(255), unitPrice VARCHAR(255), location VARCHAR(255))")
        print('New table created!')
        self.show_tables()

    def insert_item(self,name):
        #TODO
        return
        #sql = "INSERT INTO items (name,quantity, unitPrice, location) VALUES (%s, %s, %s, %s)"
        #val = (BC327.name,BC327.quantity,BC327.unitPrice,BC327.location)
        #mycursor.execute(sql, val)

        #mydb.commit()

        #print(mycursor.rowcount, "record inserted.")
    def show_tables(self):
        self.mycursor.execute("SHOW TABLES")
        for x in self.mycursor:
            print(x) 
        return
    

    










