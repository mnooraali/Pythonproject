import datetime

def specificdate():
    print("Specific...")
    specific = input("Enter the date you want to search for its project: ")
    try:
        datetime.datetime.strptime(specific, '%Y-%m-%d')
        showfile = open("newprojects.txt")
        filedata = showfile.readlines()
        for project in filedata:
            showproject = project.strip("\n")
            checkproject = showproject.split(":")
            # print(checkproject)
            # print(checkproject[4])
            if checkproject[4] == specific:
                print(f"Founded projects start within {checkproject[4]} are \n")
                print(checkproject)
    except ValueError:
        raise ValueError("Wrong date format")
