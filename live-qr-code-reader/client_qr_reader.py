import socket
import numpy as np
import cv2
import struct

# TCP bağlantısı kurma
server_ip = '10.0.0.169'  # Jetson Nano IP adresi
server_port = 12345
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))
print("Connected to the server")

while True:
    # Veri boyutunu al
    data = client_socket.recv(4)
    if not data:
        break
    data_size = struct.unpack('!I', data)[0]

    # Görüntü verisini al
    frame_data = b""
    while len(frame_data) < data_size:
        packet = client_socket.recv(data_size - len(frame_data))
        if not packet:
            break
        frame_data += packet

    # Görüntüyü decode et
    np_array = np.frombuffer(frame_data, dtype=np.uint8)
    frame = cv2.imdecode(np_array, cv2.IMREAD_COLOR)

    if frame is not None:
        cv2.imshow("Received Video", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

client_socket.close()
cv2.destroyAllWindows()
