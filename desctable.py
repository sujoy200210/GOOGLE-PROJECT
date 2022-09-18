def desc():
    import mysql.connector
    a=mysql.connector.connect(host="localhost",user="root",password="",database="pet_shop")
    mycursor=a.cursor()
    mycursor.execute("DESC pet")
    for x in mycursor:
        print(x)
    
