#enumerate() is a built-in function that lets you loop through a list (or any iterable) and 
# get both the index and the item at the same time.

fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print(i, fruits[i])


for i, fruit in enumerate(fruits):
    print(i, fruit)
