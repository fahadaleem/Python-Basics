## if else in python

is_hot = False
is_cold = False

if is_hot:
    print("Its a hot day \ndrink a plenty of water!")
elif is_cold:
    print("It's a cold day \nwear warm cloths!")
else:
    print("Enjoy your day!")


## Exercise:
## Price of a house is $1M
## if the buyers has good credit
## then the price puts down to 10%
## othewrise the price put to 20%
## print the down payment

is_good_credits = True
house_price = 1000000
down_payment = 0
if is_good_credits:
    down_payment = house_price*0.10
else :
    down_payment = house_price*0.20

print(f"The down payment is: ${down_payment}")