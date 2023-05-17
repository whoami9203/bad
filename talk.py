from pwn import *
import time


def connect_to_c2_agent(cmdId, data):
    print("cmdId: ", cmdId.decode())
    io = remote("127.0.0.1", 7373)
    header = b'nslab_w31c0m3_U\x00'
    cmd = cmdId + b'\x00' * ( 4 - len(cmdId) )
    content = header + cmd + data
    io.send(content)
    time.sleep(0.000001)
    output = recvrepeat(timeout=0.00001)
    print(output)
    io.close()



number_str = "0123456789"

for x1 in range(10):
    for x2 in range(10):
        for x3 in range(10):
            for x4 in range(10):
                cmdId = str.encode(number_str[x1] + number_str[x2] + number_str[x3] + number_str[x4])
                if cmdId.decode() != "0003" :
                    connect_to_c2_agent(cmdId, b"data")
                    time.sleep(0.000001)
