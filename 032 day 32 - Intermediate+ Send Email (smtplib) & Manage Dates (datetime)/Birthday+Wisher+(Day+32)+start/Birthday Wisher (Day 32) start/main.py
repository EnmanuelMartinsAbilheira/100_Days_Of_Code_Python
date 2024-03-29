import smtplib
import datetime as dt
import random

MY_EMAIL = ""
MY_PASSWORD = ""

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readline()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f"Subject:Monday motivation\n\n{quote}"
                            )



"""
A Note About the Next Lesson: Google SMTP Port
In the next lesson, I'll show you how to send email using the smtplib module and Python. If you are getting the error Connection unexpectedly closed, it might be due to a number of things. You can come back to this lesson to debug.

1. Make sure you've got the correct smtp address for your email provider:
Gmail: smtp.gmail.com
Hotmail: smtp.live.com
Outlook: outlook.office365.com
Yahoo: smtp.mail.yahoo.com
If you use another email provider, just Google for your email provider e.g. "Gmail SMTP address"
Below are steps specific to users sending email from Gmail addresses.

2. Go to https://myaccount.google.com/
Select Security on the left and scroll down to How you sign in to Google.
Enable 2-Step Verification

3. Click on 2-Step Verification again, and scroll to the bottom.
There you can add an App password.
Select Other from the dropdown list and enter an app name, e.g. Python Mail, then click Generate.
COPY THE PASSWORD - This is the only time you will ever see the password. It is 16 characters with no spaces.
Use this App password in your Python code instead of your normal password.

4. Add a port number by changing your code to this:
smtplib.SMTP("smtp.gmail.com", port=587)
"""


#my_email = "example@gmail.com"
#password = "1234AbCd"

#with smtplib.SMTP("smtp.gmail.com") as connection:
#    connection.starttls()
#    connection.login(user=my_email, password=password)
#    connection.sendmail(
#        from_addr=my_email,
#        to_addrs="addrees@gmail.com",
#        msg="Subject:Hello\n\nThis is the body of my email."
#    )

#connection.close()




#import datetime as dt

#now = dt.datetime.now()
#year = now.year
#month = now.month
#day_of_week = now.weekday()

#date_of_birth = dt.datetime(year=1995, month=12, day=15)
