import cv2
import urllib.request
import numpy as np

url = "http://<192.168.86.37>:5000/video_feed"  # Replace with the EV3's IP address

while True:
    try:
        with urllib.request.urlopen(url) as stream:
            bytes = bytes()
            while True:
                bytes += stream.read(1024)
                a = bytes.find(b'\xff\xd8')
                b = bytes.find(b'\xff\xd9')
                if a != -1 and b != -1:
                    jpg = bytes[a:b + 2]
                    bytes = bytes[b + 2:]
                    frame = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
                    cv2.imshow('EV3 Webcam Stream', frame)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
    except KeyboardInterrupt:
        break

cv2.destroyAllWindows()
