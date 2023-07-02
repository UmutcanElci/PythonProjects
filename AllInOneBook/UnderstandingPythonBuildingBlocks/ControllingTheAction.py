# if else

total = 100 
sales_tax = 0.065
taxable = True

if taxable : 
    print(f"Subtotal : ${total:.2f}")
    sales_tax = total * sales_tax_rate
    print(f"Sales Tax: ${sales_tax:.2f}")
    total = total + sales_tax

print(f"Total : ${total:.2f}")

age = 31 
if age < 21:
    beverage = "milk"
elif age >= 21 and age <80:
    beverage = "beer"
else:
    beverage = "prune juice"

print("Have a " + beverage)

#Looping through String

for x in "snorkel":
    print(x)
print("Done")

for x in ["The","rain","in","Spain"]:
    print(x)
print("Done")

