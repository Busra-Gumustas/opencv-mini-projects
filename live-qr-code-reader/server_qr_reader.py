import cv2
import socket
import struct
from pyzbar.pyzbar import decode

# Kamera başlatma
cap = cv2.VideoCapture(0)  # Yerel kamera

# TCP bağlantısı kurma
server_ip = '10.0.0.169'  # Jetson Nano IP adresi
server_port = 12345
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, server_port))
server_socket.listen(1)
print("Server is waiting for a connection...")

# Client bağlantısını kabul et
conn, addr = server_socket.accept()
print(f"Connection established with {addr}")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # QR kodlarını tespit et
    decoded_objects = decode(frame)
    for obj in decoded_objects:
        qr_data = obj.data.decode("utf-8")
        print(f"QR Code Detected: {qr_data}")
        cv2.putText(frame, qr_data, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    # Görüntüyü encode et
    _, buffer = cv2.imencode('.jpg', frame)
    frame_bytes = buffer.tobytes()

    # Veri boyutunu gönder
    conn.sendall(struct.pack('!I', len(frame_bytes)))

    # Görüntü verisini gönder
    conn.sendall(frame_bytes)

cap.release()
conn.close()
server_socket.close()