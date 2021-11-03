import re


def registering():
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    while True:
        firstname = input("Enter your First Name: ").strip()
        if firstname.isalpha():
            lastname = input("Enter your Last Name: ")
            if lastname.isalpha():
                email = input("Enter a valid Email: ")
                if re.search(regex, email):
                    password = input("Enter your Password: ")
                    if password.isnumeric():
                        confpass = input("Confirm your Password: ")
                        if confpass.isnumeric():
                            if confpass == password:
                                phone = input("Enter a Valid phone number: ")
                                if re.search("([002])[\d]+", phone) and len(phone) == 5:
                                    try:
                                        userfile = open("users.txt", "a")
                                        newuser = ":".join([firstname, lastname, email, password, phone])
                                        userdata = newuser + '\n'
                                        userfile.write(userdata)
                                        userfile.close()
                                        # readnow= open("users.txt")
                                        # data2 = readnow.readlines()
                                        # for d in data2:
                                        #     print(d)
                                    except:
                                        print("This file is not exist")

                                    else:
                                        print("Helooooooo")

