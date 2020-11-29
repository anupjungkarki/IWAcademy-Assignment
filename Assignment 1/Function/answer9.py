# Write a Python function that takes a number as a parameter and check the number is prime or not.
def check_prime(number):
    if number == 1:
        return False
    elif number == 2:
        return True
    else:
        for i in range(2, number):
            if number % i == 0:
                return False
        return True


number = int(input("Enter the number to check prime:"))
print(check_prime(number))
