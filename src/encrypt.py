from argparse import ArgumentParser
from IES import IES
from os import path

argparser = ArgumentParser()
argparser.add_argument("filepath", type=str)
argparser.add_argument("key", metavar="key-file-or-phrase", type=str)
argparser.add_argument("-M", "--mode", type=str)
argparser.add_argument("-iv", metavar="initial-vector-file", type=str)
argparser.add_argument(
    "-o", "--outfile", metavar="initial-vector-file", type=str, default="")

arg = argparser.parse_args()

mode_str = arg.mode.upper()
valid_modes = ["ECB", "CBC", "CFB", "OFB", "CTR"]
modes = [IES.MODE_ECB, IES.MODE_CBC, IES.MODE_CFB, IES.MODE_OFB, IES.MODE_CTR]

if mode_str not in valid_modes:
    print("Invalid mode")
    exit(1)

mode = modes[valid_modes.index(mode_str)]

# ? Get input payload
f = open(arg.filepath, "rb")
payload = f.read()
f.close()

# ? Pad input
pad_length = 0
if len(payload) % 16 != 0:
    pad_length = 16 - len(payload) % 16
    payload += b'\x00' * pad_length

pad_length_byte = pad_length.to_bytes(1, "big")

try:
    f = open(arg.key, "rb")
    key = f.read()
    f.close()
except:
    key = bytes(arg.key, encoding="utf-8")

if len(key) < 16:
    key = key * 16
if len(key) > 16:
    key = key[:16]

iv_len = 16
if mode == IES.MODE_CTR:
    iv_len //= 2
if mode == IES.MODE_ECB:
    iv_len = 0
iv_len_byte = iv_len.to_bytes(1, "big")

if mode_str != "ECB":
    f = open(arg.iv, "rb")
    iv = f.read()
    f.close()

    if len(iv) < iv_len:
        iv = iv * iv_len
    if len(iv) > iv_len:
        iv = iv[:iv_len]
else:
    iv = b''

cipher = IES(key, mode, iv)
result = cipher.encrypt(payload)

result = pad_length_byte + iv_len_byte + iv + result

result_path = arg.outfile
if result_path == "":
    directory, basename = path.split(arg.filepath)
    basename = "encrypted-" + basename
    result_path = path.join(directory, basename)

f = open(result_path, "wb")
f.write(result)
f.close()
