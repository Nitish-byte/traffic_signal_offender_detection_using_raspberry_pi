#----------------------------------------------------------------------------------------------------------------
# @traffic_offender_detection.py
# @brief This code detects, captures and notifies the car number plate breaking the traffic signal.
#
# Workflow of the code:
# Red_light_on -> if car is passed it is detected by ultrasonic sensor -> Camera captures the number plate ->
# Text is recognized on the number plate using pytesseract -> mail is sent using smtp 
#
# @author Nitish Wadhavkar
# @date 7th April 2019 
#
#----------------------------------------------------------------------------------------------------------------
#************************************CODE STARTS HERE************************************************************
#*----------------------------------IMPORTING LIBRARIES---------------------------------------------------------*
import RPi.GPIO as GPIO
import time
import picamera     
from PIL import Image
import pytesseract
import smtplib
#*------------*--------------*--------------*--------------*--------------*---------------*-----------*---------*

#*----------------------------ASSIGNING VARIABLES AND PORTS-----------------------------------------------------*
GPIO.setmode(GPIO.BOARD)

GPIO_TRIGGER = 12
GPIO_ECHO = 18
GPIO_DETECT=16
RED=33
AMBER=35
GREEN=22

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.setup(GPIO_DETECT,GPIO.OUT)
GPIO.setup(RED,GPIO.OUT)
GPIO.setup(GREEN,GPIO.OUT)
GPIO.setup(AMBER,GPIO.OUT)

RED_time=10
AMBER_time=2
GREEN_time=6
count=0

plate="MH 05 SS 9098"
filename = '/home/pi/Documents/car_image.png'

smtpUser='Enter addr of sender'
smtpPass='pass of sender'

toAdd='addr of receiver'
fromAdd=smtpUser

subject='RULE VIOLATION'
header='To:  ' + toAdd  +'\n'  +  'From:   '  +fromAdd  +  '\n'  +  'Subject:  '  +  subject
body= ' This letter is to inform you regarding the violation of rules and regulations of the traffic authority and your penalty for the same.'

#*-----------*-------------*-------------*-------------*-------------*-------------*--------------*-------------*


#*----------------------------------MAIN CODE-------------------------------------------------------------------*
while 1:
#*----------------------------------RED LIGHT-------------------------------------------------------------------*
    for count in range(0,100,1):
        GPIO.output(RED,1)
        GPIO.output(GREEN,0)
        GPIO.output(AMBER,0)
        time.sleep(RED_time/100)
#*-----------------CALCULATING DISTANCE USING ULTRASONIC SENSOR-------------------------------------------------*
        GPIO.output(GPIO_TRIGGER, True)
        time.sleep(0.00001)
        GPIO.output(GPIO_TRIGGER, False)
        StartTime = time.time()
        StopTime = time.time()
 
        while GPIO.input(GPIO_ECHO) == 0:
            StartTime = time.time()
 
        while GPIO.input(GPIO_ECHO) == 1:
            StopTime = time.time()
        
        TimeElapsed = StopTime - StartTime
        distance = (TimeElapsed * 34300) / 2
#*------------*-------------*-------------*------------*------------*-------------*--------------*--------------*
        #print ("Measured Distance = %.1f cm" % distance)
#*-------------------CHECKING WHETHER THE CAR CROSSED LINE------------------------------------------------------*
        if distance<20:
#*--------------------------------CAPTURE PHOTO-----------------------------------------------------------------*
            GPIO.output(GPIO_DETECT, True)
            camera = picamera.PiCamera()
            camera.capture(filename)
            camera.close()
#*---------------*---------------*----------------*----------------*------------*-----------*----------*--------*
#*----------------------------DETECT TEXT & SEND MAIL-----------------------------------------------------------*
            if (pytesseract.image_to_string(Image.open(filename)))==plate :
                
                s= smtplib.SMTP('smtp.gmail.com',587)
                s.ehlo()
                s.starttls()
                s.ehlo()
                s.login(smtpUser,smtpPass)
                s.sendmail(fromAdd, toAdd ,header  + '\n'  + body)
                s.quit()
        else :
            GPIO.output(GPIO_DETECT, False)
#*------------*-------------*----------*----------*--------------*-----------------*---------------*------------*
#*------------*-------------*----------*----------*--------------*-----------------*---------------*------------*
#*------------*-------------*----------*----------*--------------*-----------------*---------------*------------*
#*----------------------------------YELLOW LIGHT----------------------------------------------------------------*
    GPIO.output(RED,0)
    GPIO.output(GREEN,0)
    GPIO.output(AMBER,1)
    time.sleep(AMBER_time)
#*-------------*--------------*---------------*--------------*---------------*-------------*-----------*--------*

#------------------------------------GREEN LIGHT----------------------------------------------------------------*
    GPIO.output(RED,0)
    GPIO.output(AMBER,0)
    GPIO.output(GREEN,1)
    time.sleep(GREEN_time)
#*-------------*------------*------------*-------------*--------------*--------------*--------------*-----------*

#************************************CODE ENDS HERE**************************************************************
    
