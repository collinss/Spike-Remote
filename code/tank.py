import bluetooth

BLUETOOTH_CONNECT_EVENT     = 1
BLUETOOTH_DISCONNECT_EVENT  = 2

# class to handle interfacing with a bluetooth low energy device (ble) using micropython libraries
class BluetoothServer(object):
    def __init__(self, addr):
        self.addr = addr
        self.ble = bluetooth.BLE()
        
        self.ble.active(True)
        self.ble.config(
            # device_name='spike',
            gap_name='spike',
            bond=True
        )

        self.ble.irq(self.on_event)
        
        self.ble.gap_advertise(1000, bytes(self.addr, 'utf-8'))
        
    def on_event(self, event, data):
        if event == BLUETOOTH_CONNECT_EVENT:
            print('connected to {}'.format(data))
        elif event == BLUETOOTH_DISCONNECT_EVENT:
            print('disconnected from {}'.format(data))
        else:
            print('unknown event', event, data)

if __name__ == '__main__':
    BluetoothServer('hello')
