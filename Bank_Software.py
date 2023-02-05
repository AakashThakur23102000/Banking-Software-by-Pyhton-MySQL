##This is BANK and ATM application software which stores all data of user in MYSQL server..

##we got some pre buid passwords and data in the database
#---->(names, account_numbers, pins, passwords, balance) values ("Admin",15151515,7777,"Admin",99999999999  )

#importing pthon sql connector
import mysql.connector as connector
#database class
class DBHelper:
    def __init__(self):
        self.con = self.con = connector.connect(host="localhost", port="1920", user="root", password="root", database="bank_software")
        
    def account_create(self,user_name,user_pins,user_passwords):
        query = f"insert into users(names,passwords,pins) values('{user_name}','{user_passwords}',{user_pins})"
        cur = self.con.cursor()
        try:
            cur.execute(query)
        except:
            print("\tPassword you are using is not avialable try using diffrent next time")
        else:
            print("\n\tYour account generated Successfully")    
        self.con.commit()

    def account_login(self,user_name,user_passwords):
        query=f"select * from users where names='{user_name}' and passwords='{user_passwords}'"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print(f"\n\tName of user is {row[0]}.")
            print(f"\tPassword of user is {row[2]}.")
            print(f"\tAccount number of user is {row[1]}.")
            print(f"\tAccount pin of user is {row[4]}.")
            print(f"\tAccount Balance of user is {row[3]}.")
        if not cur.rowcount:
            print ("\n\tEntered Account Name or Password is incorrect...")
           
    def account_deletion(self,user_name,user_pins,user_passwords):
        query=f"delete from users where names='{user_name}' and passwords='{user_passwords}' and pins = {user_pins}"
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        if not cur.rowcount:
            print ("\n\tEntered Account Name or Password or PIN is incorrect...")
        else:
            print("\n\tDeleted Sucessfully")

    def pin_reset(self,user_name,user_passwords,user_pins):
        query=f"update users set pins = {user_pins} where names ='{user_name}' and passwords ='{user_passwords}'"
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        if not cur.rowcount:
            print ("\n\tEntered Account Name or Password is incorrect...")
        else:
            print("\n\tNew PIN generated Sucessfully")

    def udate_balance(self,user_name,user_passwords):
        query=f"select * from users where names='{user_name}' and passwords='{user_passwords}'"
        cur = self.con.cursor()
        cur.execute(query)
        
        for row in cur:
            print(f"{user_name} your current balance is {row[3]}")
            try:                    
                command5=int(input("Press 1 to add money, Press 2 to Debit money, Press 3 to exit - "))
            except ValueError:
                print("\n\tEnter a numerical input.\n\n")
            else:
                if command5==1:
                    try:
                        user_pins=int(input("Enter you Account PIN first - "))
                        amount=int(input("Enter amount you want to Add - "))
                    except ValueError:
                        print("\n\tEnter a numerical input..\n\n")
                    else:
                        total = amount + row[3]
                        query2 = f"update users set balance = {total} where names ='{user_name}' and passwords ='{user_passwords}' and pins = {user_pins}"
                        cur2 = self.con.cursor()
                        cur2.execute(query2)
                        self.con.commit()
                        if not cur2.rowcount:
                            print ("\n\tEntered Account PIN is incorrect...")
                        else:
                            print("\n\tBalance Added Sucessfully")
                elif command5==2:
                    try:
                        user_pins=int(input("Enter you Account PIN first - "))
                        amount=int(input("Enter amount you want to Withdraw - "))
                    except ValueError:
                        print("\n\tEnter a numerical input..\n\n")
                    else:
                        if(amount>row[3]):
                            print("\n\tEntered amount is more than your Balance.")
                        else:
                            total = row[3] - amount
                            query2 = f"update users set balance = {total} where names ='{user_name}' and passwords ='{user_passwords}' and pins = {user_pins}"
                            cur2 = self.con.cursor()
                            cur2.execute(query2)
                            self.con.commit()
                            if not cur2.rowcount:
                                print ("\n\tEntered Account PIN is incorrect...")
                            else:
                                print("\n\tAmount Withdrawn Sucessfully")
        if not cur.rowcount:
            print ("\n\tEntered Account Name or Password is incorrect...")

    def admin_login(self,user_name,user_passwords,user_pins):
        query = f"select * from users where names='{user_name}' and passwords='{user_passwords}' and pins = {user_pins} and account_numbers = 15151515"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print(f"\n\tWelcome back {row[0]}..")
            while(True):
                print("Press 1 to show all accounts details")
                print("Press 2 to delete any user")
                print("Press 3 to exit")
                try:                    
                    command5=int(input("Enter your Command Admin - "))
                except ValueError:
                    print("\n\tEnter a numerical input.\n\n")
                else: 
                    if command5 == 1:
                        query = "select * from users"
                        cur = self.con.cursor()
                        cur.execute(query)
                        for rows in cur:
                            print(f"\n\tName of user is {rows[0]}.")
                            print(f"\tPassword of user is {rows[2]}.")
                            print(f"\tAccount number of user is {rows[1]}.")
                            print(f"\tAccount pin of user is {rows[4]}.")
                            print(f"\tAccount Balance of user is {rows[3]}.")
                    
                    elif command5 == 2:
                        print("Enter 1 to delete user by user name")
                        print("Enter 2 to delete use by user account number")
                        command5_1=input("Enter your command Admin - ")
                        if command5_1 == "1":
                            data = input("Enter user's name to delete - ")
                            query2 = f"delete from users where names='{data}'"
                            cur = self.con.cursor()
                            cur.execute(query2)
                            self.con.commit()
                            if not cur.rowcount:
                                print ("\n\tEntered Account Name not present...")
                            else:
                                print("\n\tDeleted Sucessfully")
                            
                        elif command5_1 == "2":
                            data = int(input("Enter user's account number to delete - "))
                            query2 = f"delete from users where account_numbers={data}"
                            cur = self.con.cursor()
                            cur.execute(query2)
                            self.con.commit()
                            if not cur.rowcount:
                                print ("\n\tEntered Account Number not present...")
                            else:
                                print("\n\tDeleted Sucessfully")
                        else:
                            print("\n\tEnter a valid input")
                    
                    elif command5 == 3:
                        break

        if not cur.rowcount:
            print ("\n\tAdmin access denied..")
        
            
