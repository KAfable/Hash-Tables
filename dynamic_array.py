class dynamic_array:
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        self.storage = [None] * self.capacity

    def insert(self, index, value):
        if self.count >= self.capacity:
            self.double_size()

        if index > self.count:
            print("ERROR: Index out of range")
            return

        for i in range(self.count, index, -1):
            self.storage[i] = self.storage[i-1]

        self.storage[index] = value
        self.count += 1

    def append(self, value):
        self.insert(self.count, value)

    def double_size(self):
        self.capacity *= 2
        new_storage = [None] * self.capacity
        for i in range(self.count):
            new_storage[i] = self.storage[i]
        self.storage = new_storage


my_array = dynamic_array(4)
my_array.insert(0, 'a')
my_array.insert(1, 'b')
my_array.insert(2, 'c')
my_array.insert(3, 'd')
my_array.insert(4, 'e')
print(my_array.storage)
print(my_array)
