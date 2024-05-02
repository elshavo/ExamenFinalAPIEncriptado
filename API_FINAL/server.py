#Api Final lado del servidor
#Mario Alberto González Méndez A00832313

import socket
from cryptography.fernet import Fernet

# Desencriptar archivo
def decrypt_file(key, data):
    """
    Given a key and an encrypted data, it decrypts the data and returns the original data
    """
    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)

    # Guarda los datos desencriptados en un archivo
    with open('decrypted_image.png', 'wb') as dec_file:
        dec_file.write(decrypted)

    return decrypted

# Iniciar servidor
def start_server(host, port):
    print(f"Starting server on {host}:{port}...")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print("Server is listening...")
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            data = b""
            while True:
                packet = conn.recv(1024)
                if not packet:
                    break
                data += packet
            key, encrypted_data = data.split(b'\n', 1)
            decrypted = decrypt_file(key, encrypted_data)  # Desencriptar el archivo
            print("Data decrypted.")  # Imprime que se deencriptó el archivo

# Iniciar el servidor
start_server('localhost', 12345)