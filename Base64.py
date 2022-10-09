import base64

flaghex = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

flagbyte = bytes.fromhex(flaghex)
print (flagbyte)



flag64 = base64.b64encode(flagbyte)

print (flag64)

#second output is solution

