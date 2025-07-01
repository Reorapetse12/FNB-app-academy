#Loops

fruits = ["Apple", "Banana", "Cherry"]

for fruit in fruits:
    print(fruit)
    
    
numbers = [1, 2, 3, 5, 7]
    
for number in numbers:
    print(numbers)
    print(number)
    
    
#Using a while loop to count from 1 to 5
count = 1

while count <= 5:
    print(count)
    count += 1 # Increments the count by 1
    
    
    
    
    
#Loop Control Statements

fruits = ["Apple", "Banana", "Cherry", "date"]

for fruit in fruits:
    if fruit == "Cherry":
        break # Exits the loop if cherry is found
    print(fruit)
    
print()

for fruit in fruits:
    if fruit == "Cherry":
        continue # Skips Cherry and moves to the iteration
    print(fruit)
    
print()

for fruit in fruits:
    if fruit == "Cherry":
        pass # Placeholder, no action is needed for cherry
    print(fruit)


#Loop Control Statements

count = 0

while count <5:
    print(count)
    count += 1
    if count == 3:
        break # Exits the loop when the count is reached -3