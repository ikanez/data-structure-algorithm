import sys


class huff_node(object):
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def is_leaf(self):
        return not (self.left or self.right)


def get_lowest_node(freq_map):
    """
    Get huffman node with lowest frequency.
    Pop the same node from the incoming dictionary.
    """
    # get huffman node with lowest frequency
    min_val = 99  # an arbitrary high number
    min_key = ''
    for i in list(freq_map.keys()):
        if min_val > freq_map[i].freq:
            min_val = freq_map[i].freq
            min_key = i

    node_key = min_key
    node = freq_map[node_key]
    freq_map.pop(node_key)
    return freq_map, node


def build_huff_tree(text):
    """
    Build the Huffman tree.
    Input: Text (string)
    Output: The top huffman node in the tree, which connects to other branches and leaves.
    """
    frequency_map = {}
    text_by_char = list(text)

    # count frequency of each char
    # define a node for each char and store in dictionary
    for char in list(set(text_by_char)):
        frequency_map[char] = huff_node(char, text_by_char.count(char))

    # evaluate each node in dictionary, while popping them as we go
    while len(frequency_map) > 1:

        # isolate 2 of the smallest nodes
        # get node with lowest frequency (left)
        frequency_map, left = get_lowest_node(frequency_map)
        # get node with lowest frequency (right)
        frequency_map, right = get_lowest_node(frequency_map)
        freq_sum = left.freq + right.freq

        # update huffman nodes
        parent_node = huff_node(None, freq_sum)
        parent_node.left = left
        parent_node.right = right
        # giving it a name so that it's easier to troubleshoot later :)
        parent_node.char = left.char + right.char

        # update frequency_map with parent
        frequency_map[parent_node.char] = parent_node

    return frequency_map[list(frequency_map.keys())[0]]


def reduce_tree(tree, code):
    """
    Reduce huffman tree. 
    Input: Huffman tree node.
    Output: Mapping of each char to their encoding.
    """
    huff_map = {}
    if not tree:
        return huff_map
    if tree.is_leaf():
        huff_map[tree.char] = code
    huff_map.update(reduce_tree(tree.left, code + '0'))
    huff_map.update(reduce_tree(tree.right, code + '1'))
    return huff_map


def traverse_tree(encoded, index, tree):
    assert(len(encoded) > 0)

    if tree.is_leaf():  # if we've reached the leaf, we can get the char.
        return tree.char, index

    # if value is 0, then go left, else go right of the tree
    if encoded[index] == '0':
        direction = tree.left
    else:
        direction = tree.right

    return traverse_tree(encoded, index + 1, direction)


def huffman_encoding(text):
    """
    Input: Text (string)
    Output: Encoded data, Huffman tree
    """
    assert(text)
    huff_tree = build_huff_tree(text)
    huff_map = reduce_tree(huff_tree, '')
    encoded = ''.join([huff_map[char] for char in text])
    return encoded, huff_tree


def huffman_decoding(encoded, tree):
    """
    Input: Encoded data, Huffman tree
    Output: Text (string)
    """
    assert(encoded)

    text = ''
    text, next_index = traverse_tree(encoded, 0, tree)
    while next_index < len(encoded):
        next_char, next_index = traverse_tree(encoded, next_index, tree)
        text += next_char
    return text


# test
if __name__ == "__main__":
    codes = {}

    # Test case 1
    print('Test case 1')
    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(
        sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(
        sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(
        sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    # Test case 2
    print('Test case 2')
    a_great_sentence = "The bird is the word. Yet no one writes a letter anymore. A word is no longer needed than a tweet."

    print("The size of the data is: {}\n".format(
        sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(
        sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(
        sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    # Test case 3
    print('Test case 3')
    a_great_sentence = "A car"

    print("The size of the data is: {}\n".format(
        sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(
        sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(
        sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))
