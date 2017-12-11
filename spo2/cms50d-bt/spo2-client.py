#!/usr/bin/env python
"""
Sample PoC code to get the Contec device to dump its data over bluetooth.

Due to the fact that we are running an lescan to discover the device before proceeding, means that this program must be run as a privileged user.

"""

from bluetooth.ble import DiscoveryService
import bluetooth, sys, re

"""This is where you should plug your device MAC address, it can be found by issuing: hcitool lescan"""
ADDRESS = 'aa:bb:cc:dd:ee:ff'

service = DiscoveryService()
devices = service.discover(5)

found = 0

for address, name in devices.items():
    if address == ADDRESS:
        print "Found:",  address
        found = 1

if found == 0:
    print """Could not find oximeter"""
    sys.exit(1)

service = bluetooth.find_service(name='SerialPort', address=ADDRESS)

if len(service) == 0:
    print """Found oximeter, did not find the bluetooth serial port"""
    sys.exit(1)

sp = service[0]

print("""Connecting to service %s, on %s, port num %d""" % (sp['name'], ADDRESS, sp['port']))


sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((ADDRESS, sp['port']))

print """Connected, sending first stuff."""

print """Asking for device number..."""
sock.send("\x53\x4e\x08\x00\x02\x01\x53\x49\x4e\x4f\x44")
device = sock.recv(1024)

print """Sending clock for good measure... heh..."""
# This resets the clock on the device to a known time.
# The last byte seems to be some form of checksum that ranges from 0x40-ish to 0x7d-ish
# I tried to make something to calculate this number, but prevailed when the date was too far in the future.
# Let me know if you can figure it out.... :(
# 2017-12-02 02:30:00 = \x11 (17) \x0c (12) \x02 (02) \x02 (02) \x1e (30) \x00 (00) .. then \x64 which is 100.. it will fail if you use some other number
sock.send("\x93\x8e\x0a\x00\x08\x02\x11\x0c\x02\x02\x1e\x00\x64")
print sock.recv(1024)

print device
print """Asking for user"""
sock.send("\x93\x8e\x0d\x00\x08\x10\x00\x00\x00\x00\x18\x00\x00\x01\x02\x40")
user = sock.recv(1024)
print user
print """Asking for data dump"""
sock.send("\x93\x8e\x04\x00\x08\x04\x10")
data = sock.recv(1024)
print data


fp = open('datadump.hex', 'w')
fp.write(data)
fp.close()

print """Wrote the file datadump.hex with your data."""
