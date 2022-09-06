"""  Write a python program to sum all the numbers in a list. """

def f1(*l):
    s=0
    for i in l:
        s = s+i
    return s
List_of_sum = f1(10,20,30,40,50)
print("Sum all the numbers in a list = ",List_of_sum)
