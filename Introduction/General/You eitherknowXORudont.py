from base64 import decode
from pwn import xor


hex = '0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e26345115010'
flagbytes = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')


flagxor = xor(flagbytes,b'myXORkey')

flag =  ((flagxor).decode())

print (flag)

