class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.size = 0

    def __str__(self):
        out_string = ""
        for value in self.values():
            out_string += str(value) + " -> "
        return out_string

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            self.size = 1
            return

        self.tail.next = Node(value)
        self.tail = self.tail.next
        self.size += 1

    def values(self):
        node = self.head
        values = []
        while node:
            values.append(node.value)
            node = node.next

        return values


def union(llist_1, llist_2):
    union_ll = LinkedList()
    res = set(llist_1.values()).union(set(llist_2.values()))
    for i in res:
        union_ll.append(i)

    return union_ll


def intersection(llist_1, llist_2):
    intersection_ll = LinkedList()
    res = set(llist_1.values()).intersection(set(llist_2.values()))
    for i in res:
        intersection_ll.append(i)

    return intersection_ll


# TEST
# Test case 1
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)
for i in element_2:
    linked_list_2.append(i)
print('\nTest 1')
print('Union:\t\t', union(linked_list_1, linked_list_2))
# Union:         32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21 ->
print('Intersection:\t', intersection(linked_list_1, linked_list_2))
# Intersection:  4 -> 21 -> 6 ->

# Test case 2
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()
element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)
for i in element_2:
    linked_list_4.append(i)

print('\nTest 2')
print('Union:\t\t', union(linked_list_3, linked_list_4))
# Union:         65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23 ->
print('Intersection:\t', intersection(linked_list_3, linked_list_4))
# Intersection:


# Test case 3
empty_list = LinkedList()
print('\nTest 3')
print('Union:\t\t', union(empty_list, empty_list))
# Union:
print('Intersection:\t', intersection(empty_list, empty_list))
# Intersection:
