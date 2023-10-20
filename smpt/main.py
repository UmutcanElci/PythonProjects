import smtplib

my_email = "mail"
password = "password"


connection = smtplib.SMTP("smtp.mail.mail.com")
connection.starttls() # Transport Layer Security
connection.login(user=my_email,password=password) #Mail - Password
connection.sendmail(from_addr=my_email,to_addrs="anothermail",msg="Helloo")
connection.close()

