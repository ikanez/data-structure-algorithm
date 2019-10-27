from collections import deque  # we make use of deque to implement a cache


class LRU_Cache(object):

    def __init__(self, size):
        # Initialize class variables
        self.cache = {}  # dict for holding values
        self.size = size
        self.history = deque([], self.size)
        # For clarity, anytime we append(), a value is inserted to the right of the queue.
        # Thus the oldest (least used) value will be on the left.

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.cache:  # if key is already in cache
            # update history, move key to front of queue
            self.history.remove(key)
            self.history.append(key)
            return self.cache[key]

        # no key exist
        return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if len(self.cache.keys()) == self.size:
            val = self.history.popleft()  # remove least used entry from history/deque
            self.cache.pop(val)  # remove entry from cache

        self.history.append(key)  # add new key to the right of the queue
        self.cache[key] = value  # add new entry in cache


# TEST
our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print(our_cache.get(1))      # returns 1
print(our_cache.get(2))      # returns 2
print(our_cache.get(9))     # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

# returns -1 because the cache reached it's capacity and 3 was the least recently used entry
print(our_cache.get(3))

our_cache.set(7, '')
our_cache.set(8, None)

print(our_cache.get(7))  # returns ''
print(our_cache.get(1))  # returns -1 since already removed
print(our_cache.get(8))  # returns None

our_cache.set(None, None)

print(our_cache.get(None))  # returns None
print(our_cache.cache)  # {5: 5, 6: 6, 7: '', 8: None, None: None}
