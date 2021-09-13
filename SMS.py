import smtplib

carriers = {'verizon': "@vtext.com"}


def send_num(msg):
	// Enter your number below in the text:
    to_num = f"Put_Your_Number_Here(like xxx-xxx-xxxx){carriers['verizon']}"
    auth = ("aryannamavar@gmail.com", "Here_Copy_Your_Pass")

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(auth[0], auth[1])

    server.sendmail(auth[0], to_num,msg)

def send_email(msg):
    to_email = "aryannamavar@hotmail.com"
    to_pass = input("Enter authentication pass:")
    auth = ("aryannamavar@gmail.com", "Here_Copy_Your_Pass")
    print('sending an email')
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(auth[0], auth[1])

    server.sendmail(auth[0], to_email, msg)
    print("Email sent")