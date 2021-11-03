def delete(usremail):
    print("Deleting successfully")
    deleterecord = input("Enter the project name you want to delete: ")

    deletefile = open("newprojects.txt")

    # into list
    projectdata = deletefile.readlines()

    for project in projectdata:
        newproject = project.strip("\n")
        userinfo = newproject.split(":")
        # print(userinfo)
        if userinfo[0] == usremail and userinfo[1] == deleterecord:
            projectdata.remove(project)
            new = " ".join(projectdata)
            afterdeletefile = open("newprojects.txt", "w")
            afterdeletefile.write(f"{new}")
            afterdeletefile.close()
            print(projectdata.stripe("\n"))
            break

        # else:
        #     print("Not Found")


    #         # userinfo.pop()
    #         # userinfo.pop()
    #         # userinfo.pop()
    #         # deletefile.close()
    #         print(project)
    #         for i in userinfo:
    #             print (i)
    #             del i
    #             print("DONE")
    # print(project)


        # else:
        #     print("hello", project)
        # deletefile.close()
        # deletefile = open("projects.txt", "a")
        #
        # # deletefile.write(userinfo)
        # # projectdata = deletefile.readlines()
        # for xx in projectdata:
        #     # print("file after delete is ")
        #     # print(xx)
        #     deletefile.writelines(xx)
        #
        # deletefile.close()
        #
        # deletefile = open("projects.txt")
        # projectdata = deletefile.readlines()
        # # userinfo = project.split(":")
        # for yy in projectdata:
        #     print(yy)