## program to find the largest number from a list

numbers = [2,4,3,5,7,8,9,2,10,20,16,87,1]
max_num = 0
for number in numbers:
    if max_num<number:
        max_num = number

print(f"Maximum Number: {max_num}")
