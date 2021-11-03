def show():
    print("showing successfully")

    print("all projects are: ")\

    showfile = open("newprojects.txt")

    # into list
    projectinfo = showfile.readlines()

    for project in projectinfo:
        project = project.strip("\n")
        print(project)


