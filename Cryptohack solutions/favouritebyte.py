
secret = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

decodehex = bytes.fromhex (secret)

secret2 = decodehex[0] ^ ord('c')

print (''.join(chr(c^secret2)for c in decodehex))
