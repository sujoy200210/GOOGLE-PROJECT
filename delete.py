def deletedata():
    import mysql.connector
    a=mysql.connector.connect(host='localhost',user='root',passwd='',database='pet_shop')
    mycursor=a.cursor()
    r=int(input("enter id"))
    sql="delete from pet where id = %s"
    mycursor.execute(sql,(r,))
    print(mycursor.rowcount,'record deleted')
    a.commit()
    

