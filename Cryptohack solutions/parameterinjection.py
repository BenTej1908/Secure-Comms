import socket
import json
import hashlib
from Crypto.Cipher import AES
    
def duh(s):
    s.connect((HOST,PORT))
    s.recv(1024)
    data = s.recv(804)
    data2 = json.loads(data)
    p = int(data2['p'],16)
    A = int(data2['A'],16)
    # print("P is : " , p ,"\ng is :",g,"\nA is : ",A)
    s.recv(100)


    s.send(data)
    s.recv(1024)
    data3 = s.recv(404-9)
    # print(data3)
    #your public key
    data3 = b'{"B" : "0x83e907190b6484aa982847f873111a28a3f1a0617a0973b24f8ed036d01d01009f050fa636cfe030cdd26f1309465cdea4ebc97d421fa5ebeedda63d948c8b00e81c8e8e63e720ad74bf867139ac2112883928d0441290f9f40e67a44e4447b7f8841f6f573b8b6a85d679bb611d7f026a4c2c904dd4a97a2d0048531f43b78e7c539d9e59149229ed32630506d11f13b42609bb4b8c4644e0f3ede537022ac7de96288c1794746f3f57b25a2668363a4314879c3834a9961ba3800f7de4798d"}'

    s.recv(100)
    s.send(data3)
    s.recv(20+4)
    enc = s.recv(1000).strip().decode()
    enc = json.loads(enc)
    iv = enc['iv']
    enc_flag = enc['encrypted_flag']
    # print("iv is:",iv,"\nEncrypted flag is :",enc_flag)
    return A,p,enc_flag,iv


# print shared key
def dec(shared_key,enc_flag,iv):
    sha1 = hashlib.sha1()
    sha1.update(str(shared_key).encode('ascii'))
    key = sha1.digest()[:16]
    ciphertext = bytes.fromhex(enc_flag)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

if __name__ == "__main__":
    HOST = "socket.cryptohack.org"
    PORT = 13371

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Alice_pub,prime,enc_flag,iv = duh(sock)
    #private key
    private_key = 197395083814907028991785772714920885908249341925650951555219049411298436217190605190824934787336279228785809783531814507661385111220639329358048196339626065676869119737979175531770768861808581110311903548567424039264485661330995221907803300824165469977099494284722831845653985392791480264712091293580274947132480402319812110462641143884577706335859190668240694680261160210609506891842793868297672619625924001403035676872189455767944077542198064499486164431451944
    shared_key = pow(Alice_pub,private_key,prime)
    flag = dec(shared_key,enc_flag,iv).decode()
    print("Flag is :",flag)