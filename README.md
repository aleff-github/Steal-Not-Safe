# Steal-Not-Safe
Stealing a computer won't be as easy as it used to be, as long as you have Python and an internet connection.
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FNoNameoN-A%2FSteal-Not-Safe&count_bg=%231C1C1C&title_bg=%231C1C1C&icon=protonmail.svg&icon_color=%23E7E7E7&title=Views+Count&edge_flat=false)](https://github.com/NoNameoN-A/Steal-Not-Safe)

# Functions
1. main()
2. get_photos(<photos' list>)
3. send_email(<photos' list>)

## main()
I wrote this function just to manage else functions

## get_photos(<photos' list>)
In this function i use 2 lib
1. import cv2
2. import time
Whit `camera = cv2.VideoCapture(0)` i get the first cam available, then get a photo with `return_value, image = camera.read()` and save with a name like safe0.png then safe1.png then safe2.png and more...
Append the name of the photo on the photos' list and save the photo.

## send_email(<photos' list>)
1. Set all data `#To be changed` with your data
2. In 28 lines will create a MIMEMultipart object that you'll use to create the message that will be sent with the email
3. in the `with` at 42 line you'll log in on your email then attach on the email the photos encoding in base64 using `from email import encoders` then send the email.

## Guida In Italiano Step-By-Step in progress...
