# Stores routes and associated handlers
class RouteTrie:
    def __init__(self, root_handler):
        # Initialize the trie with an root node and a handler
        # This is the root path or home page node
        self.root = RouteTrieNode(root_handler)

    def insert(self, path, handler):
        # Recursively add nodes.
        node = self.root
        i = 0
        while i < len(path):
            elem = path[i]
            node = node.insert(elem)
            i += 1
        node.handler = handler

    def find(self, path):
        # Navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        node = self.root
        i = 0
        while i < len(path):
            elem = path[i]
            if elem in node.children.keys():
                node = node.children[elem]
                i += 1
            else:
                return None
        return node.handler


# Represents a single node in the Trie
class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize this node in the Trie
        self.children = {}
        self.handler = handler

    def insert(self, elem):
        # Add a child node in this Trie
        if elem not in self.children.keys():
            child = RouteTrieNode()
            self.children[elem] = child
            return child
        return self.children[elem]


# The Router class will wrap the Trie and handler
class Router:
    def __init__(self, root_handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.trie = RouteTrie(root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        self.trie.insert(self.split_path(path), handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler

        if not path:  # if path is not a string
            return self.not_found_handler

        result = self.trie.find(self.split_path(path))
        if not result:
            return self.not_found_handler
        return result

    def split_path(self, path):
        # you need to split the path into parts for
        # both the add_handler and lookup functions,
        # so it should be placed in a function here
        stripped_path = path.strip("/")
        if stripped_path:
            print(stripped_path.split("/"))
            return stripped_path.split("/")
        return []


"""
-------------------
TEST
-------------------
"""

# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router(
    "root handler", "not found handler"
)  # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
print(
    router.lookup("/home")
)  # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about"))  # should print 'about handler'
print(
    router.lookup("/home/about/")
)  # should print 'about handler' or None if you did not handle trailing slashes
print(
    router.lookup("/home/about/me")
)  # should print 'not found handler' or None if you did not implement one

# edge cases
print(router.lookup(""))  # should print 'root handler'
print(
    router.lookup(None)
)  # should print 'not found handler' or None if you did not implement one
