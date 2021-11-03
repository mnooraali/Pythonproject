import datetime


def create(usremail):

    print("created successfully")
    while True:
        projectname = input("Enter your project name: ").strip()
        if projectname.isalpha():
            if len(projectname) < 4:
                print("Your project name is short !!")
            else:
                details = input("Type your project description: ").strip()
                if len(details) < 5:
                    print("Your project details is short !!")
                else:
                    target = input("Enter your project total target: ").strip()
                    if target.isnumeric():
                        if target == 0:
                            print("Invalid total target")
                        else:
                            startdate = input("Enter a valid start date as YYYY-MM-DD syntax: ")
                            if datetime.datetime.strptime(startdate, '%Y-%m-%d'):
                                enddate = input("Enter a valid end date as YYYY-MM-DD syntax: ")
                                if datetime.datetime.strptime(enddate, '%Y-%m-%d'):
                                    if startdate > enddate:
                                        print("your start date is newer than your end date..  check this again !!")
                                    else:
                                        # register the project
                                        try:
                                            projectfile = open("newprojects.txt", "a")
                                            newproject = ":".join(
                                                [usremail, projectname, details, target, startdate, enddate])
                                            projectdata = newproject + '\n'
                                            projectfile.write(projectdata)
                                            projectfile.close()
                                            readnow = open("newprojects.txt")
                                            data2 = readnow.readlines()
                                            for d in data2:
                                                print(d)
                                        except:
                                            print("This file is not exist")

                                        else:
                                            print("Helooooooo")
                                else:
                                    print("Invalid end date syntax, the syntax should be as YYYY-MM-DD ")
                            else:
                                print("Invalid start date syntax, the syntax should be as YYYY-MM-DD ")
                    else:
                        print("your total target is not a number")









