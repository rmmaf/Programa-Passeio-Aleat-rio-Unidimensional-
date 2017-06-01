import matplotlib.pyplot
import random
import math

def mean(numbers):#Funcao para obter a media
	return float(sum(numbers)) / max(len(numbers), 1)

imagem = []#conjunto "imagem" do grafico
x = []#dominio
temp = []#lista de resultados

for index in xrange(2, 240):
	x.append(index)#criacao do dominio
	temp.append([])#adicionando listas nas listas(para fazer com que o "array" seja multidimensional)
	pass
for i in xrange(1, 100001): #configurar repeticoes, neste exemplo o numero de repeticoes eh 100000
	y = 0#variavel para armazenar a POSICAO
	for count in xrange(0, 238):#executando os casos
		y = y + random.sample([-1, 1], 1)[0]
		#funcao para retornar numeros aleatorios: nesse caso ela retorna um elemento, tal que esse elemento é 1 ou -1
		temp[count].append(math.fabs(y))#armazenamento do modulo da posicao(a distancia)
		pass
	pass
for contador in xrange(0, 238):
	imagem.append(mean(temp[contador]))#armazenamento das medias
	pass
matplotlib.pyplot.plot(x, imagem)#funcao para plotar um grafico dado dois vetores de dados
matplotlib.pyplot.show()#funcao para gerar um arquivo png do grafico