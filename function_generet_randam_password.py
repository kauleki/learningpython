# import random
# import string
#
# def generate_password():
#     length = random.randint(8, 32)
#     characters = string.unicode_letters + string.digits + string.punctuation
#     password = ''.join(random.choice(characters) for i in range(length))
#     return password
#
# print(generate_password())
# import string
# import random
#
# # Getting password length
# length = int(input("Enter password length: "))
#
# print('''Choose character set for password from these :
# 		1. Digits
# 		2. Letters
# 		3. Special characters
# 		4. Exit''')
#
# characterList = ""
#
# # Getting character set for password
# while (True):
#     choice = int(input("Pick a number "))
#     if (choice == 1):
#
#         # Adding letters to possible characters
#         characterList += string.ascii_letters
#     elif (choice == 2):
#
#         # Adding digits to possible characters
#         characterList += string.digits
#     elif (choice == 3):
#
#         # Adding special characters to possible
#         # characters
#         characterList += string.punctuation
#     elif (choice == 4):
#         break
#     else:
#         print("Please pick a valid option!")
#
# password = []
#
# for i in range(length):
#     # Picking a random character from our
#     # character list
#     randomchar = random.choice(characterList)
#
#     # appending a random character to password
#     password.append(randomchar)
#
# # printing password as a string
# print("The random password is " + "".join(password))
import string
import random  # Import the random module

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Set the desired length for the password
password_length = 8  # Change this to your desired password length

# Generate and print a random password
generated_password = generate_password(password_length)  # Pass the integer variable, not a string
print("Your Generated Password:", generated_password)