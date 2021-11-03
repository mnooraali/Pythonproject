import datetime


def edit(usremail):
    print("editing successfully")

    editproject = input("enter project name you want to Edit: ")

    editfile = open("newprojects.txt", "r")

    # into list
    projectdata = editfile.readlines()

    for project in projectdata:
        newproject = project.strip("\n")
        userinfo = newproject.split(":")
        # print(userinfo)
        if userinfo[0] == usremail and userinfo[1] == editproject:

            position = projectdata.index(project)
            # print(position)

            while True:
                userinfo[1] = input("Enter the new project name for update: ").strip()
                if userinfo[1].isalpha():
                    userinfo[2] = input("Enter the new project Details for update: ").strip()
                    if len(userinfo[2]) < 5:
                        print("Your description is short !! ")
                    else:
                        userinfo[3] = input("Enter the new project target for update: ")
                        if userinfo[3].isnumeric():
                            if userinfo[3] == 0:
                                print("Invalid total target")
                            else:
                                userinfo[4] = input("Enter the new project start date for update: ")
                                if datetime.datetime.strptime(userinfo[4], '%Y-%m-%d'):
                                    userinfo[5] = input("Enter the new project end date for update: ")
                                    if datetime.datetime.strptime(userinfo[5], '%Y-%m-%d'):
                                        if userinfo[4] > userinfo[5]:
                                            print("your start date is newer than your end date..  check this again !!")
                                        else:
                                            userinfo = ":".join(userinfo)
                                            print(userinfo)

                                            projectdata[position] = userinfo
                                            print(projectdata)

                                            addnew = open("newprojects.txt", "w")

                                            for i in projectdata:
                                                addnew.write(i + "\n")
                                            addnew.close()

                                            # print(userinfo)
                                            #
                                            # print("old one" , project)
                                            #
                                            # print("after update: ", userinfo)

                else:
                    print("Wrong project name")

    # else:
    #     print(" not found")



