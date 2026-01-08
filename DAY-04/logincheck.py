
#! WAP to check login of Instagram if username and password is correct

print("For Sign Up please fill out below field...")
user = input("Create Username: ")
passw = input("Create Password: ")

print("--------------------------------------------")

print("For Log In please fill out below field...")
username = input("Enter Username: ")

if username == user:
    password = input("Enter Password: ")
    if password == passw:
        print('Log In Successfull')
    else:
        print('Wrong Password!')

else:
    print('Incorrect Username')
