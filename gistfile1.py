print ("This program calculates eGFR using the MDRD formula")

#Obtain creatinie
creatinine = input("Enter creatinine concentration (micromol/l) ")
creatinine = float(creatinine)
gfr = (creatinine ** -1.154) * 32788

#work out age
age = input("Enter age ")
age = int(age)
gfr = (age ** -0.203) * gfr

#Work out Gender
gender = raw_input("Gender? (Enter m/f) ")
if gender == "f":
     gfr = gfr * 0.742
     
#Work out if patient is Black
black = raw_input("Is patient Black? (Enter y/n) ")
if black == "y":
    gfr = gfr * 1.21
print "Patient gfr is (ml/min/1.732m^2)"
print (gfr)

#Determine range
if gfr >= 90:
    print ("CDK Stage 1 - Normal renal function")
if gfr <= 89 and gfr >= 60:
    print ("CDK Stage 2 - Midly reduced renal function")
if gfr <= 59 and gfr >= 45:
    print ("CDK Stage 3a - Morderate decrease in renal function")
if gfr <=44 and gfr >= 30:
    print ("CDK Stage 3b - Morderate decrease in renal function")
if gfr <= 29 and gfr >= 15:
    print ("CDK Stage 4 - Severely reduced renal function")
if gfr <15:
    print ("CDK Stage 5 - End stage renal failure")


