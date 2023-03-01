class Cipher:
    __key_size = 128//8
    __block_size = 128//8

    def __init__(self, key: bytes):
        assert(len(key)==self.__key_size)
        pass

    def encrypt(self, data: bytes):
        assert(len(data) == self.__block_size)
        return data[::-1]

    def decrypt(self, data: bytes):
        assert(len(data) == self.__block_size)
        return data[::-1]