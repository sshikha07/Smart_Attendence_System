import yagmail
import os

receiver = "myemail@gmail.com"  # receiver email address
body = "Attendence File"  # email body
filename = "Attendance"

yag = yagmail.SMTP("myemail@gmail.com", "my_password")

yag.send(
    to=receiver,
    subject="Attendance Report", 
    contents=body, 
    attachments=filename, 
)

