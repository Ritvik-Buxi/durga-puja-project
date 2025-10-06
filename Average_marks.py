# The user enters his/her marks in each subject
Subjects = []
Taken_PE = bool(int(input("If you have taken Physical Education Enter 1, if not enter 0: ")))
max_marks = 0
pe_ = 0
if Taken_PE:   
    Subjects.append("PE")
    pe_ = float(input("Enter Your PE marks out of 100: "))
    max_marks += 100
else:
    pe_ = 0

Taken_Math = bool(int(input("If you have taken Math 1, if not enter 0: ")))
Math_ = 0
if Taken_Math:   
    Subjects.append("Math")
    Math_ = float(input("Enter Your Math marks out of 80: "))
    max_marks += 80
else:
    Math_ = 0

Taken_Biology = bool(int(input("If you have taken Biology 1, if not enter 0: ")))
Biology_ = 0
if Taken_Biology:   
    Subjects.append("Biology")
    Biology_ = float(input("Enter Your Biology marks out of 70: "))
    max_marks += 70
else:
    Biology_ = 0

English_ = float(input("Enter Your English marks out of 80: "))
max_marks += 80
Physics_ = float(input("Enter Your Physics marks out of 70: "))
max_marks += 70
Chemistry_ = float(input("Enter Your Chemistry marks out of 70: "))
max_marks += 70
Computer_ = float(input("Enter Your Computer marks out of 70: "))
max_marks += 70

Subjects.append("English")
Subjects.append("Physics")
Subjects.append("Chemistry")
Subjects.append("Computer")

print("Your list of subjects are: ",Subjects)
average_ = (pe_+Math_+Biology_+English_+Physics_+Chemistry_+Computer_) / len(Subjects)
percentage_ = ((pe_+Math_+Biology_+English_+Physics_+Chemistry_+Computer_) / max_marks)*100
print("You have scored and average marks of ",average_," and an average percentage of ",percentage_)
