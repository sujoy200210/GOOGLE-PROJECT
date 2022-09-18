def table():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",passwd='',database="pet_shop")
    mycursor=mydb.cursor()
    mycursor.execute("create table PET(id int(3) primary key,nameofowner varchar(20),age int(2),type char(21),gender char(1))")
    print("succesfully created")



