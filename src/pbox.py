import secrets

PBOX = [49, 35, 58, 14, 28, 59, 51, 9, 18, 46, 55, 19, 20, 27, 26, 32, 17, 56, 45, 31, 41, 23, 40, 11, 57, 44, 61, 5, 12, 15, 4, 52, 6, 62, 21, 25, 8, 13, 0, 39, 30, 33, 43, 2, 47, 42, 29, 7, 22, 3, 48, 1, 63, 37, 10, 38, 60, 50, 16, 34, 36, 54, 53, 24] 

LEN_PBOX = 64

def transform(input: int):
  temp = []
  for i in range(LEN_PBOX):
    temp.append(str((input >> PBOX[i]) & 1))
  
  res = "".join(temp)
  res = int(res, 2)
  return res
  

if __name__ == "__main__":
    num = secrets.randbits(64)
    print(num)
    print(bin(num))
    temp = transform(num)
    print(temp)
    print(bin(temp))