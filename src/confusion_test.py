from IES import IES
from pwn import xor, bits_str
from random import randbytes, randint

# ? Variables, adjust as necessary
key = randbytes(16)
iv = randbytes(16)
mode = IES.MODE_CBC
cipher = IES(key, mode, iv)
byte_count = 1024

# ? May want to use determined input
payload = randbytes(byte_count)
error_byte_index = randint(0, 16)
error_bit_index = randint(0, 7)

print(f"Payload: {payload}\n")
print(f"Key: {key}\n")

error_mask = 1 << error_bit_index
error_key = bytearray(key)
error_key[error_byte_index] ^= error_mask
# ? May want to use determined error
error_key = bytes(error_key)
error_cipher = IES(error_key, mode, iv)

# print(f"Error key: {error_key}\n")

encrypted_payload = cipher.encrypt(payload)
encrypted_error_payload = error_cipher.encrypt(payload)


# print(f"Encrypted: {encrypted_payload}\n")
# print(f"Encrypted error: {encrypted_error_payload}\n")


symdiff = xor(encrypted_payload, encrypted_error_payload)

same_bytes = sum(1 for byte in symdiff if byte == 0)
diff_bytes = len(payload) - same_bytes
diff_bits = bits_str(symdiff).count("1")


encrypted_bits = bits_str(encrypted_payload)
encrypted_error_bits = bits_str(encrypted_error_payload)

# for i in range(len(encrypted_bits)):
#     bit = encrypted_bits[i]
#     if bit == encrypted_error_bits[i]:
#         print(f"\x1b[31m{bit}\x1b[0m", end="")
#     else:
#         print(f"\x1b[32m{bit}\x1b[0m", end="")
# print()

# for i in range(len(encrypted_error_bits)):
#     bit = encrypted_error_bits[i]
#     if bit == encrypted_bits[i]:
#         print(f"\x1b[31m{bit}\x1b[0m", end="")
#     else:
#         print(f"\x1b[32m{bit}\x1b[0m", end="")
# print()

print(
    f"Different bytes : {diff_bytes}/{len(payload)} | {diff_bytes / len(payload) * 100}%")
print(
    f"Different bits  : {diff_bits}/{len(payload) * 8} | {diff_bits / (len(payload) * 8) * 100}%")
