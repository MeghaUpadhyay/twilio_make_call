import mysql.connector
from mysql.connector import Error

def storeCallerDetails(fromNo, flag):
    try:
        connection = mysql.connector.connect(host='13.91.138.194',
                                             port=3307,
                                             user='root',
                                             password='password',
                                             ssl_disabled=True)

        query = "Insert into caller_details(caller_no, flag) values(%s, %s)"

        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            #cursor.execute(query, (fromNo, flag))
            record = cursor.fetchone()
            print("You're connected to database: ", record)

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")



if __name__ == '__main__':
    storeCallerDetails("", "")