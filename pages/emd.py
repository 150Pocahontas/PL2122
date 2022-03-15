import re
import time

from createHTML import createHTML

#Função auxiliar para ordenar um dicionário consoante as suas Keys
def sortedByKey(resultadosCategorias):
    dicionarioOrdenado = {k:v for k,v in sorted(resultadosCategorias.items())}
    return dicionarioOrdenado

#Função auxiliar que adiciona ao Dicionário cada elemento ocorrido na categoria certa
def adicionaElemento(categoria,indiceLinha,elemento,resultadosCategorias):
    resultadosCategorias[categoria]['nrElementos'] += 1
    if elemento not in resultadosCategorias[categoria]['elementos']:
        resultadosCategorias[categoria]['elementos'][elemento] = [indiceLinha]
    else:
        resultadosCategorias[categoria]['elementos'][elemento].append(indiceLinha)

#Usados para construção do Dicionário
nrLinha = 1
resultadosCategorias = {}

    #"Idade" : 0,
    #"Modalidade" : 0,
    #"Clube" : 0,
    #"Federado" : 0,
    #"Resultado" : 0


#Usados para construção de um elemento de cada vez
elementoAtual = ""
categoriaAtual = ""
linhaElemento = 0

#Ficheiro a ser interpertado
file = open("emd.csv",'r')

#Análise do ficheiros e dos seus dados, bem como guardar os mesmos num dicionário
startData = time.time()

for linha in file:

    exp = re.compile(r'(\d+-\d+-\d+)\,\w+\,\w+\,(\d+)\,(\w)\,(\w+)\,([\w]+)\,[\w]+\,[\w.]+@[\w.]+\,(\w+)\,(\w+)$')
    if campos := re.search(exp,linha):

        if categoriaAtual:
            adicionaElemento(categoriaAtual,linhaElemento,elementoAtual,resultadosCategorias)

        linhaElemento = nrLinha
        categoriaAtual = campos.group(1)
        elementoAtual = campos.group(2)

        if ("data") not in resultadosCategorias:
            resultadosCategorias["data"] = {'nrElementos':0, 'elementos':{}}


    elif campos := re.search(r'I\-(\w+)[ \t]+(.+)',linha):

        elementoAtual += (" " + campos.group(2))

    else:
        pass

    nrLinha += 1

if categoriaAtual:
    adicionaElemento(categoriaAtual,linhaElemento,elementoAtual,resultadosCategorias)


endData = time.time()
print(endData-startData," seconds to get necessary data.")

#Ordenação do dicionário com toda a informação
startOrder = time.time()
resultadosCategorias = sortedByKey(resultadosCategorias)
for (key,value) in resultadosCategorias.items():
    value['elementos'] = sortedByKey(value['elementos'])
endOrder = time.time()
print(endOrder-startOrder," seconds to order the data.")

#Criação do HTML consoante os dados conseguidos
startHTML = time.time()
createHTML(resultadosCategorias)
endHTML = time.time()
print(endHTML-startHTML," seconds to create HTML's.")
