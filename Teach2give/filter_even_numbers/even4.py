def even(b):
    if b % 2 == 0:
        return True
    return False
list = [0,-2,-4]

output = filter(even,list)
print("Even numbers are :",list)