import bluetooth
import motor_pair
from hub import port
from time import sleep

BLUETOOTH_CONNECT_EVENT     = 1
BLUETOOTH_DISCONNECT_EVENT  = 2
class BluetoothServer(object):
    """ class to handle interfacing with a bluetooth low energy device (ble) using micropython libraries """
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

class TankControl(object):
    """ Class to abstract the interface with the motors and sensors """
    def __init__(self,  motor_left, motor_right):
        self.motor_left = motor_left
        self.motor_right = motor_right
        motor_pair.pair(motor_pair.PAIR_1, self.motor_left, self.motor_right)

    def forward(self):
        motor_pair.move(motor_pair.PAIR_1, 400)

    def stop(self):
        motor_pair.stop(motor_pair.PAIR_1)

if __name__ == '__main__':
    BluetoothServer('hello')
    tank = TankControl(port.A, port.B)
    tank.forward()
    sleep(10)
    tank.stop()
