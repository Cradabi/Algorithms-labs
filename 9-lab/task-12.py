class KeyValueStore:
    def __init__(self):
        self.data = {}

    def add(self, key, value):
        if key in self.data:
            self.data[key] = self.data[key] + ", " + value
        else:
            self.data[key] = value

    def remove(self, key):
        if key in self.data:
            del self.data[key]

    def search(self, key):
        if key in self.data:
            return self.data[key]
        else:
            return None


def process_operations(operations):
    store = KeyValueStore()

    for operation in operations:
        op_type = operation[0]
        key = operation[1:]

        if op_type == '+':
            key, value = key.split(':')
            store.add(key, value)
        elif op_type == '-':
            store.remove(key)
        elif op_type == '?':
            value = store.search(key)
            if value is not None:
                print(value)
            else:
                print("Key not found")

    print(store.data)


# Пример использования
operations = [
    "+key1:value1",
    "+key2:value2",
    "+key1:value3",
    "?key1",
    "-key2",
    "?key2"
]

n = int(input())
x = []
for i in range(n):
    com = input()
    x.append(com)

process_operations(x)
