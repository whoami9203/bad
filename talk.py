from pwn import *
import time


def connect_to_c2_agent(cmdId, data):
    print("Trying cmdId:", cmdId.decode())
    io = remote("127.0.0.1", 7373)
    header = b"nslab_w31c0m3_U\x00"
    cmd = cmdId + b"\x00" * (4 - len(cmdId))
    content = header + cmd + data
    io.send(content)
    time.sleep(0.001)
    io.close()


number_str = "0123456789"

# Iterate over each combination
for x1 in range(10):
    for x2 in range(10):
        for x3 in range(10):
            for x4 in range(10):
                cmdId = bumber_str[x1] + bumber_str[x2] + bumber_str[x3] + bumber_str[x4]   # Convert to bytes
                connect_to_c2_agent(cmdId, b"some_data")

                # Sleep to add delay between connections (adjust as needed)
                time.sleep(0.001)