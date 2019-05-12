# raspberry
基于树莓派3B+的环境数据收集系统
dht11.py

自动执行代码并上传数据
sudo crontab -e
*/1 * * * * python /home/pi/pi/test/dht11/dht11.py
*/1 * * * * python /home/pi/pi/test/dht11/hum_data_up.py
*/1 * * * * python /home/pi/pi/test/dht11/tmp_data_up.py
