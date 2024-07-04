# Function : A set of Code that perform certain task.
# important: We need to call a func
# def function_name():
# function doce
# function
# def displayName():
#     print("My name is Gautam")
# Create a function that display your address.


# def displayAddress():
#     print("My address is Kathmandu")
# displayAddress()
# Write a programme to print even number between start and end using function.

def display_even(first, last):
    for i in range(first, last+1):
        if i % 2 == 0:
            print(i)


start = 100
end = 150
display_even(start, end)