#main code

flag_value=0
while(flag_value==0):
    print("\nPress 1 for Account Creation")
    print("Press 2 for Account Login and Fetch Details")
    print("Press 3 for Account Deletion")
    print("Press 4 for Forget PIN reset")
    print("Press 5 for Check Balance or Update Balance")
    print("Press 6 for Admin Login")
    print("Press 7 for Exiting Software")
    try:
        command = int(input("Enter your command - "))
    except ValueError:
        print("\n\tEnter a numerical input.\n\n")
        
    else:
        if command == 1:
            name1 = input("Enter your Account Name - ")
            pass1 = input("Enter your Account Password - ")
            try:
                pin1 = int(input("Enter your Account PIN in numerics - "))
            
            except ValueError:
                print("\n\tEnter a numerical PIN next time.\n\n")
                continue
            
            #if above data is in correct order 
            helper = DBHelper()
            helper.account_create(name1,pin1,pass1)
        
        elif command == 2:
            name2 = input("Enter your Name correctly - ")
            pass2 = input("Enter your password correctly - ")
            #if above data is in correct order 
            helper = DBHelper()
            helper.account_login(name2,pass2)

        elif command == 3:
            name3 = input("Enter your Name correctly - ")
            pass3 = input("Enter your password correctly - ")
            try:
                pin3 = int(input("Enter your Account PIN correctly - "))
            except ValueError:
                print("\n\tEnter a numerical PIN next time.\n\n")
                continue
            #if above data is in correct order 
            helper = DBHelper()
            helper.account_deletion(name3,pin3,pass3)

        elif command == 4:
            name4 = input("Enter your Name correctly - ")
            pass4 = input("Enter your password correctly - ")
            try:
                pin4 = int(input("Enter your new Account PIN - "))
            except ValueError:
                print("\n\tEnter a numerical PIN next time.\n\n")
                continue
            helper = DBHelper()
            helper.pin_reset(name4,pass4,pin4)

        elif command == 5:
            name5 = input("Enter your Name correctly - ")
            pass5 = input("Enter your password correctly - ")
            helper = DBHelper()
            helper.udate_balance(name5,pass5)

        
        elif command == 6:
            name6 = input("Enter your Name correctly - ")
            pass6 = input("Enter your password correctly - ")
            try:
                pin6 = int(input("Enter your Account PIN - "))
            except ValueError:
                print("\n\tEnter a numerical PIN next time.\n\n")
                continue
            helper = DBHelper()
            helper.admin_login(name6,pass6,pin6)            

        elif command == 7:
            flag_value = 1
        else:
            print("\n\tEnter a valid Input from the option\n\n")
