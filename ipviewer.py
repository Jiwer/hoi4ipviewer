import pydivert
import threading

#de0001000f0000000400 name packet 1
#160001000c00030000006b name packet 2
#160001000c0003000000ca name packet 3
#03001b0001000f00 name sep

PlayerIPs = set()
BlockedIPs = set()

def block(ip):
    if not type(ip) is str:
        print("\nIP must be in string format. An example block would be: block('69.168.1.30')")
        return

    BlockedIPs.add(ip)
    print("\nSuccessfully added " + ip + " to the block list.")

def networking():
    with pydivert.WinDivert("udp.PayloadLength > 0") as w:
        for packet in w:
            Hex1 = packet.payload.hex()

            if "de0001000f0000000400" in Hex1 and packet.src_addr not in PlayerIPs:
                NewHex1, NewHex2 = Hex1.split("03001b0001000f00", 1)
                NewHex3, NewHex4 = NewHex2.split("de0001000f0000000400", 1)
                print("\n" + bytearray.fromhex(NewHex3[4:]).decode() + " connected. " + packet.src_addr)
                PlayerIPs.add(packet.src_addr)

            if packet.src_addr in BlockedIPs or packet.dst_addr in BlockedIPs:
                packet.payload = "\x00\x01\x02".encode()

            w.send(packet)

threading.Thread(name='networking', target=networking).start() # required multithreading to allow user input without pausing windivert

print("\nHOI4 IP Viewer by Mastoid loaded.\nPlayer name and IP will be listed on connection.\nType block('ipaddresshere') to block an IP address.")
