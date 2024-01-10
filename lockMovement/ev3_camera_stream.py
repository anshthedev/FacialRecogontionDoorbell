#!/usr/bin/env python3


from ev3dev2.sensor.lego import VisionSensor
import socket
import cv2
import numpy as np

# Create a VisionSensor object for the Logitech camera
camera = VisionSensor()
camera.mode = 'GRB'

# Configure socket connection
server_address = ('192.168.86.37', 12345)  # Replace with your computer's IP address
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(server_address)

try:
    while True:
        # Capture an image from the camera
        img = camera.image
        img_array = np.array(img)

        # Encode the image as a JPEG
        _, img_encoded = cv2.imencode('.jpg', img_array)

        # Send the encoded image to the computer
        data = img_encoded.tobytes()
        sock.sendall(data)

finally:
    sock.close()
