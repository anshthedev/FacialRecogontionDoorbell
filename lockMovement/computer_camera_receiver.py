# computer_camera_receiver.py

import socket
import cv2
import numpy as np

# Configure socket connection
server_address = ('192.168.86.37', 12345)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(server_address)
sock.listen(1)

print("Waiting for connection...")
connection, client_address = sock.accept()
print("Connected to", client_address)

try:
    while True:
        # Receive the encoded image
        data = connection.recv(4096)
        if not data:
            break

        # Decode the image and display it using OpenCV
        img_array = np.frombuffer(data, dtype=np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        cv2.imshow('Remote Camera', img)

        # Press 'q' to exit the video stream
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    connection.close()
    sock.close()
