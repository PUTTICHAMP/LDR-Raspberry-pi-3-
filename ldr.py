import RPi.GPIO as io
import time 

io.setmode(io.BCM)
io.setup(15, io.IN)
io.setup(14, io.OUT)

while 1:
	if io.input(15) == 0:
		io.output(14, 1)		
	else :
		io.output(14, 0)
