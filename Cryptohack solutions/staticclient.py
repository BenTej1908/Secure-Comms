from pwn import remote
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib


def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')



HOST = "socket.cryptohack.org"
PORT = 13373
p = remote(HOST, PORT, typ='tcp')

p.recvuntil("p\": \"")
prime = p.recvuntil("\"")
prime = prime.decode()
prime = prime.replace("\"", "")
p.recvuntil("A\": \"")
A = p.recvuntil("\"}")
A = A.decode()
A = A.replace("\"}", "")

p.recvuntil("Intercepted from Alice: {\"iv\": \"")
iv = p.recvuntil("\"")
iv = iv.decode()
iv = iv.replace("\"", "")

p.recvuntil("encrypted\": \"")
cipher = p.recvuntil("\"}")
cipher = cipher.decode()
cipher = cipher.replace("\"}", "")

p.recvuntil("Bob connects to you, send him some parameters: ")
payload = "{"
payload += "\"p\": \"{}\", \"g\": \"{}\", \"A\": \"0x02\"".format(prime, A)
payload += "}"
p.sendline(payload)

p.recvuntil("B\": \"")
B = p.recvuntil("\"}")
B = B.decode()
B = B.replace("\"}", "")
shared = int(B, 16)

print(decrypt_flag(shared, iv, cipher))