import time
while True:
	file = open("/gpio/pin25/value","r")
	t = file.read()
	print(t)
	t = int(t) 
	file2 = open("/gpio/pin21/value","w")
	if(t==1):
		file2.write("0\n")
	elif(t==0):
		file2.write("1\n")

	file3 = open("/gpio/pin22/value","w")
	file3.write("1\n")
	file3.close()
	time.sleep(0.1)
	file3 = open("/gpio/pin22/value","w")
	file3.write("0\n")
	file3.close()
	time.sleep(0.1)
	file.close()
	file2.close()
	
