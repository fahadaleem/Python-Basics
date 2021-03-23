## Comparison Operators in pytho
## Exercise
## if temperature is greater than 20
##  print its a hot day
## if temperature is less than 10
##  print its a cold day
## otherwise
##  print it's neither hot and cold

temperature = 35

if temperature > 20:
    print("It's a hot day!")
elif temperature < 10:
    print("It's a cold day!")
else:
    print("it's neither hot or cold!")

## Exercise # 2
## if name is less than 3 characters long
##      name must be atleast 3 characters
## otherwise if it's more than 50 characters long
##      name can be maximum of 50 characters 
## otherwise 
##      name looks good!

name = "Fahad Aleem"
if len(name)<3:
    print("Name must be atleast 3 characters!")
elif len(name)>50:
    print("Name can be maximum of 50 characters!")
else:
    print("Name looks good!")