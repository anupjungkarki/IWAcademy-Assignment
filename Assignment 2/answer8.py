# Write a function, is_prime, that takes an integer and returns True if the number is prime and False if the number is not
# prime
def is_prime(num):
    if not num % 2 == 0:
        return True
    else:
        return False


num = int(input("Enter the number to check Prime:"))
print(is_prime(num))
