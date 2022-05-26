import re
import sys
from prog_yacc import *
from LL1 import *

table = generate_table(prods, term, prod_lookahead) 

# -----------------------------------------------------------------
#                         Tokens
# -----------------------------------------------------------------

token = "tokens = ["

get_terms = ''' 
def t_{0}(t):
	r{1}
	t.value = ({2}, t.value)
	return t
'''
get_errors =''' 
def t_ANY_error(t):
	t.value = (-1,t.value)
	t.lexer.skip(1)
	return t
'''
get_lex = ""

for i in range(1,len(term)):
	term_str = "TERM_" + str(i)
	token += '"' + term_str +"\" ," 
	get_lex += get_terms.format(term_str, term[i],i)
token = token[:-2] + "]\n\n"
imports = "from ply import lex\nimport sys\nfrom copy import deepcopy\n\n"

# -----------------------------------------------------------------
#                         Lexer Parsing
# -----------------------------------------------------------------
aux = '''
class Aux:
	pass
aux = Aux()
'''

lex = ''' 
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
'''
tabela= '''
	axioma = "{}"
	prods = {}
	term = {}
	table = {}

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
	aux = deepcopy(copie)
	print(table)
	
if fich:
	fd.close()
'''.format(axioma, prods, term, table)

if not(error) and is_ll:
	print_ll1(term, prods, prod_first, prod_follow, prod_lookahead)
	fd = open(inFilePath + "_gen.py","w")
	fd.write(imports + token + get_lex + get_errors + aux + lex + tabela)
	fd.close()
else:
	print_errors(errors)









	