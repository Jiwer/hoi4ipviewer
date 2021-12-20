#6d657774776f mewtwo hj packet

import pydivert
import threading
import socket

HostIPs = set()

HostIPs.add(socket.gethostbyname(socket.gethostname()))

def networking():
	with pydivert.WinDivert("udp.PayloadLength > 0") as w:
		for packet in w:
			Hex1 = packet.payload.hex()

			if packet.dst_addr not in HostIPs:
				if "de0001000f0000000400" in Hex1 or "010100000004" in Hex1 or "0100000000000030000000000000010002f0" in Hex1 or "00000002f00002" in Hex1:
					print("\nThe host IP is: " + packet.dst_addr + " | Port: " + str(packet.dst_port))
					HostIPs.add(packet.dst_addr)

			w.send(packet)

def dumpIPs():
	print(HostIPs)

threading.Thread(name='networking', target=networking).start() # required multithreading to allow user input without pausing windivert

print("\nHOI4 Host IP Revealer by Mastoid loaded.\nHost IP will be revealed when trying to make any connection to the game.\nType dumpIPs() to dump the HostIPs set.")
