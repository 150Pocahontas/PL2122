import ply.yacc as yacc
from prog_lex import *
from LL1 import *
import os
import re
import sys

# -----------------------------------------------------------------
#                           ENTRY
# -----------------------------------------------------------------

def p_Axiom(p):
        "Axiom : All"
        p[0] = p[1]

def p_all(p):
        "All : Entry"
        pass

def p_All_Entry(p):
        "All : All Entry"
        pass

def p_Entry(p):
        "Entry : Production NEWLINE"
        name,prod,act = p[1]
        if (p.parser.axioma == ""):
                p.parser.axioma = name
        if(name in p.parser.prods): 
                p.parser.prods[name].append(prod)
                p.parser.act[name].append(act)
        else: 
                p.parser.prods[name] = [prod]
                p.parser.act[name] = [act]

def p_Entry_Action(p):
        "Entry : act"
        pass

def p_Entry_Function(p):
        "Entry : Function"
        p.parser.function += p[1]

def p_Function(p):
        "Function : FUNCTION String"
        p[0] = p[2]
# -----------------------------------------------------------------
#                           Production
# -----------------------------------------------------------------

def p_Production(p):
        "Production : Identification DOTS Symbols"
        p[0] = (p[1],p[3],"")
        p.parser.name = p[1]

def p_Production_identification_symbols(p):
        "Production : Identification DOTS Symbols EXCLAM LINE"
        p[0] = (p[1],p[3],"\t"+p[5])
        p.parser.name = p[1]

def p_Production_bar_symbols(p):
        "Production : BAR Symbols"
        if (p.parser.name == ""): 
                p.parser.error = True
        p[0] = (p.parser.name,p[2],"")

def p_Production_bar_symbols_exclam(p):
        "Production : BAR Symbols EXCLAM LINE"
        if (p.parser.name == ""): 
                p.parser.error = True
        p[0] = (p.parser.name,p[2],"\t"+p[4])

# -----------------------------------------------------------------
#                           Symbols
# -----------------------------------------------------------------

def p_Symbols(p):
        "Symbols : Symbol"
        p[0] = [p[1]]
        
def p_Symbols_symbol(p):
        "Symbols : Symbols Symbol"
        p[0] = p[1] + [p[2]]

def p_Symbol(p):
        "Symbol : TERM"
        if not(p[1] in p.parser.term) and p[1] != '""':
                p.parser.term.append(p[1])
        elif p[1] == '""':
                p[1] = None
        p[0] = p[1]

def p_Symbol_term(p):
        "Symbol : terminal"
        p[0] = p[1]
# -----------------------------------------------------------------
#                           Semantic act
# -----------------------------------------------------------------
def p_Action_dot(p):
    "act : HASH Identification DOTS String"
    if p[2] in p.parser.act:
        p.parser.act[p[2]][0] = p[4]
        
    else:
        print(p[2] + " doesn't exist in this grammar")
        p.parser.error = True

def p_Action_star(p):
    "act : HASH Identification STAR NUM DOTS String"
    if p[2] in p.parser.act:
        if int(p[4]) < len(p.parser.act[p[2]]):
            p.parser.act[p[2]][int(p[4])] = p[6]
        else:
            print("This production doesn't exist:{}*{}".format(p[2],p[4]))
    else:
        print(p[2] + " doesn't exist in this grammar")
        p.parser.error = True
# -----------------------------------------------------------------
#                           String
# -----------------------------------------------------------------

def p_String(p):
        "String : LINE NEWLINE Strings"
        p[0] = p[1] + p[2] + p[3]

def p_String_line(p):
        "String : LINE"
        p[0] = p[1] + "\n"

def p_String_newline(p):
        "String : NEWLINE Strings"
        p[0] = p[2] 

def p_String_line_newline(p):
        "String : LINE NEWLINE"
        p[0] = p[1] + p[2]

def p_Strings_newline(p):
        "Strings : NEWLINE"
        p[0] = ""

def p_Strings_tab(p):
        "Strings : TAB NEWLINE"
        p[0] = p[1] + p[2]

def p_Strings_tab_newline(p):
        "Strings : Strings TAB NEWLINE"
        p[0] = p[1] + p[2] + p[3]

# -----------------------------------------------------------------
#                           Other
# -----------------------------------------------------------------

def p_Identification(p):
        "Identification : STRING"
        p[0] = p[1]

def p_terminal(p):
        "terminal : STRING"
        p[0] = p[1]

def p_error(p):
        print('Illegal Character: ', p)
        parser.success = False
# Build the parser
parser = yacc.yacc()
# -----------------------------------------------------------------
#                         PARSER
# -----------------------------------------------------------------

def parse_(file):

    parser.error = False
    parser.act = {}
    parser.prods = {}
    parser.function = ""
    parser.name = ""
    parser.term = []
    parser.axioma = ""

    try:
        fd = open(file,"r")
        for line in fd :
            #print(line)
            parser.parse(line)

    except (FileNotFoundError, NotADirectoryError) as error:
        print("Wrong File Path\n")
        parser.error = True
        raise(error)

    return (parser.term,parser.prods,parser.axioma,parser.function,parser.act,parser.error)
# -----------------------------------------------------------------
#                         RUN
# -----------------------------------------------------------------
# Build the parser

inFilePath = input("Code File Path >> ")
term, prods, axioma, function, act, error = parse_(inFilePath)

is_ll, prod_first, prod_follow, prod_appear, prod_lookahead, errors = LL1(prods, term, axioma)
        
try:
    is_ll, prod_first, prod_follow, prod_appear, prod_lookahead, errors = LL1(prods, term, axioma)

except Exception as e:
    print(f"Error computing LL1 : {e}")
    sys.exit(1)

print(f"File is LL1 : {is_ll}")

   







