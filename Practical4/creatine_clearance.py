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
age = 20
weight = 63
creatine = 25
#This is not my creatine concentration
#It's just in the normal scale
gender = "male"
if age >= 100:
    print("Error: age must be less than 100")
elif weight <=20 or weight >= 80:
    print("Error: weight must be between 20 and 80")
elif creatine <= 0 or creatine >= 100:
    print("Error: creatine concentration must be between 0 and 100")
elif gender != "male" and gender != "female":
    print("Error: gender must be male or female") 
else:
    CrCl = ((140 - age) * weight) / (72 * (creatine / 88.4))
    if gender == "female":
        CrCl = CrCl * 0.85
    print(f"{CrCl}")