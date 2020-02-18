#!/usr/bin/env python3

import socket
import time
import serial
import helper
from nmeamessages import *
import fletcher

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# set rate B5 62 06 08 06 00 64 00 01 00 01 00 7A 12  // 100 ms - lil endian!!
# set rate B5 62 06 08 06 00 E8 03 01 00 01 00 01 39 // 1000ms

ser=serial.Serial('/dev/ttyACM0')
ser.baudrate = 115200


while 1:
    bufferLength=ser.inWaiting()
    bytesFromGPS = ser.read(bufferLength)
    msg = getFirstNMEAMessage(bytesFromGPS) + b'\r\n'
    if len(msg) > 10:
        sock.sendto(msg,('255.255.255.255',6666))
    if len(bytesFromGPS) > 10:
        print(bytesFromGPS)
    time.sleep(0.1)