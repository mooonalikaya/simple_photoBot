import psycopg2

class DatabasePy:
    def __init__(self,pghost,pgdatabase,pguser,pgpassword,pgport):
        self.pghost = pghost
        self.pgdatabase = pgdatabase
        self.pguser = pguser
        self.pgpassword = pgpassword
        self.pgport = pgport
    
    def __PGconnections(self):
        with psycopg2.connect(
            host = self.pghost,
            database =self.pgdatabase,
            user = self.pguser,
            password = self.pgpassword,
            port = self.pgport ) as connetion:

            connetion.autocommit = True
        return connetion
        
    def _CRTtables(self,name):
        with self.__PGconnections().cursor() as cursor:
            cursor.execute(f"CREATE TABLE IF NOT EXISTS {name}(\
                id SERIAL PRIMARY KEY,\
                title VARCHAR(255) NOT NULL,\
                discription TEXT,\
                category VARCHAR(255) NOT NULL,\
                price INT NOT NULL)")           


    def InsertIntoTable(self,table,title,description,category,price):
        with self.__PGconnections().cursor() as cursor:
            cursor.execute(
                "INSERT INTO {0}(title, discription, category, price)\
                    VALUES (%s,%s,%s,%s)".format(table),
                        (title,description,category, price))
            

    def UpdateTable(self,table,column,new_value,column_where,where_value):
        with self.__PGconnections().cursor() as cursor:
            cursor.execute(f"UPDATA{table} SET {column}=\
            '{new_value}' WHERE {column_where}={where_value}")
    def _UpdateIntoTable(self,new_title,id):
        with self.__PGconnection().cursor() as cursor:
            cursor.execute(
                f"UPDATE product SET title = '{new_title}' WHERE id = {id}"
            )
    def _Altertable(self,price,new_price):
        with self.__PGconnection().cursor() as cursor:
            cursor.execute(
                f"ALTER TABLE product RENAME COLUMN {price} TO {new_price}"
            )
            
db = DatabasePy('localhost','oop_for_db','bayan','123',5432)
# db.InsertIntoTable('product','Apple','red apple','fruits',1000)
# db._CRTtables('product')
db._UpdateIntoTable('banana',1)
db._Altertable('price','new_price')
            
                    
db= DatabasePy("localhost","oop_for_db","moona","805020",5432)
db._CRTtables("product")
db.InsertIntoTable("product","apple","good apple", "fruit", 1200)

#update(1 МЕТОД)
#Add,rename,delete- ALTER TABLE (3 МЕТОДА)
#SELECT  * FROM product(несколько методов максимум и минимум)
