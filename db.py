import mysql.connector
from mysql.connector import Error

from config import host, user, password, db_name
class manage_db():
    col_names = []

    def create_connection(self, host_name, user_name, user_password, db_name):
        connection = None
        try:
            connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
            )
            print("Connection to MySQL DB successful")
        except Error as e:
            print(f"The error '{e}' occurred")

        return connection

    def get_table_columns(self, connection, table_name):
        query = f"SHOW COLUMNS FROM {table_name}"
        cursor = connection.cursor()
        cursor.execute(query)
        columns = [column[0] for column in cursor.fetchall()]
        return columns

    def execute_read_query(self, connection, query):
        cursor = connection.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"The error '{e}' occurred")



#SHOW columns FROM `staff_data`;

# manager = manage_db()
# connect = manager.create_connection(host, user, password, db_name[1])
# query = "select * from actor"#str(input('query:'))
# table_name = query.split()
# columns = manager.get_table_columns(connect, table_name[-1])
# print(columns)
# result = manager.execute_read_query(connect, query)
# for row in result:
#     print(row)
