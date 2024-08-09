
list = [10,15,20,25]

result = filter(lambda i : i % 2 == 0, list)

for i in result:
    print("even numbers are :",i)


