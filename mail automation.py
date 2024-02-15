import smtplib, ssl

sender_email = "blahblahblah@gmail.com"
receiver_email = "blahblahblah@gmail.com"
message = """\
from: Minje
to: Minje"""

# Send email here

port = 465  # For SSL
password = "blahblahblah"

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("blahblahblah@gmail.com", password)
    server.sendmail(sender_email, receiver_email, message)