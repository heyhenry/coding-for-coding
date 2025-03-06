# credit: https://www.youtube.com/shorts/gikCisBPTgw

from cryptography.fernet import Fernet
import os

if not os.path.exists("encryption_key.txt"):
    key = Fernet.generate_key()
    with open("encryption_key.txt", "wb") as key_file:
        key_file.write(key)
else:
    with open("encryption_key.txt", "rb") as key_file:
        key = key_file.read()

def encrypt_file(org_file, enc_file):
    with open(org_file, "rb") as f:
        data = f.read()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)
    with open(enc_file, "wb") as f:
        f.write(encrypted)

def decrypt_file(enc_file, dec_file):
    with open(enc_file, "rb") as f:
        data = f.read()
    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)
    with open(dec_file, "wb") as f:
        f.write(decrypted)

f = Fernet(key)

VIDEO_FILE = "video.mp4"
ENCRYPTED_FILE = "video_encrypted.mp4"
DECRYPTED_FILE = "video_decrypted.mp4"

encrypt_file(VIDEO_FILE, ENCRYPTED_FILE)
decrypt_file(ENCRYPTED_FILE, DECRYPTED_FILE)
