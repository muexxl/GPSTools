#!/usr/bin/env python3


def extractNMEAmessage(msg):
    NMEA_msg=bytearray()
    NMEA_msg=msg.split(b'\r\n')[0]
    msg=msg[len(NMEA_msg):]
    return NMEA_msg

def getFirstNMEAMessage(msg):
    NMEAMessage=bytearray()
    while len(msg) > 1:
        if msg.startswith(b'$GNGGA'):
            NMEAMessage = extractNMEAmessage(msg)
            break
        msg=msg[1:]
    return NMEAMessage
