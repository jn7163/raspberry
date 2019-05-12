# raspberry
基于树莓派3B+的环境数据收集系统,可在Web上实时观测数据及触发报警
dht11.py

自动执行代码并上传数据
sudo crontab -e

*/1 * * * * python /home/pi/pi/test/dht11/dht11.py #温度湿度检测

*/1 * * * * python /home/pi/pi/test/dht11/hum_data_up.py #湿度上传至onenet平台

*/1 * * * * python /home/pi/pi/test/dht11/tmp_data_up.py #温度上传至onenet平台

