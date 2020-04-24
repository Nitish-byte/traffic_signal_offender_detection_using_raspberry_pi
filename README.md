# traffic_signal_offender_detection_using_raspberry_pi
Traffic Light Image Processing &amp; Mailing System

Abstract:
While traffic policing remains one of the most important area in the management of road and
transportation of the city, state and the nation, increase in the number of offenders of traffic rules are the
main concern. An introduction to a system for recognizing and charging penalty for all these offenders is
necessary these days. Traffic police, in such situations with their old methods to handle them and with
limited manpower seems to be highly inefficient. Here, technology comes into picture, with
advancements in embedded systems with powerful microcontrollers and developments in IOT (Internet
Of Things) industry same task with good reliability and real time system can be done more efficiently
and subtly. Also with advanced IOT protocols, deep learning and image processing algorithms no
manual monitoring is needed from recognizing to charging fine to the offenders. This will, in future,
reduce the number of traffic rule offences and lead to a well-managed and ordered road transportation.

Components used in the circuit: 
1) Raspberry Pi 3B 
2) Ultrasonic Sensor 
3) 1 330 ohm, 1 470 ohm &amp;
3 resistors of any value
4) Red, yellow and green led 
5) Camera module
6) Jumper wires 
7) Breadboard
8) Micro pin power supply 
9) Led for detection.

1. Libraries used: GPIO used for accessing pins, time used for crating delay in the system, picamera
for accessing camera module, PIL for accessing an image from a file/folder, pytesseract for text
detection, smtplib for sending mail.
2. Variables and assigning of ports: Rpi pins are assigned to variables with their nature
(input/output), format of the mail sent is also assigned here.
3. Main code: It is run infinitely and is further divided in 4 parts
3.1 Traffic Lights: For each light the one which is on is set to 1 and others are set to 0 and a
time delay is inserted and for that duration led is on.
3.2 Taking picture: When red light is on, that specific loop is run multiple times with
ultrasonic sensor monitoring the distance of the width of the road every time. If a car
passes the sensor on red light it is detected and the if distance&lt;roadwidth: here 20cm is
true and the photo of the car with the number plate is captured and saved in the database.
3.3 Recognizing text: Pytesseract object pytesseract.image_to_string is used to get the
number plate text and is matched with the registered number in the database with mail id.
3.4 Sending mail: Simple mail transfer protocol is used to send mail to the address matched
with the text detection in the database.
