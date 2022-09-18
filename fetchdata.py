def fetch():
    import mysql.connector
    a=mysql.connector.connect(host="localhost",user="root",passwd="",database="pet_shop")
    mycursor=a.cursor()
    mycursor.execute("select*from pet")
    r=mycursor.fetchall()
    for x in r:
        print(x[0],x[1],x[2])
