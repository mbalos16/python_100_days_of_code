# Exercise27.1. Function with unlimited positional arguments

def add(*args):
    # Prints the number in position 0 of the args tuple
    print(args[0]) 
    
    sum_numbers = 0
    for n in args:
        sum_numbers += n
    return sum_numbers

print(add(1,2,3,4,5))