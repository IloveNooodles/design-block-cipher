from random import randbytes, randint

from pwn import bits_str, xor

from src.IES import IES

# ? Variables, adjust as necessary
key = b'b' * 16
iv = randbytes(16)
cipher = IES(key, IES.MODE_CBC, iv)
byte_count = 16

# ? May want to use determined input
payload = randbytes(byte_count)
error_byte_index = randint(0, byte_count - 1)
error_bit_index = randint(0, 7)

print(f"Payload: {payload}\n")

error_mask = 1 << error_bit_index
error_payload = bytearray(payload)
error_payload[error_byte_index] ^= error_mask
# ? May want to use determined error
error_payload = bytes(error_payload)

print(f"Error payload: {error_payload}\n")


encrypted_payload = cipher.encrypt(payload)
encrypted_error_payload = cipher.encrypt(error_payload)


print(f"Encrypted: {encrypted_payload}\n")
print(f"Encrypted error: {encrypted_error_payload}\n")


symdiff = xor(encrypted_payload, encrypted_error_payload)

same_bytes = sum(1 for byte in symdiff if byte == 0)
diff_bytes = len(payload) - same_bytes
diff_bits = bits_str(symdiff).count("1")


encrypted_bits = bits_str(encrypted_payload)
encrypted_error_bits = bits_str(encrypted_error_payload)

for i in range(len(encrypted_bits)):
    bit = encrypted_bits[i]
    if bit == encrypted_error_bits[i]:
        print(f"\x1b[31m{bit}\x1b[0m", end="")
    else:
        print(f"\x1b[32m{bit}\x1b[0m", end="")
print()

for i in range(len(encrypted_error_bits)):
    bit = encrypted_error_bits[i]
    if bit == encrypted_bits[i]:
        print(f"\x1b[31m{bit}\x1b[0m", end="")
    else:
        print(f"\x1b[32m{bit}\x1b[0m", end="")
print()

print(
    f"Different bytes : {diff_bytes}/{len(payload)} | {diff_bytes / len(payload) * 100}%")
print(
    f"Different bits  : {diff_bits}/{len(payload) * 8} | {diff_bits / (len(payload) * 8) * 100}%")
