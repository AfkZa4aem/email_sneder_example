import datetime as dt
import smtplib
import random
import pandas
import os

PLACEHOLDER = "[NAME]"
MY_EMAIL = "my_email@gmail.com"
MY_PASSWORD = "my_password"
LETTER_TO_SEND = ""

now = dt.datetime.now()
is_day = now.day
is_month = now.month
data = pandas.read_csv("./birthdays.csv")
birthdays = data.to_dict(orient="records")
is_birthday = [person for person in birthdays if person['month'] == is_month and person['day'] == is_day]
name = is_birthday[0]["name"]
email = is_birthday[0]["email"]
if is_birthday:
    file = random.choice(os.listdir("./letter_templates/"))
    with open(f"./letter_templates/{file}") as letter:
        new_letter = letter.read()
        LETTER_TO_SEND = new_letter.replace(PLACEHOLDER, name)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=email,
            msg=f"Subject:Happy Birthday {name}\n\n{LETTER_TO_SEND}"
        )


