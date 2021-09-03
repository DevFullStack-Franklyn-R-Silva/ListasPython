class Celula:
	item = None
	proximo = None

	def __init__(self,item):
		self.item = item

class Lista_Encadeada:
	inicio = None
	tamanho = 0

	def __init__(self):
		self.inicio = Celula(None)

	#verificar se tá vazia
	def estaVazia(self):
		return self.tamanho == 0

	#inserir
	def inserir(self,item,*pos):
		pos = pos if pos != () else self.tamanho
		if pos <= self.tamanho:
			p = self.inicio
			for i in range(pos):
				p = p.proximo
			aux = Celula(item)
			aux.proximo = p.proximo
			p.proximo = aux
			self.tamanho+=1
		else:
			print('operacao invalida')
	
	#remover
	def remover(self,pos):
		if not self.estaVazia() and pos<self.tamanho:
			p = self.inicio
			for i in range(pos):
				p = p.proximo
			aux = p.proximo
			p.proximo = aux.proximo
			item = aux.item
			del aux
			self.tamanho -=1
			return item
		else:
			print('operacao invalida')

	#imprimir
	def imprimir(self):
		p = self.inicio
		for i in range(self.tamanho):
			p = p.proximo
			print(p.item)
		print('---')

	#buscar
	def buscar(self,item):
		p = self.inicio
		for i in range(self.tamanho):
			p = p.proximo
			if p.item == item:
				return i
		return None

lista = Lista_Encadeada()
lista.inserir('a')
lista.inserir('b')
lista.inserir('c')
lista.inserir('d')
lista.imprimir()
print(lista.buscar('w'))
# lista.inserir('w',2)
# lista.imprimir()
# lista.remover(2)
# lista.remover(2)
# lista.remover(2)
# lista.remover(1)
# lista.remover(0)
# lista.imprimir()
# lista.inserir('a',0)
# lista.imprimir()






























# class Celula:
# 	item = None
# 	proximo = None

# 	def __init__(self,item):
# 		self.item = item

# class Lista_Encadeada:
# 	inicio = None
# 	tamanho = 0

# 	def __init__(self):
# 		self.inicio = Celula(None)		

# 	def estaVazia(self):
# 		return self.tamanho == 0

# 	def inserir(self,item,pos):
# 		if pos<=self.tamanho:
# 			p = self.inicio
# 			#encontrar a celula anterior a pos
# 			for i in range(pos):
# 				p = p.proximo
# 			aux = Celula(item)
# 			aux.proximo = p.proximo
# 			p.proximo = aux
# 			self.tamanho +=1

# 	def remover(self,pos):
# 		if not self.estaVazia() and pos < self.tamanho:
# 			p = self.inicio
# 			for i in range(pos):
# 				p = p.proximo
# 			aux = p.proximo
# 			p.proximo = aux.proximo
# 			item = aux.item
# 			del aux
# 			self.tamanho -=1
# 			return item
# 		else:
# 			print('operacao invalida')
			
		

# 	def imprimir(self):
# 		p = self.inicio.proximo
# 		while p!= None:
# 			print(p.item)
# 			p = p.proximo
# 		print('---')

		

# 	# def buscar(self,item):
# 		#retornar posicao do item se ele existir

# 	# def removerI(self,item):
# 		#remover o item se ele existir

# lista = Lista_Encadeada()
# lista.inserir('a',0)
# lista.inserir('b',1)
# lista.inserir('c',2)
# lista.inserir('d',3)
# lista.inserir('e',4)
# lista.imprimir()
# lista.inserir('h',2)
# lista.imprimir()
# lista.remover(5)
# lista.remover(4)
# lista.remover(3)
# lista.remover(2)
# lista.remover(1)
# lista.remover(0)
# lista.imprimir()
# lista.inserir('h',0)
# lista.imprimir()
