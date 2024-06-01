class HashTable:
    def __init__(self, size):
        self.alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        self.table_size = size
        self.table = [None] * size
        self.keys = [None] * size

    def __value_of_key(self, key):
        if len(key) < 2:
            raise ValueError("Ключ должен быть длинной больше 2 символов.")
        if not (key[0].upper() in self.alphabet and key[1].upper() in self.alphabet):
            raise ValueError("Первые два символа ключа должны быть буквы русского алфавита")
        base = len(self.alphabet)
        v = self.alphabet.index(key[0].upper()) * base + self.alphabet.index(key[1].upper())
        return v

    def __hash(self, key):
        return self.__value_of_key(key) % self.table_size

    def __quadratic_probing(self, hash_value, step):
        return (hash_value + step ** 2) % self.table_size

    def insert(self, key, value):
        hash_index = self.__hash(key)
        step = 0
        while self.table[hash_index] is not None:
            if self.keys[hash_index] == key:  # Update case
                self.table[hash_index] = value
                return
            step += 1
            hash_index = self.__quadratic_probing(hash_index, step)
        self.table[hash_index] = value
        self.keys[hash_index] = key

    def search(self, key):
        hash_index = self.__hash(key)
        step = 0
        while self.table[hash_index] is not None:
            if self.keys[hash_index] == key:
                return self.table[hash_index]
            step += 1
            hash_index = self.__quadratic_probing(hash_index, step)
        return None

    def delete(self, key):
        hash_index = self.__hash(key)
        step = 0
        while self.table[hash_index] is not None:
            if self.keys[hash_index] == key:
                self.table[hash_index] = None
                self.keys[hash_index] = None
                return
            step += 1
            hash_index = self.__quadratic_probing(hash_index, step)
        raise KeyError("Нет такого ключа.")

    def update(self, key, value):
        hash_index = self.__hash(key)
        step = 0
        while self.table[hash_index] is not None:
            if self.keys[hash_index] == key:
                self.table[hash_index] = value
                return
            step += 1
            hash_index = self.__quadratic_probing(hash_index, step)
        raise KeyError("Нет такого ключа.")


# Debug or hand-usage mode
#
# table = HashTable(10)
# table.insert("Дима", "Плотник")
# table.insert("ДимаКоллизия", "Актер")
# table.insert("Рома", "Слесарь")
#
# print(table.search("Дима"))
# print(table.search("ДимаКоллизия"))
# print(table.search("Рома"))
#
# table.update("Дима", "Программист")
# print(table.search("Дима"))
#
# table.delete("Рома")
# print(table.search("Рома"))

