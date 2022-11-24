import smtplib

my_email = "adeyemiqudus361@gmail.com"
password = 'tbkeexyuvsbgmedm'

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs=my_email,
#                         msg='Subject: Hello\n\n This is the content of the mail'
#                         )
#
#datetime module

import datetime as dt
import random
# now = dt.datetime.now()
# print(now)

now = dt.datetime.now()
print(now.weekday())
if now.weekday() == 2:
    with open("quotes.txt") as file:
        quotes_list = file.readlines()
        quote = random.choice(quotes_list)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="adeyemiadebayo60@gmail.com",
                            msg=f"Subject: Monday Motivational quotes\n\n {quote}"
                            )
