import datetime
import hashlib

class Block:
	def __init__(self,timestamp,previousHash,hash,data):
		self.timestamp = timestamp
		self.previousHash = previousHash
		self.hash = hash
		self.data = data
	
	def __str__(self):
		res = f""" 
			Block - 
			Timestamp		:	{self.timestamp}
			PreviousHash 	:	{self.previousHash}
			Hash 			:	{self.hash}
			Data 			: 	{self.data}
		"""
		return res

	@staticmethod	
	def getGenesis():
		timestamp = datetime.datetime.now()
		gen = Block(timestamp,None,'_g3n3s1s-h4sh','Data Bloque Genesis')
		return gen

	@staticmethod
	def mine(previousBlock,data):
		timestamp = datetime.datetime.now()
		previousHash = previousBlock.hash
		hash = Block.getHash(timestamp,previousHash,data)
		obj = Block(timestamp,previousHash,hash,data)
		return obj

	@staticmethod	
	def getHash(timestamp,previousHash,data):
		return hashlib.sha256(f"{timestamp}{previousHash}{data}".encode('utf8')).hexdigest()



