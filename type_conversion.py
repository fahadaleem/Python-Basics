## for type conversion we have following methods
## 1- int()
## 2- bool()
## 3- float()
## 4- str()

birth_year = input("Enter Birth Year: ")
age = 2021 - int(birth_year)
print(age)


## Exercise
## Ask a user their weight(pounds), convert it into kilogram and print on the terminal

weight_in_pound = float(input("Enter your weight in pound: "))
converted_weight = weight_in_pound / 2.205
print("Your weight in KG is: ", converted_weight)

