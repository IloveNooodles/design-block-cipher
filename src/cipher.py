class Cipher:
    __size = 128//8

    def __init__(self, key: bytes):
        assert(len(key)==self.__size)
        pass

    def encrypt(self, data: bytes):
        assert(len(data)%self.__size == 0)
        return data[::-1]

    def decrypt(self, data: bytes):
        assert(len(data)%self.__size == 0)
        return data[::-1]