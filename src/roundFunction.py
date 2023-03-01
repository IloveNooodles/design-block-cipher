from pwn import xor
from math import gcd
from typing import Callable
class RoundFunction:
    def get_f(self) -> Callable[[bytes, bytes], bytes]:
        return self._f

    def _f(self, input: bytes, round_key: bytes) -> bytes:
        temp = slice_box(input, round_key)
        return b"".join(temp)
    
    def _slice_box(self, input: bytes, key: bytes) -> (bytes, bytes):
        assert(len(key) == 2)
        assert(len(input) == 8)
        
        key_binary = bin(int.from_bytes(key, "big"))[2:]
        n = 64
        a = int(key_binary[:6], 2)
        init = int(key_binary[6:12], 2)
        cnt = int(key_binary[12:], 2)

        a = a*3//gcd(a, n)
        init = (init + cnt * a) % 64

        left = ""
        right = ""
        input_binary = format(int.from_bytes(input, "big"), '#066b')[2:]
        for _ in range(32):
            left += input_binary[init]
            init = (init + a) % 64
            right += input_binary[init]
            init = (init + a) % 64
        left = int(left, 2).to_bytes(4, "big")
        right = int(right, 2).to_bytes(4, "big")
        return (left, right)
