'''Linked List hash table key/value pair'''


class LinkedPair:
    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next

    def __repr__(self):
        return f"{{{self.key}, {self.value}}}, next {self.next}"


class HashTable:
    '''A hash table that with `capacity` buckets that accepts string keys'''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.size = 0

    def _hash(self, key):
        ''' Hash an arbitrary key and return an integer. You may replace the Python hash with DJB2 as a stretch goal. '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash
        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        ''' Take an arbitrary key and return a valid integer index within the storage capacity of the hash  table. '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key. Hash collisions should be handled with Linked List Chaining.
        '''
        self.size += 1
        index = self._hash_mod(key)
        if self.storage[index] is None:
            # found the item
            # print(f"\nfree real estate, new pair")
            self.storage[index] = LinkedPair(key, value)
        else:
            # print(f'\nwe have a collision')
            # if the head of the LL matches the key, overwrite it
            if self.storage[index].key == key:
                # print(f'overwriting head with {value}')
                self.storage[index].value = value
            else:
                # otherwise traverse the LL
                current = self.storage[index]
                while current.next is not None:
                    current = current.next
                    if current.key == key:
                        current.value = value
                        return
                # if not found, insert at the end
                current.next = LinkedPair(key, value)

            # already existing, add it to the beginning
            # old = self.storage[index]
            # self.storage[index] = LinkedPair(key, value)
            # self.storage[index].next = old

    def remove(self, key):
        '''Remove the value stored with the given key. Print a warning if the key is not found.'''
        pair = self.storage[self._hash_mod(key)]
        if pair is None:
            print("ERROR: Key not found")
        # if the pair found is the only node in the bucket
        elif pair.key == key and pair.next is None:
            self.storage[self._hash_mod(key)] = None
            self.size -= 1
        # if the pair found is also the head of a linked list
        elif pair.key == key and pair.next is not None:
            # remove the head, and make next the head
            self.storage[self._hash_mod(pair.next.key)] = pair.next
            self.size -= 1
        # if there was a collision and pair is head of a linked list
        elif pair.key != key and pair.next is not None:
            prev = pair
            current = pair.next
            while current is not None:
                if current.key == key:
                    # remove current from linked list
                    prev.next = current.next
                    current = None
                    self.size -= 1
                    return
                prev = current
                current = current.next
            # if you don't find it in the collisions, error
            print("ERROR: Key not found")

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key. Returns None if the key is not found.
        '''
        pair = self.storage[self._hash_mod(key)]
        if pair is None:
            return None
        elif pair.key == key:
            return pair.value
        else:
            while pair.next:
                pair = pair.next
                if pair.key == key:
                    return pair.value
            return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and rehash all key/value pairs.
        '''
        old_storage = self.storage.copy()
        self.capacity *= 2
        # you want to be able to use insert, so you assign the old_storage first
        self.storage = [None] * self.capacity
        for pair in old_storage:
            if pair is not None:
                self.insert(pair.key, pair.value)
                # if the pair is also a Linked List, traverse down there and add onto it
                if pair.next is not None:
                    current = pair.next
                    while current is not None:
                        self.insert(current.key, current.value)
                        current = current.next


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
