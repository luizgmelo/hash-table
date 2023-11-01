class PairKeyValue:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:
    def __init__(self):
        self.__capacity = 5
        self.__table = [[] for _ in range(self.__capacity)]

    def hashCode(self, key):
        strKey = str(key)
        return hash(strKey) % self.__capacity

    def __setitem__(self, key, value):
        index = self.hashCode(key)
        self.__table[index].append(PairKeyValue(key, value))
        


my_hash = HashTable()
my_hash['nome'] = 'Luiz'



