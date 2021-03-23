## print F shape on terminal
numbers = [5,2,5,2,2]

for x in numbers:
    line = ""
    for y in range(x):
        line+="x"
    print(line)