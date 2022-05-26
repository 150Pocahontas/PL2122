# -----------------------------------------------------------------
#                         INIT Productions
# -----------------------------------------------------------------
# Se o 1o elemento nao for um simbolo terminal entao adicionamos esse ao segundo elemento do conjunto do First
# Se for um simbolo terminal e estiver no First dá erro sendo que o First tem que guardar o valor dos Axiomas par dps aceder
# Se for um simbolo terminal e nao estiver no First entao adiciona-o ao primeiro elemento do conjunto First
def init_prods(terminal, prods, prod_first, prod_appear, errors):
	for prod in prods:
		for els in prods[prod]:	
			if els[0] not in terminal:
				prod_first[prod][1].append(els[0])

			elif els[0] in prod_first[prod][0]:
				errors.add((prod, "First/First"))

			else:
				prod_first[prod][0].append(els[0])

			for el in els:
				if not el or el in terminal or el != "":
					continue
				if el not in prods:
					print("No definition to this production:", el)
					raise Exception("")

				prod_appear[el].add(prod)

	return prod_first, prod_appear, errors

# -----------------------------------------------------------------
#                         LOOKAHEAD - calculo do lookahead
# -----------------------------------------------------------------
def compute_lookahead(terminal, prods, prod_first, prod_follow, prod_appear, errors):
    # percorre todas as produçoes (descobre o get_first terminal)
    prod_lookahead = {prod: [] for prod in prods}
    # prod_els = [(el, prod) for prod in prods for el in prod]
    for prod in prods:
        for el in prods[prod]:
            if el[0] in terminal:
                prod_lookahead, errors = merge_arrays_with_lookahead(prod_lookahead, prod, [el[0]], errors, "First/First")
            elif el[0]:
                first, errors = get_first(el[0], terminal, prods, prod_first, prod_follow, prod_appear, errors)
                prod_lookahead, errors = merge_arrays_with_lookahead(prod_lookahead, prod, first, errors, "First/First")
            else:
                follow, errors = get_follow(prod, terminal, prods, prod_first, prod_follow, prod_appear, errors)
                prod_lookahead, errors = merge_arrays_with_lookahead(prod_lookahead, prod, follow, errors, "First/Follow")

    return prod_lookahead, errors

# -----------------------------------------------------------------
#                         LL1 detection
# -----------------------------------------------------------------
# Verifica se aparece inicialmente um axioma a seguir ao S (produçao inicial)
# o First tem obrigatoriamente o conjunto de simbolos terminais seguidos pelo axioma que vem na linha seguinte
# o Follow é o conjunto de simbolos terminais a seguir à entrada dum axioma
def LL1(prods, terminal, axioma):
    
    errors = set()
    prod_first = {
        prod: ([], []) for prod in prods
    } 
    prod_follow = {axioma: [""]}  # "" = simbolo terminal
    prod_appear = {
        prod: set() for prod in prods
    }  
    prod_first, prod_appear, errors = init_prods(
        terminal, prods, prod_first, prod_appear, errors
    )
    
    prod_lookahead, errors = compute_lookahead(terminal, prods, prod_first, prod_follow, prod_appear, errors)
    is_ll = len(errors) == 0

    return is_ll, prod_first, prod_follow, prod_appear, prod_lookahead, errors

# -----------------------------------------------------------------
#                         ARRAYS
# -----------------------------------------------------------------
#junta 2 arrays e deteta os erros de tipo First/First Follow/First
def merge_arrays_with_lookahead(prod_lookahead, prod, lookahead, errors, error):

    for _ in prod_lookahead[prod]:
        errors.union(set((prod, error) for el in lookahead if el in prod_lookahead[prod]))

    prod_lookahead[prod].extend(lookahead)
    
    return prod_lookahead, errors


def merge_arrays(
    array_1, array_2, errors, error=None
):
    diff = [el for el in array_2 if el not in array_1]
    array_1.extend(diff)
    if error is not None:
        for _ in diff:
            errors.add(error)

    return array_1, errors

# -----------------------------------------------------------------
#                         FIRST
# -----------------------------------------------------------------

def get_first(prod, terminal, prods, prod_first, prod_follow, prod_appear, errors):
    
    first = prod_first[prod][0]

    if prod in prod_first[prod][1]:
        errors.add((prod, "Left Recursion"))

    for prod_term in prod_first[prod][1]:
        if prod_term and prod_term != prod:
            first_term, errors = get_first(prod_term, terminal, prods, prod_first, prod_follow, prod_appear, errors)
            first, errors = merge_arrays(first, first_term, errors, error = (prod, "First/First"))

        else:
            follow_term, errors = get_follow(prod, terminal, prods, prod_first, prod_follow, prod_appear, errors)
            first, errors = merge_arrays(first, follow_term, errors, error = (prod, "First/Follow"))

    return first, errors

# -----------------------------------------------------------------
#                         FOLLOW
# -----------------------------------------------------------------

def get_follow(prod, terminal, prods, prod_first, prod_follow, prod_appear, errors, v=[]):
    result = []

    
    if prod in prod_follow:
        return prod_follow[prod], errors

    prod_appears = prod_appear[prod]
    for appear in prod_appears:
        for els in prods[appear]:
            i = 0
            while True:
                if prod not in els[i:]:
                    break

                i = els[i:].index(prod) + 1
                if i >= len(els):
                    if appear != prod and appear not in v:
                        appear_follow, errors = get_follow(
                            appear,
                            terminal,
                            prods,
                            prod_follow,
                            prod_appear,
                            errors,
                            v + [appear],
                        )
                        result, errors = merge_arrays(result, appear_follow, errors)
                        continue

                if els[i] in terminal:
                    if els[i] not in result:
                        result.append(els[i])
                        continue
                
                first, errors = get_first(els[i], terminal, prods, prod_first, prod_follow, prod_appear, errors)
                result, errors = merge_arrays(result, first, errors)
    if len(v) == 0:
        prod_follow[prod] = result
        
    return result, errors

# -----------------------------------------------------------------
#                         TABLE
# -----------------------------------------------------------------
# O numero de colunas é o numero de simbolos terminais existentes 
# para cada coluna verifica a partir do ultimo simbolo terminal
# se é o lookahead do axioma
def generate_table(prods, terminal, lookahead):
    table = {}
    aux = 0

    for prod in prods:
        table[prod] = []
        for id_t in range(len(terminal)):
            for id, el in enumerate(lookahead[prod]):
                if terminal[id_t] in el:
                    aux = id
            table[prod].append(aux)

    return table

# -----------------------------------------------------------------
#                         PRINT RESULTS
# -----------------------------------------------------------------

def print_ll1(terminal, prods, prod_first, prod_follow, prod_lookahead):
    print("\n", terminal, "\n\n")
    for i in prods:
        print("Production ", i, ":")
        print("First:", prod_first[i])
        if i in prod_follow:
            print("Follow:", prod_follow[i])
        print("Lookahead:")
        print(prod_lookahead[i])


def print_errors(errors):
    print(errors)
    for i in errors:
        print("Error in production {} type: {}".format(i[0], i[1]))
