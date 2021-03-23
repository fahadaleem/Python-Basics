## Weight converted KG to pound and vice versa


weight = int(input("Weight: "))
unit = input("(L) lb or (K) kg: ").upper()
if unit=="L":
    converted_weight =weight / 2.20462
    print(f"You are {converted_weight} in kilogram")

elif unit=="K":
    converted_weight =weight * 2.20462
    print(f"You are {converted_weight} in Pound")
else:
    print("Invalid unit!")






