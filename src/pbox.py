PBOX = [14, 28, 9, 18, 19, 20, 27, 26, 17, 31, 23, 11, 5, 12, 15, 4, 6, 21, 25, 8, 13, 0, 30, 2, 29, 7, 22, 3, 1, 10, 16, 24]
LEN_PBOX = 32

def permute(input: bytes) -> bytes:
  assert(len(input) == 4) # 8 bytes
  
  temp = []
  num = int.from_bytes(input, "big")

  for i in range(LEN_PBOX):
    temp.append(str((num >> PBOX[i]) & 1))
  
  res = "".join(temp)
  res = int(res, 2).to_bytes(LEN_PBOX // 8, "big")
  
  assert(len(res) == 4)
  
  return res
