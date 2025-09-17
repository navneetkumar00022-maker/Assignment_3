# Calculate Factorial Using a function ==>

global n
def factorial(n):
    n = int(input("Enter a number: "))
    if n==0 or n==1:
        return print("factorial of ",n," is: 1")
    else:
        fact = 1
        for i in range(1,n+1):
            fact*=i
        return print("factorial of ",n," is: ",fact)
factorial(5)