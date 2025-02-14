import random
import string
def generatepassword(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
print("\t\t\tPASSWORD GENERATOR\t\t\t")
print("\t\t\t======== =========\t\t\t")
length = int(input("Enter the desired password length: "))
password = generatepassword(length)
print("Generated Password:",password)
