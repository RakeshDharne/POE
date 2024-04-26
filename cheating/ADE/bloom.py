class BloomFilter:
    def __init__(self, filter_size):
        self.filter_size = filter_size
        self.bit_set = [False] * filter_size

    def add(self, key):
        hash1 = self.hash_function1(key)
        hash2 = self.hash_function2(key)
        hash3 = self.hash_function3(key)
        self.bit_set[hash1] = True
        self.bit_set[hash2] = True
        self.bit_set[hash3] = True

    def contains(self, key):
        hash1 = self.hash_function1(key)
        hash2 = self.hash_function2(key)
        hash3 = self.hash_function3(key)
        return self.bit_set[hash1] and self.bit_set[hash2] and self.bit_set[hash3]

    def hash_function1(self, key):
        x = int(key)
        return (3 * x + 1) % self.filter_size

    def hash_function2(self, key):
        x = int(key)
        return (3 * x + 5) % self.filter_size

    def hash_function3(self, key):
        x = int(key)
        return (3 * x + 7) % self.filter_size


def bloom_join(relation1, relation2):
    # Create Bloom filter for relation 2
    bloom_filter = BloomFilter(100)
    for row in relation2:
        key = row.split(",")[0]
        bloom_filter.add(key)

    # Perform join
    result = []
    for row in relation1:
        key = row.split(",")[0]
        if bloom_filter.contains(key):
            result.append(row)

    # Print bit set
    print("Bit Set:", bloom_filter.bit_set)

    return result


# Sample relations (tables)
relation1 = [
    "1, Pranay",
    "2, Anshul",
    "3, Ritesh",
    "4, Yash",
    "5, Siddharth"
]

relation2 = [
    "1, Amazon",
    "2, Microsoft",
    "4, Adobe",
    "6, TCS",
    "7, Netflix"
]

# Perform Bloom join
result = bloom_join(relation1, relation2)
s
# Print result
print("Result:")
for row in result:
    print(row)
