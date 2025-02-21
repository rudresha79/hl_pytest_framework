import imaplib


def te():
    imap_host = 'imap.gmail.com'
    imap_user = 'tautomation.qa@gmail.com'
    imap_pass = 'ltmw btvp jkln unwo'

    imap = imaplib.IMAP4_SSL(imap_host)
    imap.login(imap_user, imap_pass)
    imap.select('"[Gmail]/All Mail"')
    message = imap.search(None, 'Security alert', "Verify your email")
    print(message)



te()