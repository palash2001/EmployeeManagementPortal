import sys
print("welcome to Employee system")
id = input("Please Enter Login id : ")
pwd = input("Please Enter Password:")
file = open("login.txt", "r")
a=file.readlines()
ctr = 0


def check_for_emp(b):
    pass


for i in a:
    ctr+=1
    b=i.split()
    if id == b[0] and pwd == b[1] and id == "admin":
        import admin
        break
    else:
        check_for_emp(b)
       