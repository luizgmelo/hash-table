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

        self.__expand_percentage = 0.75
        self.__reduce_percentage = 0.20

    @property
    def capacity_percentage_used(self):
        return self.__count / self.__capacity

    def hashCode(self, key):
        strKey = str(key)
        return int(hashlib.sha256(strKey.encode()).hexdigest(), 16) % self.__capacity

    def __len__(self):
        return self.__count

    def __setitem__(self, key, value):
        if self.capacity_percentage_used > self.__expand_percentage:
            new_capacity = self.__capacity * 2
            self.update(new_capacity)
        
        index = self.hashCode(key)
        new_element = PairKeyValue(key, value)
        for element in self.__table[index]:
            if element.key == key:
                element.value = value
                return
        self.__table[index].append(new_element)
        self.__count += 1

    def __delitem__(self, key):
        if self.capacity_percentage_used < self.__reduce_percentage:
            new_capacity = self.__capacity // 2
            self.update(new_capacity)
        
        index = self.hashCode(key)
        for element in self.__table[index]:
            if element.key == key:
                self.__table[index].remove(element)
                self.__count -= 1
                return element.value
        
        raise KeyError(f'{key}')

    def update(self, new_capacity):
        old_table = self.__table
        self.__count = 0
        self.__capacity = new_capacity
        self.__table = [[] for _ in range(new_capacity)]
        for list in old_table:
            for element in list:
                self.__setitem__(element.key, element.value)

    def __getitem__(self, key):
        index = self.hashCode(key)
        for element in self.__table[index]:
            if element.key == key:
                return element.value
        raise KeyError(f'{key}')

    def __str__(self):
        objString = "{"
        for list in self.__table:
            if len(list) > 0:
                for element in list:
                    objString += f"'{element.key}': '{element.value}', "
            
        return objString[:-2] + objString[-2].replace(',', '}')
            
    def __iter__(self):
        for list in self.__table:
            if len(list) > 0:
                for element in list:
                    yield element.key, element.value


phones = HashTable()
phones['Steve'] = '9999-1111'
phones['Maria'] = '9999-2222'
phones['Alex'] = '9999-3333'
phones['Alex'] = '1111-3333'
phones['Ronaldo'] = '9999-5555'
phones['Gabriel'] = '9999-4444'

print(phones['Steve'])
print(phones['Alex'])
print(phones['Ronaldo'])

print(phones)

for name, phone in phones:
    print(name, phone)