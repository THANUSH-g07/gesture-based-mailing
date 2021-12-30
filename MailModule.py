import smtplib

fromId = "vasa20ad055@rmkcet.ac.in"
passWord = "RANdom-#1234"
toId = "harsha6286@gmail.com"


class EmailManager:
    def send_mail(self, fromAdd, toAdd, password, mailContext):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(fromAdd, password)
        server.sendmail(from_addr=fromAdd, to_addrs=toAdd, msg=mailContext)
        server.quit()


if __name__ == "__main__":
    emailManager = EmailManager()
    emailManager.send_mail(fromId, toId, passWord, "testing")
