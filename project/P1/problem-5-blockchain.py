import hashlib
import time


class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = time.strftime('%d/%m/%Y %H:%M%p', timestamp)
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = str(self.data).encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def __str__(self):
        string = 'Data: ' + str(self.data) + '\n'
        string += 'Time: ' + str(self.timestamp) + '\n'
        string += 'Hash: ' + str(self.hash) + '\n'
        string += 'Prev Hash:' + str(self.previous_hash) + '\n'
        return string


class Blockchain:
    def __init__(self):
        self.current_block = None

    def add_block(self, value):
        timestamp = time.gmtime()
        data = value
        previous_hash = self.current_block.hash if self.current_block else 0
        self.current_block = Block(timestamp, data, previous_hash)


# test
blockchain = Blockchain()

blockchain.add_block('I have a blockchain.')
print(blockchain.current_block)

blockchain.add_block("It's stores a lot of data.")
print(blockchain.current_block)

blockchain.add_block("It's also secure.")
print(blockchain.current_block)
