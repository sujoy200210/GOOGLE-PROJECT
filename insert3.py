def adddata():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="pet_shop")
    mycursor=mydb.cursor()
    r=int(input("enter the id"))
    n=input("enter name of owner")
    m=int(input("enter age"))
    g=str(input("enter type"))
    h=str(input("enter gender"))
    mycursor.execute("INSERT INTO pet (id,nameofowner,age,type,gender) VALUES(r,n,m,g,h)")
    mydb.commit()
    print(mycursor.rowcount,"RECORD INSERTED")
    a=mycursor.execute("desc pet")
