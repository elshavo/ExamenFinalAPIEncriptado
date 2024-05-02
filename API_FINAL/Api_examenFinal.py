
#Api Final Lado del usuario 
#Mario Alberto González Méndez A00832313

import socket
from cryptography.fernet import Fernet
import os

# Encriptar archivo
def encrypt_file(key, file_name):
    """
    Le das una llave y un archivo, encripta el archivo y regresa el archivo encriptado
    """
    fernet = Fernet(key)
    with open(file_name, 'rb') as file:
        original = file.read()
    encrypted = fernet.encrypt(original)

    # Guarda los datos encriptados en un archivo
    with open('encrypted_image', 'wb') as enc_file:
        enc_file.write(encrypted)

    #Test para verificar que el archivo se encriptó correctamente si si BORRAR o comentar si no se quiere
    with open('encrypted_image_for_verification', 'wb') as enc_file:
        enc_file.write(encrypted)

    return encrypted

# Enviar archivo al servidor
def send_file_to_server(server_host, server_port, file_name):
    print(f"Connecting to server {server_host}:{server_port}...")  # Imprime detalles de la conexión
    key = Fernet.generate_key()  # Genera una llave
    print("Key generated.")

    encrypted = encrypt_file(key, file_name)  # Encripta el archivo
    print("File encrypted.")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((server_host, server_port))
        print("Connected to the server.")
        s.sendall(key + b'\n' + encrypted)  # Manda la llave y el archivo encriptado al servidor
        print("Key and encrypted file sent to the server.")  

# Iniciar función para enviar archivo al servidor:
send_file_to_server('localhost', 12345, 'image.png')