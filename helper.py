import binascii

def hexStrToByteArray(inputString):
    stringArray= inputString.lower().split(" ")
    return bytearray([int(s,16) for s in stringArray])

def bytesToHexStr(inputByteArray):
    inputString = binascii.hexlify(inputByteArray).decode()
    stringArray=[]
    while len(inputString) > 1:
        stringArray.append(inputString[:2])
        inputString = inputString[2:]
    return " ".join(stringArray)

def getFletcher(payload):
    CK_A=0
    CK_B=0
    for b in payload:
        CK_A +=b 
        CK_A %=256
        CK_B = CK_B + CK_A
        CK_B %=256
        #print (b, CK_A, CK_B)
    
    return bytearray([CK_A, CK_B])