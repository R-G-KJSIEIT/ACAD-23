def leap(lp):
    if lp%4 == 0:
        print("It is a leap year")
    elif lp%4 != 0:
        print("It ain't a leap year")

# Adding a comment to get rid of a warning
lp = int (input("Enter the year to check if it's a leap year: "))
leap(lp)