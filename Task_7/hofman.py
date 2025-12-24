import heapq
from collections import defaultdict

class HuffmanNode:
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq

class HuffmanTree:
    def __init__(self, text):
        self.text = text
        self.root = None
        self.codes = {}
        self.reverse_mapping = {}

    def build_tree(self):
        frequency = defaultdict(int)
        for char in self.text:
            frequency[char] += 1

        priority_queue = []
        for char, freq in frequency.items():
            heapq.heappush(priority_queue, HuffmanNode(char, freq))

        while len(priority_queue) > 1:
            left = heapq.heappop(priority_queue)
            right = heapq.heappop(priority_queue)
            merged = HuffmanNode(None, left.freq + right.freq, left, right)
            heapq.heappush(priority_queue, merged)

        self.root = priority_queue[0]
        self._generate_codes(self.root, "")

    def _generate_codes(self, node, current_code):
        if node is None:
            return

        if node.char is not None:
            self.codes[node.char] = current_code
            self.reverse_mapping[current_code] = node.char
            return

        self._generate_codes(node.left, current_code + "0")
        self._generate_codes(node.right, current_code + "1")

    def encode(self):
        encoded_text = ''.join(self.codes[char] for char in self.text)
        return encoded_text

    def decode(self, encoded_text):
        current_code = ""
        decoded_text = ""

        for bit in encoded_text:
            current_code += bit
            if current_code in self.reverse_mapping:
                decoded_text += self.reverse_mapping[current_code]
                current_code = ""

        return decoded_text
