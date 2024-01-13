import heapq

class HuffmanNode:
    def _init_(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def _lt_(self, other):
        return self.freq < other.freq

def build_huffman_tree(freq_dict):
    priority_queue = [HuffmanNode(char, freq) for char, freq in freq_dict.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)

        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(priority_queue, merged)

    return priority_queue[0]

def print_huffman_codes(node, code=""):
    if node:
        if node.char is not None:
            print(f"{node.char}: {code}")
        print_huffman_codes(node.left, code + "0")
        print_huffman_codes(node.right, code + "1")

# Example usage:
# Frequencies of characters in a string
text = "hello, world!"
freq_dict = {}
for char in text:
    if char in freq_dict:
        freq_dict[char] += 1
    else:
        freq_dict[char] = 1

huffman_tree = build_huffman_tree(freq_dict)
print_huffman_codes(huffman_tree)