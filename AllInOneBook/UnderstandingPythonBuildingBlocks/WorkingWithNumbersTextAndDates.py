import datetime as date
#Formatting
username = "Alan"
print(f"Hello {username}")

#Formatting percent numbers
sales_tax_rate = 0.065

print(f"Sales tax rate {sales_tax_rate:.2%}")

#Strings 

#Getting length of a string

s1 = "A B C"

print(len(s1))

username.capitalize() #Returns the first letter capitalized and the rest lowercase

username.count("a",[0,1])#Finding the given string between

username.lstrip()#Removed and leading spaces

#Date and time

todays_date = f"{today:%m/%d/%Y}"

#Or use datetime

now = date.datetime.now()

birthdate = dt.datetime(2000,12,3)

#Formatting at dates and times ex: weekday %a = Sun or %A = Sunday only difference is the one is abbreviated other is full
