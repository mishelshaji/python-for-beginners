# TO TEST ON LOCAL SERVER
# RUN python -m smtpd -c DebuggingServer -n localhost:1025
import smtplib, ssl

port = 465  # For SSL
password = input("Type your password and press enter: ")

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("my@gmail.com", password)
    # TODO: Send email here

    sender_email = "my@gmail.com"
    receiver_email = "your@gmail.com"
    message = """\
    Subject: Hi there

    This message is sent from Python."""
    server.sendmail(sender_email, receiver_email, message)