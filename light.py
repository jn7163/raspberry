#Light
GPIO.setmode(GPIO.BCM)
GPIO.setup(20,GPIO.IN)
GPIO.setup(26,GPIO.OUT)
 
GPIO.output(26,GPIO.LOW)
for i in range(0,20):
    if GPIO.input(20)==1:
        GPIO.output(26,GPIO.HIGH)
    else:
        GPIO.output(26,GPIO.LOW)
 
    time.sleep(1)
    
    print GPIO.input(20)
