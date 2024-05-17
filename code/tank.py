import bluetooth

BLUETOOTH_CONNECT_EVENT = 0x1
BLUETOOTH_DISCONNECT_EVENT = 0x2

# class to handle interfacing with a bluetooth low energy device (ble) using micropython libraries
class BluetoothServer(object):
    def __init__(self, addr):
        self.addr = addr
        self.ble = bluetooth.BLE()
        
        self.ble.active(True)
        self.ble.config(
            device_name='spike',
            gap_name='spike',
            bond=True
        )

        self.ble.irq(self.on_event)
        
        self.ble.gap_advertise(100, bytes(self.addr, 'utf-8'))
        
    def on_event(self, event, data):
        match event:
            case BLUETOOTH_CONNECT_EVENT:
                print('connected to {}'.format(data))
            case BLUETOOTH_DISCONNECT_EVENT:
                print('disconnected from {}'.format(data))
            case _:
                print('unknown event')
