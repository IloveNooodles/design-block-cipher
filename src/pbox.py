from secrets import randbits

PBOX = [49, 35, 58, 14, 28, 59, 51, 9, 18, 46, 55, 19, 20, 27, 26, 32, 17, 56, 45, 31, 41, 23, 40, 11, 57, 44, 61, 5, 12, 15, 4, 52, 6, 62, 21, 25, 8, 13, 0, 39, 30, 33, 43, 2, 47, 42, 29, 7, 22, 3, 48, 1, 63, 37, 10, 38, 60, 50, 16, 34, 36, 54, 53, 24] 

LEN_PBOX = 64

def permute(input: bytes) -> bytes:
  assert(len(input) == 8) # 8 bytes
  
  temp = []
  num = int.from_bytes(input, "big")

  for i in range(LEN_PBOX):
    temp.append(str((num >> PBOX[i]) & 1))
  
  res = "".join(temp)
  res = int(res, 2).to_bytes(LEN_PBOX // 8, "big")
  
  assert(len(res) == 8)
  
  return res
  

if __name__ == "__main__":
    num = randbits(64)
    
    print("NUM: ", num)
    print("BIN: ", bin(num))
    
    temp = permute(num.to_bytes(LEN_PBOX // 8, "big"))
    temp_int = int.from_bytes(temp, "big")
    
    print("NUM: ", temp_int)
    print("BIN: ", bin(temp_int))