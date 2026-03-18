import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'admin1234'
)

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE crm_tutotial")

print("All Done!")