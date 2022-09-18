def showdatabases():
    import mysql.connector
    a=mysql.connector.connect(host="localhost",password='',user='root')
    mycursor=a.cursor()
    mycursor.execute("SHOW DATABASES")
    for x in mycursor:
        print(x)

def database():
    import mysql.connector
    a=mysql.connector.connect(host="localhost",user="root",password="")
    mycursor=a.cursor()
    mycursor.execute("pet_shop")
