import asyncio
import threading
from bleak import BleakClient, BleakScanner
from bleak.backends.characteristic import BleakGATTCharacteristic
from bleak.backends.device import BLEDevice
from bleak.backends.scanner import AdvertisementData

SCAN_TIMEOUT = 10.0

SERVICE_UUID = "0000fd02-0000-1000-8000-00805f9b34fb"   # The UUID of the lego service
RX_CHAR = "0000fd02-0001-1000-8000-00805f9b34fb"        # The UUID the hub will receive data on
TX_CHAR = "0000fd02-0002-1000-8000-00805f9b34fb"        # The UUID the hub will transmit data on

class SpikeMessenger(object):
    def __init__(self):
        pass
        # device = await BleakScanner.find_device_by_filter(filterfunc=self.service_uuid_is_match, timeout=SCAN_TIMEOUT)

    def move(self, speed, direction):
        print(f'moving in direction {direction} at speed {speed}')

    # def service_uuid_is_match(self, device: BLEDevice, adv: AdvertisementData) -> bool:
    #     return SERVICE_UUID.lower() in adv.service_uuids

    def scan(self, callback):
        # thread = threading.Thread(target=self._scan, args=(callback,))
        # thread.start()

        asyncio.async(self._scan(callback))

        # asyncio.to_thread(self._scan())

    async def _scan(self, callback):
        async with BleakScanner(detection_callback=callback) as scanner:
            for i in range(SCAN_TIMEOUT):
                sleep(1)

            # devices = scanner.get_discovered_devices(timeout=SCAN_TIMEOUT)

        # return devices

    def connect(self, device):
        asyncio.async(self._connect(device))

    async def _connect(self, device):
        self.client = BleakClient(device)

        self.service = client.services.get_service(SERVICE)
        self.rx_char = service.get_characteristic(RX_CHAR)
        self.tx_char = service.get_characteristic(TX_CHAR)

        # send info request first to get extra info

        # enable device notifications

        # clear the program in the example slot

        # start a new file upload

        # transfer the program in chunks

        # start the program

    def message(self, message):
        raise NotImplementedError

    def request(self, message):
        # calls message and waits for response
        raise NotImplementedError


