def updatedata():
    import mysql.connector
    a=mysql.connector.connect(host='localhost',user='root',password='',database='pet_shop')
    mycursor=a.cursor()
    n=int(input("enter id"))
    k=int(input("enter age"))
    sql="update pet set id =%s where age = %s"
    val=(k,n)
    mycursor.execute(sql,val)
    print(mycursor.rowcount,'record update')
    a.commit()
