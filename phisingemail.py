import smtplib

# Set up the email server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("yashchaturvedi851@gmail.com", "b2b2")

# Set up the email message
sender_email = "your_email_address@gmail.com"
receiver_email = "receiver_email_address@example.com"
subject = "Deactivation Request"
body = "Please deactivate my account."

message = f"Subject: {subject}\n\n{body}"

# Send the email
server.sendmail(sender_email, receiver_email, message)

# Close the email server
server.quit()