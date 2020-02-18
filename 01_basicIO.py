#!/usr/bin/env python3


import serial
import os
import time
import binascii
import helper
from datetime import datetime


ser=serial.Serial('/dev/ttyACM0')
message = bytearray()
payload = bytearray()
message.extend([0xB5, 0x62]) #header
payload.extend([0x06, 0x08]) #class, id
payload.extend([0x06,0x00])#length
payload.extend([0x00,0x10]) # meas time
payload.extend([0x01,0x00]) # navRate
payload.extend([0x01,0x00]) #  timeRef

checksum= helper.getFletcher(payload)

message.extend(payload)
message.extend(checksum)

ser.write(message)


print (datetime.now())
while 1:
    bufferLength = ser.inWaiting()
    answer = ser.read(bufferLength)
    hexAnswer =  bytesToHexStr(answer)
    if hexAnswer.startswith("b5 62"):
        pass
    print (datetime.now(), answer)
    print (datetime.now(), hexAnswer)

    ser.write(message)
    time.sleep(0.2)

