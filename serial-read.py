
import time
import serial
import csv

ser = serial.Serial(  
   port='/dev/ttymxc0',
   baudrate = 115200,
   parity=serial.PARITY_NONE,
   stopbits=serial.STOPBITS_ONE,
   bytesize=serial.EIGHTBITS,
   timeout=1
)


while 1:
   x=ser.readline()

   if x is  '':
      continue

   print(x.strip())
