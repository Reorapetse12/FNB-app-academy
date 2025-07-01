#List p1
fruits = ["apple", "banana", "cherry"]

print(fruits[0])

fruits[1] = "blueberry"

print(fruits)

#List p2

fruits = ["apple", "banana", "cherry", "kiwi"]

fruits.append("kiwi")
print(fruits)

fruits.insert(1, "orange")
print(fruits)

fruits.remove("kiwi")
print(fruits)

fruits.sort()
print(fruits)

fruits.sort(reverse=True)
print(fruits)