""" Write a python program to multiply all the numbers in a list."""
def mul_list(List):
    s = 0
    for i in List:
        s = s+i
    return s
list1 =[int (e) for e in input("Enter list elements:").split(',')]
print(mul_list(list1))
