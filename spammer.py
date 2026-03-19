from email.mime.text import MIMEText
import smtplib
import ssl

# -----------------------------
# -----------------------------
# -----------------------------
def send_email(email_to, subject, message):
    # 1. build gmail message
    msg = MIMEText(message)
    msg["From"] = "OWN_GMAIL_OSOITE"
    msg["To"] = email_to
    msg["Subject"] = subject

    # 2. open gmail (SSL)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:

        # 3. login to gmail (USE GMAIL APP PASSWORD)
        server.login("gmail address here", "gmail password here")

        # 4. Send message
        server.sendmail("OWN_GMAIL_OSOITE", email_to, msg.as_string())


# -----------------------------
# Main
# -----------------------------
print("EMAIL SENDER")
print("")
print("MADE BY MrLizard!")
print("1. Email sender")
print("")
print("2. Made by ")
print("")

number = int(input("Choose number: "))

if number == 1:
    print("Welcome!")
    print("")

    email_to = input("Email to: ")
    subject = input("Enter subject: ")
    message = input("Enter message: ")
    amount = int(input("Enter amount: "))

    for i in range(amount):
        send_email(email_to, subject, message)
        print("Email sent...")

if number == 2:
    print("Made by MrLizard!")
    print("Thanks for using my spammer tool!")
