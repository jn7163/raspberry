#!/usr/bin/python
#data/out GPIO.2 PIN.3
import RPi.GPIO as GPIO
import time
 
channel = 2 #temp
trig = 18  #buzzer
rain = 17  #rain
fire = 21  #fire
light = 20 #light
data = []
j = 0
a = 1
#buzzer
def init():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(trig, GPIO.OUT, initial=GPIO.HIGH)
    pass

def beep(seconds):
    GPIO.output(trig, GPIO.LOW)
    time.sleep(seconds)
    GPIO.output(trig, GPIO.HIGH)

def beepBatch(seconds, timespan, counts):
    for i in range(counts):
        beep(seconds)
        time.sleep(timespan)
 
GPIO.setmode(GPIO.BCM)
 
time.sleep(1)
 
GPIO.setup(channel, GPIO.OUT)
GPIO.output(channel, GPIO.LOW)
time.sleep(0.02)
GPIO.output(channel, GPIO.HIGH)
GPIO.setup(channel, GPIO.IN)
 
while GPIO.input(channel) == GPIO.LOW:
  continue
while GPIO.input(channel) == GPIO.HIGH:
  continue
 
while j < 40:
  k = 0
  while GPIO.input(channel) == GPIO.LOW:
    continue
  while GPIO.input(channel) == GPIO.HIGH:
    k += 1
    if k > 100:
      break
  if k < 8:
    data.append(0)
  else:
    data.append(1)
 
  j += 1
 
print "sensor is working."
print data
 
humidity_bit = data[0:8]
humidity_point_bit = data[8:16]
temperature_bit = data[16:24]
temperature_point_bit = data[24:32]
check_bit = data[32:40]
 
humidity = 0
humidity_point = 0
temperature = 0
temperature_point = 0
check = 0
 
for i in range(8):
  humidity += humidity_bit[i] * 2 ** (7-i)
  humidity_point += humidity_point_bit[i] * 2 ** (7-i)
  temperature += temperature_bit[i] * 2 ** (7-i)
  temperature_point += temperature_point_bit[i] * 2 ** (7-i)
  check += check_bit[i] * 2 ** (7-i)
 
tmp = humidity + humidity_point + temperature + temperature_point
 
if check == tmp:
  print "temperature :", temperature, "*C, humidity :", humidity, "%"
else:
  print "wrong"
  print "temperature :", temperature, "*C, humidity :", humidity, "% check :", check, ", tmp :", tmp

mytemp = '%f' %temperature
myhumi = '%f' %humidity
 
tmp_output = open('/home/pi/dht11/tmp_data.txt', 'w')
hud_output = open('/home/pi/dht11/hum_data.txt', 'w')
 
tmp_output.write(mytemp)
hud_output.write(myhumi)

#temp-buzzer
if temperature >40:
  init()
  beepBatch(0.1, 0.3, 3)
    
#rain-buzzer rain =0  norain =1
GPIO.setmode(GPIO.BCM)
GPIO.setup(rain,GPIO.IN) 
rainData = '%f' %(GPIO.input(rain))
if GPIO.input(rain):
    print("no rain")
    #rainData = 0
else:
     print("rain")
     #rainData = 1
     init()
     beep(0.1)
     beepBatch(0.3, 0.3, 5)
rain_output = open('/home/pi/dht11/rain_data.txt', 'w')
rain_output.write(rainData)

#fire-buzzer
GPIO.setmode(GPIO.BCM)
GPIO.setup(fire,GPIO.IN)

if GPIO.input(fire):
     print("no fire")
else:
     print("fire detected")
     init()
     beepBatch(0.1, 0.1, 10)


#Light
GPIO.setmode(GPIO.BCM)
GPIO.setup(light,GPIO.IN)
GPIO.setup(26,GPIO.OUT)
 
GPIO.output(26,GPIO.LOW)
if GPIO.input(light) == 1:
  GPIO.output(26,GPIO.HIGH)
  print("no light")
  init()
  beepBatch(0.1, 0.1, 2)
else:
  GPIO.output(26,GPIO.LOW)
  print("light")
  


#time.sleep(1)
tmp_output.close
hud_output.close
rain_output.close
GPIO.cleanup()
