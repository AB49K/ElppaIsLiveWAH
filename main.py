import subprocess
from imapclient import IMAPClient
from email.mime.multipart import MIMEMultipart
from email.mime.message import MIMEMessage
from email.mime.text import MIMEText
import email
def MonitorMail(hostv,imap_user, imap_pass):
    with IMAPClient(hostv) as client:
        client.login(imap_user, imap_pass)
        client.select_folder('INBOX')
        messages=client.search(['FROM', 'no-reply@twitch.tv', "UNSEEN"])
        for uid, message_data in client.fetch(messages, 'RFC822').items():
            email_message = email.message_from_bytes(message_data[b'RFC822'])
            #Reading the email like this marks it as read. It won't re-read old emails
            if """elppa is live""" in email_message.get("Subject").lower():
               print("ElppA!")
               subprocess.run(["mpv", "elppa.mp4"])


MonitorMail("server", "username", "password")
