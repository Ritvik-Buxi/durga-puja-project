# The user enters his/her marks in each subject
Subjects = []
Stream = int(input("If You have taken Science Stream enter 0, if you have taken Commerce press 1:\n"))
Taken_PE = bool(int(input("If you have taken Physical Education Enter 1, if not enter 0:\n")))
if Taken_PE:
    Subjects.append("PE")
English_Marks = input("Enter Your English marks out of 80:\n")

