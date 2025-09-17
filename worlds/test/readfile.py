import os
def import_binary_bytes(file_name: str):
    with open(file_name, "rb") as f:
        data = f.read()
    return bytearray(data)

print(f"{os.listdir()}")