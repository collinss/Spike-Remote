import bluetooth

BLUETOOTH_SCAN_RESULT = 5
BLUETOOTH_SCAN_DONE   = 6

class BluetoothClient(object):
    def __init__(self, address):
        self.address = address

        self.ble = bluetooth.BLE()

        self.ble.active(True)
        self.ble.config(
            device_name='remote',
            gap_name='remote',
            bond=True
        )

        self.ble.irq(self.on_event)
        self.ble.gap_scan(0)

    def on_event(self, event, data):
        if event == BLUETOOTH_SCAN_RESULT:
            print(data)
        else:
            print('unknown event', event, data)
