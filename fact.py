n =int (input ("Enter the number to display the factorial:     "))

def factorial(n):
    if n < 0:
        return "Invalid"
    elif n == 0:
        return 1
    else:
        fact = 1
        while n > 0:
            fact = fact * n
            n = n - 1
        print ("The factorial is: ")
        return fact

print (factorial(n))