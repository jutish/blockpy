from src.block import Block
from src.blockchain import Blockchain


# genesis = Block.getGenesis()
# bloque1 = Block.mine(genesis,'D4t4-Bloqu3_1')
# bloque2 = Block.mine(bloque1,'D4t4-Bloqu3_2')
# print(bloque1)
# print(bloque2)

print("Test 1 -Every blockchain has a Genesis Block")
blockchain = Blockchain()
genesis = blockchain.blocks[0]
print(genesis)

print("Test 2 - use addBlock")
blockchain = Blockchain()
data = 'd4t4-blk1'
blockchain.addBlock(data)
lastBlock = blockchain.blocks[-1]
print(lastBlock.data == data)
print(len(blockchain.blocks)==2)

print("Test 3 - replaces the chain with a valid chain")
blockchain = Blockchain()
blockchainb =  Blockchain()
data = 'd4t4-blk1'
blockchainb.addBlock(data)
blockchain.replaceBlock(blockchainb.blocks)
print(blockchain.blocks==blockchainb.blocks)

print("Test 4 - Does not replace with one with less blocks")
blockchain = Blockchain()
blockchainb =  Blockchain()
data = 'd4t4-blk1'
blockchain.addBlock(data)
try:
	blockchain.replaceBlock(blockchainb.blocks)
except Exception as e:
	print(str(e)=='Received chain is not longer than current chain.')

print("Test 5 - Not replace the chain with a not valid block")
blockchain = Blockchain()
blockchainb =  Blockchain()
data = 'd4t4-blk1'
blockchainb.addBlock(data)
lastBlock = blockchainb.blocks[-1]
lastBlock.data = 'hack-data'
try:
	blockchain.replaceBlock(blockchainb.blocks)
except Exception as e:
	print(str(e)=='Invalid hash')


