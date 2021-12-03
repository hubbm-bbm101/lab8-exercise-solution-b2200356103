import sys
dict = {}

with open(sys.argv[1], "r") as file:
    line = file.read().splitlines()
    for x in line:
        student, student_info = x.split(":")
        dict[student] = str(student_info)
    try:
        for student in sys.argv[2].split(","):
            print("Name: " + str(student) + "\nUniversity: {}".format(dict[student]))
    except KeyError:
        print("\nNo record of {} was found.".format(student))
