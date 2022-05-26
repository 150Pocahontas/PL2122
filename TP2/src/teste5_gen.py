from ply import lex
import sys
from copy import deepcopy

tokens = ["TERM_1" ,"TERM_2" ,"TERM_3" ,"TERM_4"]

 
def t_TERM_1(t):
	r"\("
	t.value = (1, t.value)
	return t
 
def t_TERM_2(t):
	r"\)"
	t.value = (2, t.value)
	return t
 
def t_TERM_3(t):
	r"\+"
	t.value = (3, t.value)
	return t
 
def t_TERM_4(t):
	r"\*"
	t.value = (4, t.value)
	return t
 
def t_ANY_error(t):
	t.value = (-1,t.value)
	t.lexer.skip(1)
	return t

class Aux:
	pass
aux = Aux()
 
lexer = lex.lex()
inp = sys.stdin
error = False
fich = False
copie = deepcopy(aux)

inFilePath = input("Code File Path >> ")
try:
	fd = open(inFilePath, "r")
	inp = [fd.read()]
	fich = True
	
except (error):
        print("Wrong File Path")
        error = True
if not(error):
	for line in inp:
		if not(fich):
			line = line[:-1]
		lexer.input(line)

	axioma = "S"
	prods = {'S': [['Exp']], 'Exp': [['"\\d+"'], ['"\\("', 'Funcao', '"\\)"']], 'Funcao': [['"\\+"', 'Lista']], 'Lista': [['"\\*"']]}
	term = ['"\\d+"', '"\\("', '"\\)"', '"\\+"', '"\\*"']
	table = {'S': [0, 1, 1, 1, 1], 'Exp': [0, 1, 1, 1, 1], 'Funcao': [1, 1, 1, 0, 0], 'Lista': [0, 0, 0, 0, 0]}

	indice = 0
	position = 0
	stack = []
	n = axioma
	function = prods[n][position]
	arg = [] 

	Error = False
	Recognize = False

	match = lexer.token().value
	token = match[1]
	match = match[0]

	while not(Error):
		if indice >= len(function) or function[indice] == None:
			if stack:
				function,indice,arg = stack.pop()
			else: Recognize = True
		elif function[indice] in term: 
			arg.append(token)
			indice += 1
			match = lexer.token()
			if match:
				match = match.value
				token = match[1]
				match = match[0]
		elif match != None and match != -1:
			stack.append((function,indice+1,arg))
			n = function[indice]
			t = table[n][match]
			if t != None:
				function = prods[n][t]
				arg = []
				indice = 0
			else:
				Error = True
		else:
				Error = True
	if Error:
		if token == "":token = "Terminal"
		print("Error in the position:",lexer.lexpos,"group: (",token,")")
	aux = deepcopy(copie)
	print(aux)
	
if fich:
	fd.close()
