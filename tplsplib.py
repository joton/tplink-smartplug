# Encryption and Decryption of TP-Link Smart Home Protocol
# XOR Autokey Cipher with starting key = 171


def encrypt(string):
    key = 171
    result = "\0\0\0\0"
    for i in string:
        a = key ^ ord(i)
        key = a
        result += chr(a)
    return result


def decrypt(string):
    key = 171
    result = ""
    for i in string:
        a = key ^ ord(i)
        key = ord(i)
        result += chr(a)
    return result


# Send command and receive reply
def sendrectplsp(cmd, ip, port):
    import socket
    try:
        sock_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock_tcp.connect((ip, port))
        sock_tcp.send(encrypt(cmd))
        data = sock_tcp.recv(2048)
        sock_tcp.close()
        return decrypt(data[4:])
    except socket.error:
        quit("Cound not connect to host " + ip + ":" + str(port))

def getConsumedEnergy(cmd, ip, port, dataRoot):
    msg = sendrectplsp(cmd, ip, port)
    m = json.loads(msg)
    en = [x['energy'] for x in json.loads(sendrectplsp(cmd, ip, port-2))['emeter']['get_daystat']['day_list']]
    
    
    
