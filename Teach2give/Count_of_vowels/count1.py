animal = input ("Enter animal: ")
string = animal.lower()
print(string)
count = 0
list1 = ["a" , "e" , "i" , "o" , "u"]
for char in string:
    if char in list1:
        count = count+1
print("number vowels in given sentence is:",count)

