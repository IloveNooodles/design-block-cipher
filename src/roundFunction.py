from pwn import xor

class RoundFunction:
    def get_f(self) -> callable([bytes, bytes], bytes):
        return self._f

    def _f(input: bytes, round_key: bytes) -> bytes:
        temp = slice_box(input, round_key)
        return b"".join(temp)
    
    def _slice_box(input: bytes, key: bytes) -> [bytes, bytes]:
        assert(len(key) == 2)
        assert(len(input) == 8)
        return [input[:1], input[1:]]