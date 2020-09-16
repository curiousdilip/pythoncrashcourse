gpa = float(input("Enter you GPA: "))

if gpa >= 5:
    print("You are Eligible")
elif gpa < 5 and gpa >= 4:
    if gpa >= 4.5:
        print("You have higher chances of getting selected")
    else:
        print("You have been put in the waiting list and have lower chances of getting selected")
else:
    print("You are not eligible")
