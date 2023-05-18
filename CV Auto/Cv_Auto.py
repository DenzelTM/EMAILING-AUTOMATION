import smtplib

#configure our Email
Sender_Email = 'Youremail@gmail.com'
Sender_Password = 'YourPassword'
Recipient_Emails= ['Email1@gmail.com', 'Email2@mail.com']
Subject = 'Notification'

def send_email(recipient, message):
    msg= f"Subject: {Subject}\n\n{message}"
    #Configuration of SMTP server
    server=smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(send_email, Sender_Password)
    server.sendmail(Sender_Email, recipient, msg)
    server.quit()

if __name__ == '__main__':
    message = "The message sent when the script is run"

    for recipient in Recipient_Emails:
        send_email(recipient, message)
