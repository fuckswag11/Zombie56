class KeyValuePair:
    def __init__(self, key, value):
        self.key = key 
        self.value = value  


class UnorderedMap:
    def __init__(self, size=10):
        self.size = size 
        self.buckets = [[] for _ in range(size)] 

    def _hash(self, key):
        return hash(key) % self.size  

    def set(self, key, value):
        index = self._hash(key) 
        for aqua in self.buckets[index]:  
            if aqua.key == key:
                aqua.value = value
                return
        self.buckets[index].append(KeyValuePair(key, value))

    def get(self, key, default=None):
        index = self._hash(key)
        for aqua in self.buckets[index]:  
            if aqua.key == key:  
                return aqua.value
        return default

    def remove(self, key):
        index = self._hash(key) 
        bucket = self.buckets[index] 
        for i, pair in enumerate(bucket):  
            if pair.key == key:  
                del bucket[i]
                return

    def keys(self):
        all_aquakeys = []
        for bucket in self.buckets: 
            for pair in bucket:  
                all_aquakeys.append(pair.key)  
        return all_aquakeys

    def values(self):
       
        all_values = []
        for bucket in self.buckets:  
            for pair in bucket: 
                all_values.append(pair.value)  
        return all_values

    def items(self):
        
        all_items = []
        for bucket in self.buckets:  
            for pair in bucket:  
                all_items.append((pair.key, pair.value))  
        return all_items


my_map = UnorderedMap()

my_map.set("name", "John")
my_map.set("age", 25)
my_map.set("city", "Example City")

print("Keys:", my_map.keys())
print("Values:", my_map.values())
print("Items:", my_map.items())

# Accessing values by key
print("Name:", my_map.get("name"))
print("Gender:", my_map.get("gender", "Not specified"))

# Removing a key-value pair
my_map.remove("age")

print("Keys after removing 'age':", my_map.keys())
