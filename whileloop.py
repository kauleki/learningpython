
# atm_pin = '1456'
#
# user_pin = ''
# attempt = 0
#
# while atm_pin != user_pin:
#     if attempt>0:
#         print(f"Invalid pin code. Total Attempt  {attempt}")
#     user_pin = input("Enter ATM Pin: ")
#     attempt = attempt + 1
# print("Access Granted. How much you want to withdraw?")
#
# git config --global user.name "Gautam Mainali"
# git config --global user.email "gautamkauleki@outlook.com"

name = input("Enter Your Name : ")
index = 0
while index <= 5:
    print(name)
    index = index +1
    if index == 5:
        break

