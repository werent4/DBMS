import mysql.connector
from mysql.connector import Error
import re

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


    def execute_read_query(self, connection, query):
        cursor = connection.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"The error '{e}' occurred")
###############################################################
    def get_col_names(self,connection, query):

        col_names = []

        table_name = re.findall("\w{3,};$", query)
        #query = f"SHOW columns FROM '{table_name[0]}'"
        cursor = connection.cursor()
        col = None
        try:
            cursor.execute(f"SHOW columns FROM {table_name[0]}")
            col = cursor.fetchall()
            #return col
        except Error as e:
            print(f"The error '{e}' occurred")
        for row in col:
            col_names.append(row[0])
        return col_names

###############################################################
    def output_query(self, result):
        for row in result:
            return row

#SHOW columns FROM `staff_data`;

#manager = manage_db()
#connect = manager.create_connection(host, user, password, db_name[0])
#query = str(input('query:'))
#result = manager.get_col_names(connect, query)
#col_names = []
#for row in result:#
    #col_names.append(row[0])
#print(result)
