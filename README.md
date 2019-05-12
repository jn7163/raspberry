# raspberry
#### 基于树莓派3B+的环境数据收集系统，可在Web上实时观测数据及触发报警
###### 拿着江老师的树莓派，手抖的，给学弟们留点文档 呃呃，挑战杯！

* dht11.py 温湿度采集
* rain.py  雨滴
* ligth.py 光敏
* fire.py 火焰
* source-buzzer.py  有源蜂鸣器
* bate.py 综合所有传感器 （阈值触发蜂鸣器）

自动执行代码并上传数据

    sudo crontab -e
     
    */1 * * * * python /home/pi/pi/test/dht11/dht11.py #温度湿度检测

    */1 * * * * python /home/pi/pi/test/dht11/hum_data_up.py #湿度上传至onenet平台

    */1 * * * * python /home/pi/pi/test/dht11/tmp_data_up.py #温度上传至onenet平台

## Demo
http://oker.ooo


## 架构
前端：Semantic UI + eCharts + JQuery Datapicker

后端：Python + Apache

* 支持断点续传
* json文件输出
* 后端轻量、稳定
 
 
## 接线方案
树莓派3B的GPIO图如下：
[![GPIO]](https://github.com)  
[GPIO]:https://github.com/yfgeek/rpi-TempRuntime/raw/master/images/2.png "GPIO"  

* 连接DHT11,数据传输到GPIO

      DHT11有3个脚,VCC,DATA,GND

      VCC,接 3.3V,PIN 01

      GND,接地,PIN 09

      DATA,接 GPIO26,PIN 37(根据程序里GPIO定义接)
* 其他接线 代码中都有定义

## 依赖
* Adafruit_DHT
* Nginx/Apache (请自行提前安装)

## 安装依赖
    sudo apt-get update
    sudo apt-get install python-dev python-rpi.gpio
    sudo apt-get install build-essential python-dev python-smbus python-pip
    git clone https://github.com/adafruit/Adafruit_Python_DHT.git
    cd Adafruit_Python_DHT
    sudo python setup.py install
    sudo pip install RPi.GPIO
    
## 运行
    python bate.py
    
## 后续等待更新...

[我的博客 okoke.cn](http://okoke.cn "okoke")  
