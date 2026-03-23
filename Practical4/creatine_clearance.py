# 1.Define variables
# 2.Check the standard:
#    Age < 100
#    20 < Weight < 80
#    0 < Creatine < 100
#    Gender is "male" or "female"
# 3.If any input is invalid, print a specific error message
# 4.Calculate the CrCl
#   Formula: CrCl = ((140 - age) * weight) / (72 * (creatine / 88.4))
#   If the patient is female, multiply the result by 0.85
#   Print the final calculated CrCl value
import sys
age = float(input("Enter age (years):"))
if age >= 100:
    print("Error: age must be less than 100")
    sys.exit()
weight = float(input("Enter weight (kg):"))
if weight <=20 or weight >= 80:
    print("Error: weight must be between 20 and 80")
    sys.exit()
creatine = float(input("Enter creatinine concentration (umol/L):"))
if creatine <= 0 or creatine >= 100:
    print("Error: creatine concentration must be between 0 and 100")
    sys.exit()
gender = input("Enter gender (male/female):").lower()
if gender != "male" and gender != "female":
    print("Error: gender must be male or female")
    sys.exit() 
else:
    CrCl = ((140 - age) * weight) / (72 * (creatine / 88.4))
    if gender == "female":
        CrCl = CrCl * 0.85
    print(f"{CrCl}")