import asyncio
# from bleak import BleakClient, BleakScanner
# from bleak.backends.characteristic import BleakGATTCharacteristic
# from bleak.backends.device import BLEDevice
# from bleak.backends.scanner import AdvertisementData

class SpikeMessenger(object):
	def __init__(self):
		pass

	def move(self, speed, direction):
		print(f'moving in direction {direction} at speed {speed}') 
		