import smbus
import time

bus = smbus.SMBus(1)
#addr = 0x10

def get_readings():
	for addr in range(0x22, 0x2b, 1):
		try:
			bus.write_byte(addr, 0x00)
		except IOError, err:
			pass
			#print err
		time.sleep(.001)
		try:
			HighByte = bus.read_word_data(addr, 2)
			# LowByte = bus.read_byte(addr)
			# HB2 = bus.read_byte(addr)
			# LB2 = bus.read_byte(addr)
			print "Addr: {}  Value: {}".format(addr, HighByte)
			# print HighByte
		except IOError, err:
			# print err
			pass

while True:
	try:
		get_readings()

		time.sleep(5)
	except KeyboardInterrupt:
		raise

#print LowByte
#print HB2
#print LB2