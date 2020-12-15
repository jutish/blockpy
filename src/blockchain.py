from src.block import Block 
from src.modules.validate import validate

class Blockchain:
	def __init__(self):
		self.blocks = [Block.getGenesis()]

	def addBlock(self,data):
		previousBlock = self.blocks[-1]
		block = Block.mine(previousBlock,data)
		self.blocks.append(block)
		return block

	def replaceBlock(self,newBlocks):
		if len(newBlocks) < len(self.blocks):
			raise Exception('Received chain is not longer than current chain.')
		try:
			validate(newBlocks)
		except Exception as e:
			raise Exception(str(e))
		self.blocks = newBlocks

