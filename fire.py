import RPi.GPIO as GPIO
 
import time
 
GPIO.setmode(GPIO.BCM)
 
GPIO.setup(21,GPIO.IN)
 
while True:
 
  if GPIO.input(21):
     print("no fire")
  else:
     print("fire detected")
    
  time.sleep(1)
