from pwn import * # pip install pwntools
import json
import base64
import codecs
from Crypto.Util.number import bytes_to_long, long_to_bytes


r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)





def decode_(encoding, msg):
    decoded = ""
    
    if encoding == "base64":
        decoded = base64.b64decode(msg).decode() # wow so encode

    elif encoding == "hex":
        decoded =  bytes.fromhex(msg).decode

    elif encoding == "rot13":
        decoded = codecs.decode(msg,"rot13")

    elif encoding == "bigint":
        decoded = long_to_bytes(int(msg,16)).decode()

    elif encoding == "utf-8":
        decoded = "".join([chr(x) for x in msg])

    return decoded


#
#print("Received type: ")
#print(received["type"])
#print("Received encoded value: ")
#print(received["encoded"])


#

#json_recv()

count = 0

while (count := count + 1) < 101:
    received = json_recv()
    print(received)
    to_send = {"decoded": decode_(received["type"], received["encoded"])}

    json_send(to_send)