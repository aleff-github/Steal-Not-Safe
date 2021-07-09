# Photos
import cv2
# Sleep
import time
# Email
import email, smtplib, ssl
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
# Internet
from urllib.request import urlopen

def internet_test():
    try:
        response = urlopen('https://www.google.com/', timeout=10)
    except: 
        time.sleep(10)
        internet_test()

def get_photos(photos):
    i = 0
    while i < 10:
        camera = cv2.VideoCapture(0)
        return_value, image = camera.read()
        file_name = 'safe'+str(i)+'.png'
        photos.append(file_name)
        cv2.imwrite(file_name, image)
        i += 1
        time.sleep(3)
        del(camera)

def send_email(photos):
    port = 465  # For SSL
    password = "your password here" # To be changed TODO

    sender_email = "sender@gmail.com" # To be changed TODO
    receiver_email = "receiver@gmail.com" # To be changed TODO

    message = MIMEMultipart("alternative")
    message["Subject"] = "INSERT HERE THE SUBJECT" # To be changed, if you want TODO
    message["From"] = sender_email
    message["To"] = receiver_email
    text = """\
    Email sent automatically, access from your PC has been detected!
    """ # To be changed, if you want TODO

    part1 = MIMEText(text, "plain")
    message.attach(part1)

    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password) 
        # Open PNG file in binary mode
        for photo in photos:
            with open(photo, "rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {photo}",
            )
            message.attach(part)
        
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )

def main():
    photos = []
    internet_test()
    get_photos(photos)
    send_email(photos)

main()
