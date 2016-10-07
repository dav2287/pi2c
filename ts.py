import smbus, time, datetime
import sqlite3

bus = smbus.SMBus(1)

def get_readings():
	for addr in range(0x29, 0x2b, 1):
		bus.write_byte(addr, 0x00)

		time.sleep(0.001)

		value = bus.read_word_data(addr, 2)
		print "Addr: {} \t Value: {}".format(addr,value)

		curs.execute("INSERT INTO value_log values ( (?), (?), (?) )", (int(time.time()), addr, value))
		conn.commit

conn=sqlite3.connect('values.db')

curs=conn.cursor()

while True:
	try:
		get_readings()

		time.sleep(10)
	except KeyboardInterrupt:
		raise