import random
import string

def generatestrogpassword(password_length):
    if password_length < 8:
        print("Password should contain  8 characters.")
        password_length = 8
    letters = string.ascii_letters  
    digits = string.digits
    specialchars = string.punctuation  

    while True:
        password = ''
        count = 0
        
        for i in range(password_length):
            password += random.choice(letters + digits + specialchars)

        has_special_char = False
        for char in password:
            if char in specialchars:
                has_special_char = True
                break

        for char in password:
            if char in digits:
                count += 1

        if has_special_char and count >= 2:
            return password
        
password_length = int(input("Enter the password length: "))
password = generatestrogpassword(password_length)
print(" your Password is:", password)
