主程序


#!/usr/bin/python
import RPi.GPIO as GPIO
import time
 
channel =2 
data = []
j = 0
 
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
 
tmp_output.close
hud_output.close
GPIO.cleanup()


上传温度数据代码

import urllib2
import json
import time
import datetime
 
APIKEY = '你的APIKey'  
        
        
def http_put():
        file = open("/home/pi/dht11/tmp_data.txt")
        temperature= float(file.read())
        CurTime = datetime.datetime.now()
        url='http://api.heclouds.com/devices/你的设备ID/datapoints'
        values={'datastreams':[{"id":"temp","datapoints":[{"at":CurTime.isoformat(),"value":temperature}]}]}
 
        print "the time is: %s" %CurTime.isoformat()
        print "The upload temperature value is: %.3f" %temperature
 
        jdata = json.dumps(values)
        print jdata
        request = urllib2.Request(url, jdata)
        request.add_header('api-key', APIKEY)
        request.get_method = lambda:'POST'
        request = urllib2.urlopen(request)
        return request.read()
 
while True:
        time.sleep(5)
        resp = http_put()
        print "OneNET result:\n %s" %resp
        time.sleep(5)


上传湿度数据代码

import urllib2
import json
import time
import datetime
 
APIKEY = '你的APIKey'  
        
        
def http_put():
        file = open("/home/pi/dht11/hum_data.txt")
        humidity= float(file.read())
        CurTime = datetime.datetime.now()
        url='http://api.heclouds.com/devices/你的设备ID/datapoints'
        values={'datastreams':[{"id":"hum","datapoints":[{"at":CurTime.isoformat(),"value":humidity}]}]}
 
        print "the time is: %s" %CurTime.isoformat()
        print "The upload humidity value is: %.3f" %humidity
 
        jdata = json.dumps(values)
        print jdata
        request = urllib2.Request(url, jdata)
        request.add_header('api-key', APIKEY)
        request.get_method = lambda:'POST'
        request = urllib2.urlopen(request)
        return request.read()
 
 
time.sleep(5)
resp = http_put()
print "OneNET result:\n %s" %resp
file.closes
