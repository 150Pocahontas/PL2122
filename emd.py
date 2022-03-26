import re
import time

from createHTML import createHTML

#Função auxiliar para ordenar um dicionário consoante as suas Keys
def sortedByKey(resultadosCategorias):
    dicionarioOrdenado = {k:v for k,v in sorted(resultadosCategorias.items())}
    return dicionarioOrdenado

#Função auxiliar que adiciona ao Dicionário cada elemento ocorrido na categoria certa
def adicionaElemento(categoria,indiceLinha,filhoCategoria,elemento,resultadosCategorias):
    resultadosCategorias[categoria]['nrElementos'] += 1
    if elemento not in resultadosCategorias[categoria]['elementos']:
        resultadosCategorias[categoria]['elementos'][filhoCategoria][elemento] = [indiceLinha]
    else:
        resultadosCategorias[categoria]['elementos'][filhoCategoria][elemento].append(indiceLinha)



#Usados para construção do Dicionário
nrLinha = 1
resultadosAnos = {}

resultadosAnos['total'] = {
    "genero": {
        "M": [], 
        "F": []
    },
    "moralidade": {},
    "genero por idade": {
        "M, >= 35": [],
        "M, < 35": [],
        "F, >= 35": [],
        "F, < 35": [],
    },
    "morada": {},
    "federado": {
        "false": [],
        "true": [],
    },
    "aptos": {
        "false": [],
        "true": []
    }
}

#Usados para construção de um elemento de cada vez
# categoriaAtual = ""
linhaElemento = 0

#Ficheiro a ser interpertado
file = open("emd.csv",'r', encoding="utf-8")

#Análise do ficheiros e dos seus dados, bem como guardar os mesmos num dicionário
startData = time.time()

for linha in file:
    if campos := re.search(r'(\d+)-\d+-\d+\,\w+\,\w+\,(\d+)\,(\w)\,(\w+)\,([\w]+)\,[\w]+\,[\w.]+@[\w.]+\,(\w+)\,(\w+)',linha):

        linhaElemento = nrLinha
        anoAtual = campos.group(1)

        nomePessoa = " ".join(linha.split(',')[3:5])

        if anoAtual not in resultadosAnos:
            resultadosAnos[anoAtual] = {
                "genero": {
                    "M": [], 
                    "F": []
                },
                "moralidade": {},
                "genero por idade": {
                    "M, >= 35": [],
                    "M, < 35": [],
                    "F, >= 35": [],
                    "F, < 35": [],
                },
                "morada": {},
                "federado": {
                    "false": [],
                    "true": [],
                },
                "aptos": {
                    "false": [],
                    "true": []
                }
            }

        genero = campos.group(3)
        resultadosAnos[anoAtual]['genero'][genero].append(nomePessoa)
        resultadosAnos['total']['genero'][genero].append(nomePessoa)

        moralidade = campos.group(5)
        if moralidade not in resultadosAnos[anoAtual]['moralidade'] :
            resultadosAnos[anoAtual]['moralidade'][moralidade] = [nomePessoa]
        else :
            resultadosAnos[anoAtual]['moralidade'][moralidade].append(nomePessoa)

        if moralidade not in resultadosAnos['total']['moralidade'] :
            resultadosAnos['total']['moralidade'][moralidade] = [nomePessoa]
        else :
            resultadosAnos['total']['moralidade'][moralidade].append(nomePessoa)

        idade = campos.group(2)
        
        if int(idade) < 35 :
            resultadosAnos[anoAtual]['genero por idade'][genero + ', < 35'].append(nomePessoa)
            resultadosAnos['total']['genero por idade'][genero + ', < 35'].append(nomePessoa)
        else :
            resultadosAnos[anoAtual]['genero por idade'][genero + ', >= 35'].append(nomePessoa)
            resultadosAnos['total']['genero por idade'][genero + ', >= 35'].append(nomePessoa)

        morada = campos.group(4)
        if morada not in resultadosAnos[anoAtual]['morada'] :
            resultadosAnos[anoAtual]['morada'][morada] = [nomePessoa]
        else :
            resultadosAnos[anoAtual]['morada'][morada].append(nomePessoa)

        if morada not in resultadosAnos['total']['morada'] :
            resultadosAnos['total']['morada'][morada] = [nomePessoa]
        else :
            resultadosAnos['total']['morada'][morada].append(nomePessoa)

        federado = campos.group(6)
        resultadosAnos[anoAtual]['federado'][federado].append(nomePessoa)
        resultadosAnos['total']['federado'][federado].append(nomePessoa)
        
        apto = campos.group(7)
        resultadosAnos[anoAtual]['aptos'][apto].append(nomePessoa)
        resultadosAnos['total']['aptos'][apto].append(nomePessoa)


        # adicionaElemento(categoriaAtual,linhaElemento,"idade",campos.group(2),resultadosCategorias)     
    
    
    
    else:
        pass
    nrLinha += 1


# print(resultadosAnos)

endData = time.time()
print(endData-startData," seconds to get necessary data.")

#Ordenação do dicionário com toda a informação
startOrder = time.time()
resultadosAnos = sortedByKey(resultadosAnos)
for (key,value) in resultadosAnos.items():
    value = sortedByKey(value)
endOrder = time.time()
print(endOrder-startOrder," seconds to order the data.")

#Criação do HTML consoante os dados conseguidos
startHTML = time.time()
createHTML(resultadosAnos)
endHTML = time.time()
print(endHTML-startHTML," seconds to create HTML's.")