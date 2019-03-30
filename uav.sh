if [ -f /var/opt/m4/m4last.fw ]
then
rm -f /var/opt/m4/m4last.fw
echo udooer | sudo -S reboot
else
arduino --port /dev/ttyMCC --upload ~/Desktop/aetdrone/Image-Processing-in-UAV/aruino-data/aruino-data.ino
python ~/Desktop/aetdrone/Image-Processing-in-UAV/udoo_sensor_data_read.py
fi  
