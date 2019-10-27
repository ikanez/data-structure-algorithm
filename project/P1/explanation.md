# Introduction
The following summarizes the analysis for each of the task assigned.


## Problem 1 (LRU Cache)
### Approach
- Used deque to store the cache. This helps to keep the overall code simple and maintain the order of insertion and removal of oldest entry.
### Efficiency
- The time complexity of get() is O(1), since there are no loops (constant time)
- The time complexity of set() is O(1), since there are no loops (constant time)
- Reordering of deque might incur O(n) complexity 
- The space complexity of O(k) where k is the size of the cache


## Problem 2 (Recursion)
### Approach
- Recursively check dir listing and see whether child is dir or file. If dir then apply check again into the dir. Else evaluate whether suffix criteria is met.
- Any filename match is appended to list.
### Efficiency
- All dir/files will need to be checked once. Hence, O(n)
- The space complexity of the O(1) since only values that is being processed is being stored


## Problem 3 (Huffman Encoding)
### Approach
- Used a dictionary to initially store a mapping of char with each Huffman node.
- Reduce code tree by traversing the huffman tree from the top and working way down to the bottom and retrieving each char.
- Join encoded bits to form encoded data
- Decoding data is done by traversing through each bits in encoded data, based on the direction of the huffman tree.
### Efficiency
- huff_node has a space complexity of O(k) where k is the number of unique char in the string. 
#### get_lowest_node()
- Finding the node with lowest frequency is O(n)
- Removing node with lowest frequency is O(1)
- Space complexity of O(k), where k is the number of variable in the function.
#### build_huff_tree()
- Counting frequency of char and storing it to a dictionary is O(n)
- Evaluating the nodes and building the tree is O(2n) (which can also be considered as O(n))
- Space complexity of O(n) for building the huffman tree. 
#### reduce_tree()
- Traversing the tree takes O(n)
- Space complexity is also O(n)
#### traverse_tree()
- Traversing the tree takes O(n)
- Space complexity is also O(n)
#### huffman_encoding()
- O(n^2) as we evaluate each node in the dictionary and run get_lowest_node() each time.
#### huffman_decoding()
- O(2n), since we use traverse_tree() twice


## Problem 4 (Active Directory)
### Approach
- Uses recursion to keep exploring child branch
### Efficiency
- If user already in group, O(1). If not, O(n), where n is the number of group
- Space complexity is neglible since we're recursively evaluating branch.


## Problem 5 (Blockchain)
### Approach
- Linked list.
### Efficiency
- O(1) for each block added.
- O(n) where n is size of the blockchain.

## Problem 6 (Union & Intersect)
### Approach
- Double linked list. Uses set() to get union and intersect. Assumes that there are no duplicate in input entries, and the order of output does not matter.
### Efficiency
- Intersect has complexity of O(n), where n is the length of the smallest input.
- Union has complexity of O(2n), if we assume that both input have the same size
- Space complexity of O(k+m), where k and m are size of 1st and 2nd input respectively