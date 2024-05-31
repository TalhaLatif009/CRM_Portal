import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root123'
)

cursorObject = dataBase.cursor()

# Note: Hyphens are not allowed in database names, so use underscore instead.
cursorObject.execute("CREATE DATABASE crm_portal")

print("Database 'crm_portal' created successfully!")

# Close the cursor and connection
cursorObject.close()
dataBase.close()
 