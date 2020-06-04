import usb.core

VENDORID = 0x8086
PRODUCTID = 0x0808

def MicTest():
	dev = usb.core.find(find_all=True)
	for cfg in dev:
		print(str(cfg.idVendor) + ": " + str(cfg.idProduct))
	# dev = usb.core.find(idVendor=VENDORID, idProduct=PRODUCTID)
	# if dev is None:
 #    	raise ValueError('Our device is not connected')


if __name__ == "__main__":
	MicTest()
   