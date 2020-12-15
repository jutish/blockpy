from django.shortcuts import render,HttpResponse
from bch1.blockchain import Blockchain
import json


blockchain = Blockchain()
blockchain.addBlock('Bloque1')

# Create your views here.
def index(request):
	res = []
	for block in blockchain.blocks:
	    res.append({
			"Timestamp"		:	str(block.timestamp),
			"PreviousHash" 	:	str(block.previousHash),
			"Hash" 			:	str(block.hash),
			"Data" 			: 	str(block.data)
			})	
	return HttpResponse(json.dumps(res),content_type="application/json")

# Minado de un bloque
def mine(request,data):
	block = blockchain.addBlock(data)
	jsonBlock = {
		"Timestamp"		:	str(block.timestamp),
		"PreviousHash" 	:	str(block.previousHash),
		"Hash" 			:	str(block.hash),
		"Data" 			: 	str(block.data)
	}
	res = {
			"length": len(blockchain.blocks),
			"block": jsonBlock
	}
	return HttpResponse(json.dumps(res),content_type="application/json")

		