from email.mime.text import MIMEText
import smtplib
import ssl

# -----------------------------
# SÄHKÖPOSTIN LÄHETYSFUNKTIO
# -----------------------------
def send_email(email_to, subject, message):
    # 1. Rakenna sähköpostiviesti
    msg = MIMEText(message)
    msg["From"] = "OWN_GMAIL_OSOITE"
    msg["To"] = email_to
    msg["Subject"] = subject

    # 2. Avaa Gmail-yhteys (SSL)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:

        # 3. Kirjaudu sisään Gmailiin (käytä SOVELLUSSALASANAA)
        server.login("gmail address here", "gmail password here")

        # 4. Lähetä viesti
        server.sendmail("OWN_GMAIL_OSOITE", email_to, msg.as_string())


# -----------------------------
# PÄÄOHJELMA
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
