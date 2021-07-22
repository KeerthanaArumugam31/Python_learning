user={}

while True:
    ch=int(input("1.sign up 2.sign in 3.exit"))
    if ch==1:
        uname=input("Enter Username:")
        email=input("Enter your email id:")
        mobile=input("Enter your Mobile number:")
        password=input("Enter password:")
        if uname in user:
            print("This username already exist")
        else:
            user.setdefault(uname,[email,mobile,password])
            print("Account is created successfully")
    elif ch==2:
            uname=input("Enter your username or email id:")
            password=input("Enter your password:")
            print(user)
            if uname in user and password==user[uname][2]:
                
                print("login is success")
            else:
                for i in user.values():
                    if uname in i and password in i:
                        print("Login in success")
                        break
                else:
                    print("unauthorised user")
    else:
            break
