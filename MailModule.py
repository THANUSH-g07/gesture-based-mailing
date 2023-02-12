import smtplib
import os
import email
import imaplib
from AudioModule import ThunderAssistant as ta

hostEmailId = "harsha6286@gmail.com"
hostPassword = "nezohxjckmydnlyx"
toId = os.environ.get('tomail')


class ThunderMail:
    @staticmethod
    def send_mail(fromAdd, toAdd, password, mailContext):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(fromAdd, password)
        server.sendmail(from_addr=fromAdd, to_addrs=toAdd, msg=mailContext)
        server.quit()

    @staticmethod
    def read_mail(emailId, password, count = 1):
        imap = imaplib.IMAP4_SSL("imap.gmail.com")
        result = imap.login(emailId, password)
        imap.select('"[Gmail]/All Mail"', readonly=True)
        response, messages = imap.search(None, 'Unseen')
        messages = messages[0].split()
        latest = int(messages[-1])
        oldest = int(messages[0])
        for i in range(latest, latest - count, -1):
            res, msg = imap.fetch(str(i), "(RFC822)")
            for response in msg:
                if isinstance(response, tuple):
                    try:
                        msg = email.message_from_bytes(response[1])
                        Date = str(msg["Date"])
                        From = msg["From"]
                        From = str(From)[:From.index("<")]
                        Subject = str(msg["Subject"])
                        print(f'Subject is :{Subject}')
                        ta.speak("Subject is: ")
                        ta.speak(Subject)
                        print(f'mail from {From}')
                        ta.speak("Mail from")
                        ta.speak(From)
                        # print(msg["Date"])
                        # print(msg["From"])
                        # print(msg["Subject"])
                        print(f'mail on {Date}')
                        print(f'mail from {From}')
                    except:
                        print("missing data in mail")

                    # mail_from = str(msg["From"])
                    # mail_from = mail_from[:mail_from.index("<")]
                    # speak(f'mail from. {mail_from}')
                    # print(f'Subject is. {str(msg["Subject"])}')
                    # speak(f'Subject is. {str(msg["Subject"])}')

            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    body = part.get_payload(decode=True)
                    # print(body.decode("UTF-8"))
                    Body = body.decode('utf-8')
                    print(f'Body: \n{Body}')
                    ta.speak("Body is :")
                    ta.speak(Body)


if __name__ == "__main__":
    emailManager = ThunderMail()
    emailManager.send_mail("")
    emailManager.read_mail(hostEmailId, password=hostPassword)
