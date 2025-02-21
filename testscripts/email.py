import imaplib
import email
#from email.header import decode_header
#import webbrowser
#import os

# establish connection with Gmail
server = "imap.gmail.com"
imap = imaplib.IMAP4_SSL(server)

# instantiate the username and the password
username = "tautomation.qa@gmail.com"
password = "ltmw btvp jkln unwo"

# login into the gmail account
imap.login(username, password)

# select the e-mails
res, messages = imap.select('"[Gmail]/All Mail"')

# calculates the total number of sent messages
messages = int(messages[0])
print(messages)

# determine the number of e-mails to be fetched
n = 1

# iterating over the e-mails
for i in range(messages, messages - n, -1):
    res, msg = imap.fetch(str(i), "(RFC822)")
    for response in msg:
        if isinstance(response, tuple):
            msg = email.message_from_bytes(response[1])

            # getting the sender's mail id
            From = msg["From"]

            # getting the subject of the sent mail
            subject = msg["Subject"]

            # printing the details
            print("From : ", From)
            print("subject : ", subject)