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
# Data: I have a blockchain.
# Time: 21/10/2019 06:07AM
# Hash: 5689ce8e17e1690ad698582789a77b4e74777bd4d24ac3afbb16f74274be4945
# Prev Hash:0

blockchain.add_block("It's stores a lot of data.")
print(blockchain.current_block)
# Data: It's stores a lot of data.
# Time: 21/10/2019 06:07AM
# Hash: e3ad7bbd27e5997b6cae4fe3c6b82081ad4a73f61a02f8f6f8ab4e7f22f888e9
# Prev Hash:5689ce8e17e1690ad698582789a77b4e74777bd4d24ac3afbb16f74274be4945

blockchain.add_block("It's also secure.")
print(blockchain.current_block)
# Data: It's also secure.
# Time: 21/10/2019 06:07AM
# Hash: 60de085298c394de8479abddfb2fd692abee2a1ec2e67221feb85db901d4cffa
# Prev Hash:e3ad7bbd27e5997b6cae4fe3c6b82081ad4a73f61a02f8f6f8ab4e7f22f888e9

blockchain.add_block(None)
print(blockchain.current_block)
# Data: None
# Time: 21/10/2019 06:07AM
# Hash: dc937b59892604f5a86ac96936cd7ff09e25f18ae6b758e8014a24c7fa039e91
# Prev Hash:60de085298c394de8479abddfb2fd692abee2a1ec2e67221feb85db901d4cffa

blockchain.add_block('')
print(blockchain.current_block)
# Data:
# Time: 21/10/2019 06:07AM
# Hash: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
# Prev Hash:dc937b59892604f5a86ac96936cd7ff09e25f18ae6b758e8014a24c7fa039e91
