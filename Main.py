import mysql.connector as connector

class DBHelper:
    def __init__(self):
        self.con = connector.connect(host="localhost", port="1920", user="root", password="root", database="pyhton_project")
        query = "create table if not exists user(userId int primary key, userName varchar(255), phone varchar(255))"
        cur=self.con.cursor()
        cur.execute(query)

    def insert_user(self,user_id,user_name,user_phone):
        query = f"insert into user(userId,userName,phone) values({user_id},'{user_name}','{user_phone}')"
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()

    def fetch_all(self):
        query = "select * from user"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("User ID - ",row[0])
            print("User Name - "+row[1])
            print("User Phone - "+row[2])
            print()
            print()
    
    def delete_user(self,userID):
        query=f"delete from user where userId={userID}"
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()


helper = DBHelper()
# helper.insert_user(100,"Aakash","9958053672")
# helper.delete_user(100)
helper.fetch_all()
