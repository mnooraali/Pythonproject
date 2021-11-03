import editing
import deleting
import showing
import creating
import specificsearch
import re


def login():

    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

    usremail = input("Enter a valid Email: ").strip()
    if re.search(regex, usremail):
        usrpassword = input("Enter your password: ")
        if usrpassword.isnumeric():
            loginfile = open("users.txt")
            userdata = loginfile.readlines()
            for usr in userdata:
                usr = usr.strip("\n")
                userinfo = usr.split(":")
                if userinfo[2] == usremail and userinfo[3] == usrpassword:
                    print("Gooooood")
                    choice = \
                        input("What you want to do? 'c' for create, 's' for show all the projects, 'd' for delete, 'e' for edit, 'sr' for search..: ").strip().lower()
                    if choice == 'c':
                        creating.create(usremail)
                        break
                    elif choice == 's':
                        showing.show()
                        break
                    elif choice == 'e':
                        editing.edit(usremail)
                        break
                    elif choice == 'd':
                        deleting.delete(usremail)
                        break
                    elif choice == 'sr':
                        specificsearch.specificdate()
                        break
                    else:
                        print("Wrong choice")












                # for i in userinfo:
                #     print(type(i))
                    # print(i[3])
                    # if i[2] == usremail and i[3]== usrpassword:
                    #     print(i)
                    #     break
                # print(userinfo)
                # print(userinfo[2])
                # if userinfo[2] == usremail and userinfo[3] == usrpassword:
                #     print("Welcome back..")
                #     break
                # else:
                #     print("Error")


    #
    #
    # if usrmail == email:
    #     usrpassword =
    #         print("Welcome Back")
    # usremail = input("Enter a valid Email: ")
    #
    #     if usrpassword.isnumeric():
    #         print("Welcome Back")
    #     else:
    #         print("Wrong password")