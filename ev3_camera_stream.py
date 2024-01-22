#!/usr/bin/env python3


# ev3_camera_stream.py

from ev3dev.ev3 import *
import usb.core
import usb.util

motor = LargeMotor('outB')  # Use 'outB' for motor on port B

def receive_signal():
    VENDOR_ID = 0x0694  # Replace with your actual Vendor ID
    PRODUCT_ID = 0x0005  # Replace with your actual Product ID

    # Find the USB device
    dev = usb.core.find(idVendor=VENDOR_ID, idProduct=PRODUCT_ID)

    if dev is None:
        raise ValueError("Device not found")

    try:
        # Detach the kernel driver from the device
        if dev.is_kernel_driver_active(0):
            dev.detach_kernel_driver(0)

        # Set the configuration
        dev.set_configuration()

        # Receive data
        data = dev.read(0x81, 64, 1000)  # Endpoint 0x81, 64 bytes, timeout 1000ms

        print("Received data: {}".format(data))

        # Run the motor on port B for 5 rotations if the received data matches the expected signal
        if data == b"Face detected!":
            motor.run_to_rel_pos(position_sp=5 * 360, speed_sp=500, stop_action="brake")  # 5 rotations at speed 500

    finally:
        # Release the device
        usb.util.release_interface(dev, 0)

while True:
    receive_signal()
    # Continue with other EV3 code as needed
    # This script will keep running and listening for signals
