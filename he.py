from itertools import product
from pwn import *
import time


def connect_to_c2_agent(cmdId, data):
    print("Trying cmdId:", cmdId.decode())
    io = remote("127.0.0.1", 7373)
    header = b"nslab_w31c0m3_U\x00"
    cmd = cmdId + b"\x00" * (4 - len(cmdId))
    content = header + cmd + data
    io.send(content)
    time.sleep(0.00001)
    io.close()


# Generate all possible combinations of cmdId
cmdId_combinations = product("9876543210", repeat=4)

# Iterate over each combination
for cmdId in cmdId_combinations:
    cmdId = "".join(cmdId).encode()  # Convert to bytes
    connect_to_c2_agent(cmdId, b"some_data")

    # Sleep to add delay between connections (adjust as needed)
    time.sleep(0.00001)
