""" Write a python program to create a function to check whether a number falls in a given range."""
def test_range(n):
    if n in range(3,9):
        print("Yes,range")
    else:
        print("The number is outside range")
test_range(5)