# ------------------------------------------------------------
# program_lex.py
#
# Parser recursivo descendente para a linguagem criada:
#
# ------------------------------------------------------------
import ply.lex as lex


# STRING-> todas as palavras/nomes
# TERM -> todos os simbolos terminais

tokens = ['STRING','TERM','NUM','FUNCTION','STAR','HASH','DOTS','EXCLAM','BAR','TAB','LINE','NEWLINE']
states = [("line","exclusive")]

def t_STRING(t):
	r"\w+" 
	return t

def t_TERM(t):
	r'"(?:(?:(?!(?<!\\)").)*)"'
	return t

def t_NUM(t):
	r"\d+"
	return t

def t_FUNCTION(t):
	r"\#\#"
	t.lexer.push_state("line")
	return t

def t_STAR(t):
	r"\*"
	return t

def t_HASH(t):
	r"\#"
	t.lexer.change = True
	return t

def t_DOTS(t):
	r":"
	if(t.lexer.change):
		t.lexer.change = False
		t.lexer.push_state("line")
	return t

def t_EXCLAM(t):
	r"\!"
	t.lexer.push_state("line")
	return t

def t_BAR(t):
	r"(\t|[ ])*\|"
	return t

def t_TAB(t):
	r"\t[^\n]*"
	return t

def t_line_LINE(t):
	r"[^\n]+"
	i = 0 
	flag = True
	while(flag):
		if i < len(t.value) and t.value[i] == " ":
			i += 1
		else:
			flag = False
	t.value = t.value[i:]  
	t.lexer.pop_state()
	return t

def t_line_NEWLINE(t):
	r"\n"
	t.lexer.pop_state()
	return t	

t_line_ignore = ""

def t_NEWLINE(t):
	r"\n"
	t.lexer.lineno += 1
	return t


# Error handling rule
def t_ANY_error(t):
	print("Illegal character: ",t.value[0]," \nLine: ",t.lineno)
	t.lexer.skip(1)


t_ignore = " "

#fd = open("teste1")
lexer = lex.lex()
lexer.change = False
lexer.nline = 0
