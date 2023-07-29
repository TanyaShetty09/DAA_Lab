import heapq

class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ''

    def __lt__(self, nxt):
        return self.freq < nxt.freq

def printNodes(node, val=''):
    newVal = val + str(node.huff)
    if node.left:
        printNodes(node.left, newVal)
    if node.right:
        printNodes(node.right, newVal)
    if not node.left and not node.right:
        print(f"{node.symbol} -> {newVal}")

def build_huffman_tree(chars, freq):
    nodes = []
    for x in range(len(chars)):
        heapq.heappush(nodes, Node(freq[x], chars[x]))

    while len(nodes) > 1:
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)
        left.huff = '0'
        right.huff = '1'
        new_node = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
        heapq.heappush(nodes, new_node)

    return nodes[0]

def encode_text(text, huffman_tree):
    encoding_map = {}

    def traverse_tree(node, code=''):
        if node.left:
            traverse_tree(node.left, code + '0')
        if node.right:
            traverse_tree(node.right, code + '1')
        if not node.left and not node.right:
            encoding_map[node.symbol] = code

    traverse_tree(huffman_tree)

    encoded_text = ''
    for char in text:
        encoded_text += encoding_map[char]

    return encoded_text

def decode_text(encoded_text, huffman_tree):
    decoded_text = ''
    current_node = huffman_tree

    for bit in encoded_text:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right

        if not current_node.left and not current_node.right:
            decoded_text += current_node.symbol
            current_node = huffman_tree

    return decoded_text

# User input
text = input("Enter the English text to encode: ")

chars = []
freq = []

n = int(input("Enter the number of characters: "))
for i in range(n):
    char = input("Enter character: ")
    chars.append(char)
    f = int(input("Enter frequency: "))
    freq.append(f)

huffman_tree = build_huffman_tree(chars, freq)
print("Huffman Codes:")
printNodes(huffman_tree)

encoded_text = encode_text(text, huffman_tree)
print("Encoded text:", encoded_text)

decoded_text = decode_text(encoded_text, huffman_tree)
print("Decoded text:", decoded_text)

# Binary decoding
binary_input = input("Enter binary digits to decode (without spaces): ")
decoded_binary_text = decode_text(binary_input, huffman_tree)
print("Decoded binary text:", decoded_binary_text)