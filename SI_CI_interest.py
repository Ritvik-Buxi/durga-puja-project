prncpl_amnt = float(input("Enter your principal amount: "))
rate = float(input("Enter your rate percentage: "))
time_taken = float(input("Enter the total time taken to hold loan(in years): "))

S_I = (prncpl_amnt*rate*time_taken)/100
C_I = prncpl_amnt*(((rate+100)/100)**time_taken)

print("Your Simple interest is ",S_I,"Your Compound Interest is ",C_I-prncpl_amnt)
