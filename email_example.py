import smtplib
from email.mime.text import MIMEText

def send_email(subject, message, to_email):
    """Function that sends an email to a provided email address with the given subject and message."""

    # Credentials. Change if different email is used
    #   Google app password used to avoid authentication error
    sender_email = "chavasalasb1@gmail.com"
    sender_password = "XXXX"	# Place here your app password

    # Create multipurpose internet mail extension message object
    email = MIMEText(message, "plain", "utf-8")

    # Populate standard headers for MIME message object
    email["Subject"] = subject
    email["From"] = sender_email
    email["To"] = to_email

    # Establish SMTP connection to the Gmail SMTP server
    #   "smtp.gmail.com" is the SMTP server address for Gmail
    #   465 is the port number for SSL-encrypted SMTP connection for Gmail
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        # Log into the SMTP server using the provided credentials
        server.login(sender_email, sender_password)
        # Send email
        #   as_string() method to convert the MIMEText object into a string representation with headers and settings
        server.sendmail(sender_email, to_email, email.as_string())

subject = "Test email"
message = "Hello\nThis is an automatic email test from Python!\nBR,\nSalvador"
to_email = "chavasalasb@hotmail.com"

if __name__ == '__main__':
    send_email(subject, message, to_email)
