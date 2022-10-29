from cryptography.hazmat.primitives.serialization import load_der_public_key
from cryptography.hazmat.primitives.asymmetric.ec import EllipticCurvePublicKey
from cryptography.hazmat.primitives.asymmetric.ec import SECP256R1
from cryptography.hazmat.primitives.asymmetric.ec import ECDH
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization

import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 5566  # Port to listen on (non-privileged ports are > 1023)

server_private_key = ec.generate_private_key(ec.SECP256R1)
server_public_key = server_private_key.public_key()
server_public_der = server_public_key.public_bytes(encoding=serialization.Encoding.DER, format=serialization.PublicFormat.SubjectPublicKeyInfo)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("listening")
    conn, addr = s.accept()
    print("accepted")
    with conn:
        print(f"Connected by {addr}")
        data = conn.recv(1024)
        client_public_key = load_der_public_key(data)
        print(client_public_key)
        conn.sendall(server_public_der)
        client_secret = conn.recv(1024)


shared_secret = server_private_key.exchange(ec.ECDH(), client_public_key)
print(shared_secret)
print(client_secret)

print(f"Are the two shared secrets identical? {shared_secret == client_secret}")
