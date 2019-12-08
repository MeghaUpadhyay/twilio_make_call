import mysql
import requests
from mysql.connector import Error

def storeCallerDetails(fromNo, flag):

#     API_ENDPOINT = "https://sheetsu.com/apis/v1.0qu/207826a8646e"
#
#     data = {'caller_no': fromNo , 'flag': flag}
#
#     # sending post request and saving response as response object
#     requests.post(url=API_ENDPOINT, data=data, verify=False)
#
# if __name__ == '__main__':
#     storeCallerDetails("", "")

    try:
        connection = mysql.connector.connect(host='remotemysql.com',
                                             port=3306,
                                             user='58y5021f53',
                                             password='1sxcXeilmn',
                                             database='58y5021f53',
                                             ssl_disabled=True)

        query = "Insert into caller_details(caller_no, flag) values(%s, %s)"

        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute(query, (fromNo, flag))
            cursor.execute("commit;")
            record = cursor.fetchone()
            print("You're connected to database: ", record)

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


# if __name__ == '__main__':
#   storeCallerDetails("+917256969", 0)
