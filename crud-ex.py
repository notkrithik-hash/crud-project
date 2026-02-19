from pymysql import *

def adduser():
    try:
        sno = int(input("Enter the sno :"))
        name = input("Enter the user name :")
        age = int(input("Enter the user age :"))
        phno =int(input("Enter the phone no:"))
       
        con = connect(host="localhost",user="root",password="accord",database="userdb430")
        q=f"insert into userinfo values({sno},'{name}',{age},{phno})"
        cur = con.cursor()
        res=cur.execute(q) #store the no of records executed
        con.commit() #used to save the changes in the db
        print("Data Saved" if(res!=0) else "Data Not Saved...")
        con.close()
    except Exception as e:
        print(e)
def updateuser():
    try:
        sno = int(input("Enter the sno :"))
        phno =int(input("Enter the phone no:"))
       
        con = connect(host="localhost",user="root",password="accord",database="userdb430")
        q=f"update userinfo set phno = {phno} where sno ={sno}"
        cur = con.cursor()
        res=cur.execute(q) #store the no of records executed
        con.commit() #used to save the changes in the db
        print("Data updated" if(res!=0) else "Incorrect sno")
        con.close()
    except Exception as e:
        print(e)

def deleteuser():
    try:
        sno = int(input("Enter the sno :"))
       
        con = connect(host="localhost",user="root",password="accord",database="userdb430")
        q=f"delete from userinfo where sno ={sno}"
        cur = con.cursor()
        res=cur.execute(q) #store the no of records executed
        con.commit() #used to save the changes in the db
        print("Data deleted" if(res!=0) else "Incorrect sno")
        con.close()
    except Exception as e:
        print(e)
def finduser():
    try:
        sno = int(input("Enter the sno :"))
        con = connect(host="localhost",user="root",password="accord",database="userdb430")
        q=f"select * from userinfo where sno ={sno}"
        cur = con.cursor()
        cur.execute(q)
        data = cur.fetchall()
        c=0
        print("sno\tname\tage\tphno")
        for i in data:
            for j in i:
                print(j,end="\t")
                c=1
            print()
        if(c==0):
            print("Incorrect sno")
        con.close()
    except Exception as e:
        print(e)
def printuser():
    try:
        con = connect(host="localhost",user="root",password="accord",database="userdb430")
        q=f"select * from userinfo"
        cur = con.cursor()
        cur.execute(q)
        data = cur.fetchall()
        c=0
        print("sno\tname\tage\tphno")
        for i in data:
            for j in i:
                print(j,end="\t")
                c=1
            print()
        if(c==0):
            print("No Data Found")
        con.close()
    except Exception as e:
        print(e)

while(True):
    ch=int(input("1.insert\n2.update\n3.delete\n4.find\n5.print\n6.exit\nselect any 1:"))
    if(ch==1):
        adduser()
    elif(ch==2):
        updateuser()
    elif(ch==3):
        deleteuser()
    elif(ch==4):
        finduser()
    elif(ch==5):
        printuser()
    elif(ch==6):
        print("Thank you...")
        break
    else:
        print("Invalid choice...")

