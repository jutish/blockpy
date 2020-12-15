from src.block import Block

def validate(blockchain):
	genesisBlock =  blockchain[0] #Genesis
	blocks = blockchain[1:] #Resto de los bloques
	if str(genesisBlock)!=str(Block.getGenesis()): #El genesis de blockchain debe ser igual al de Block.getGenesis() ya que es una variable de clase.
		raise Exception('Invalid Genesis Block')
	for i, bl in enumerate(blocks):
		previousHash = bl.previousHash
		timestamp = bl.timestamp
		hash = bl.hash
		data = bl.data
		previousBlock = blockchain[i]
		#El bloque actual debe apuntar al Hash del bloque anterior.
		if previousHash!=previousBlock.hash:
			raise Exception('Invalid previous hash')
		#El hash del bloque actual debe ser correcto. Para eso comparo el hash del bloque actual con el devuelto por la funcion Hash en base a los datos del bloque.
		if hash!=Block.getHash(timestamp,previousHash,data):
			raise Exception('Invalid hash')

	return True


