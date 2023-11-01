import hashlib

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
        self.__count = 0
        self.__table = [[] for _ in range(self.__capacity)]


    def hashCode(self, key):
        strKey = str(key)
        return int(hashlib.sha256(strKey.encode()).hexdigest(), 16) % self.__capacity

    def __len__(self):
        return self.__count

    def __setitem__(self, key, value):
        index = self.hashCode(key)
        new_element = PairKeyValue(key, value)
        for element in self.__table[index]:
            if element.key == key:
                element.value = value
                return
        self.__table[index].append(new_element)
        self.__count += 1

    def __delitem__(self, key):
        index = self.hashCode(key)
        for element in self.__table[index]:
            if element.key == key:
                self.__table[index].remove(element)
                self.__count -= 1
                return element.value
        
        raise KeyError(f'{key}')

    


phones = HashTable()
phones['Steve'] = '9999-1111'
phones['Maria'] = '9999-2222'
phones['Alex'] = '9999-3333'
phones['Alex'] = '1111-3333'
del phones['Alex']
del phones['Maria']
del phones['Steve']
del phones['Alex']
print()
