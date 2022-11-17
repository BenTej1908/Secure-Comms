from Crypto.PublicKey import RSA
key = RSA.importKey(open('bruce_rsa_6e7ecd53b443a97013397b1a1ea30e14.pub').read())
print(key.n)