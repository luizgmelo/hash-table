class PairKeyValue:
    def __init__(self, key, value):
        self.key = key
        self.value = value
    def __str__(self):
        return f'{self.key}: {self.value}'
    
    def __repr__(self):
        return f'{self.key}: {self.value}'

class HashTable:
    def __init__(self):
        self.__capacity = 5
        self.count = 0
        self.__table = [[] for _ in range(self.__capacity)]

    def hashCode(self, key):
        strKey = str(key)
        return hash(strKey) % self.__capacity

    def __len__(self):
        return self.count

    def __setitem__(self, key, value):
        index = self.hashCode(key)
        new_element = PairKeyValue(key, value)
        for element in self.__table[index]:
            if element.key == key:
                element.value = value
                return
        self.__table[index].append(new_element)
        self.count += 1


phones = HashTable()
phones['Steve'] = '9999-1111'
phones['Maria'] = '9999-2222'
phones['Alex'] = '9999-3333'
phones['Alex'] = '1111-3333'
print()
