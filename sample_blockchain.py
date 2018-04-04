import hashlib as hash
import datetime as date


class Block:

    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.current_hash = self.hash_block

    def hash_block(self):
        sha = hash.sha256()
        sha.update = (str(self.index) +
                      str(self.timestamp) +
                      str(self.data) +
                      str(self.previous_hash).encode('utf-8'))
        return sha.hexadigest()


def create_genesis_block():
    return Block(0, date.datetime.now(), "Genesis Block", "0")


def next_block(last_block):
    this_index = last_block.index + 1
    print(this_index)
    this_timestamp = date.datetime.now()
    this_data = "Block" + str(this_index)
    print(this_data)
    this_hash = last_block.current_hash
    return Block(this_index, this_timestamp, this_data, this_hash)


blockC = [create_genesis_block()]
previous_block = blockC[0]
add_to_block = next_block(previous_block)

number_of_blocks = 10

for i in range(0, number_of_blocks):
    add_to_block = next_block(previous_block)
    blockC.append(add_to_block)
    previous_block = add_to_block
    print("Block #{} has been added ".format(add_to_block.index))
    print("Blocks: {}\n".format(add_to_block.current_hash))
