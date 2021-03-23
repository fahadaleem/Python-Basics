## for loop in python

for item in "strings":
    print(item)


print("to iterate on an array items")
for item in ["Banana", "Apple", "Strawberry"]:
    print(item)    


## range function to apply limts
## 0-4
## 0, 1,2,3,4
print("for loop to limit the numbers")
for item in range(5):
    print(item)

## to set the starting number
print("for loop to set the starting number ")
for item in range(1,9):
    print(item)

## to set the step:
print("for Loop with Step in range:")
for item in range(1,10, 2):
    print(item)

## exercise:
## print the sum of [10,20,30]
print("Exercise:")
sum = 0
for i in [10,20,30]:
    sum += i
print(f"total sum is: {sum} ") 