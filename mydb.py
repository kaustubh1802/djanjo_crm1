import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
)

#perpare a cursor object
cursorObject = dataBase.cursor()

#Create a database
cursorObject.execute("CREATE DATABASE dcrm")

print("All Done!")