#Função que cria o HTML das páginas relativas a uma categoria em específico.

import os
import matplotlib.pyplot as plt

def createHTMLPages(ano, categoria, elementos):

    if not os.path.exists('pages/'+ano.lower()) :
        os.makedirs('pages/'+ano.lower())

    pathFicheiro = 'pages/'+ano.lower()+'/'+categoria.lower()+'.html'
    nrElementos = sum(len(values) for key, values in elementos.items())
    elementoNr = 1

    if not os.path.exists('figures') :
        os.makedirs('figures')


    with open (pathFicheiro, 'w', encoding="utf-8") as ficheiro:
        ficheiro.write(f'''<!DOCTYPE html>
<html>
   <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css ">
        <link rel="stylesheet" href="../css/style.css">
        <title>{categoria}</title>
    </head>
    <body>
        <div class="w3-bar w3-black w3-top">
            <span class="marca w3-bar-item w3-mobile">Processamento de Linguagens <b>(Grupo 29)</b></span>
            <span class="w3-right w3-mobile">
                <a href=".../index.html" class="marca w3-bar-item w3-button w3-mobile w3-hover-orange">Voltar à Página Inicial</a>
            </span>
        </div>

        <section class="showcaseElementos">
            <div class="w3-container w3-center">
                <h1 class="w3-text-shadow w3-animate-zoom">Trabalho TP1 PL - Enunciado 3</h1>
                <h2 class="w3-text-shadow w3-animate-zoom">Grupo 29</h2>
                <hr class="w3-animate-zoom">
            </div>
        </section>

        <section class="listagemElementos w3-animate-zoom">
            <h2 class="w3-center w3-text-shadow">Distribuição da Categoria <b>{categoria}</b><b> em {ano}</b></h2>
            <h3 class="w3-center w3-text-shadow">{nrElementos} Ocorrências</h3>

            <ul class="w3-ul w3-grey w3-mobile w3-hoverable">''')

        if not os.path.exists('figures/'+ano) :
            os.makedirs('figures/'+ano)

        if categoria != "morada" :
            plt.figure()

            if categoria == "aptos" :
                values = [len(v) for v in elementos.values()]
                total = sum(values)
                labels = [key + " : " + str(round(len(elementos[key])/total * 100, 2)) + "%" for key in elementos]
                plt.pie(values, labels = labels)

            else :
                plt.barh(list(elementos.keys()), [len(x) for x in elementos.values()])
            plt.tight_layout()
            pathFigure = 'pages/'+ano.lower()+'/'+categoria.lower()+'.png'
            plt.savefig(pathFigure)
            plt.close()

            ficheiro.write(f'''
                <button onclick="myFunction('distribuição')" class="w3-button w3-block w3-left-align w3-hover-deep-orange">
                    <span class="topografia w3-mobile"><b>Distribuição</b></span>
                </button>
                <div id="distribuição" class="w3-container w3-hide w3-center w3-light-grey">
                    <div class="w3-row">''')
            ficheiro.write(f'''<img src="{'./'+categoria.lower()+'.png'}"> </img>''')
            ficheiro.write(f'''
                    </div>
                </div>''')
            ficheiro.write('''
            <hr>''')

        for (elemento, linhas) in elementos.items():
            ficheiro.write(f'''
                <button onclick="myFunction('{elemento}')" class="w3-button w3-block w3-left-align w3-hover-deep-orange">
                    <span class="topografia w3-mobile"><b>{elemento}</b></span>
                    <span class="topografia w3-right w3-mobile">{len(linhas)} Ocorrências</span>
                </button>
                <div id="{elemento}" class="w3-container w3-hide w3-center w3-light-grey">
                    <div class="w3-row">''')


            # print(linhas)
            # print(type(linhas))
            for linha in linhas:
                ficheiro.write(f'''
                        <div class="w3-col s12 w3-center"><p>{linha}</p></div>''')
            ficheiro.write(f'''
                    </div>
                </div>''')
            if elementoNr != nrElementos:
                ficheiro.write('''
                <hr>''')
            elementoNr += 1

        ficheiro.write('''
            </ul>
        </section>
        <script>
            function myFunction(id) {
              var x = document.getElementById(id);
              if (x.className.indexOf("w3-show") == -1) {
                x.className += " w3-show";
                x.className.replace(" w3-show", "")
              } else {
                x.className = x.className.replace(" w3-show", "");
              }
            }
        </script>
    </body>
</html>
''')



#Função que cria o HTML da página principal do Projeto onde podemos aceder às várias outras categorias
def createYearHTML(ano, resultadosCategorias):

    nrCategorias = len(resultadosCategorias)
    categoriaNr = 1

    with open ('pages/'+ano.lower()+'.html', 'w', encoding="utf-8") as ficheiro:

        ficheiro.write(f'''<!DOCTYPE html>
<html>
   <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=2">
        <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css ">
        <link rel="stylesheet" href="css/style.css">
    </head>
    <body>

        <div class="w3-bar w3-black w3-top">
            <span class="marca w3-bar-item w3-mobile">Processamento de Linguagens <b>(Grupo 29)</b></span>
        </div>
        <p style="padding: 10px; margin: 10px">

        <section class="listagemCategorias w3-animate-zoom">
            <h2 class="w3-center w3-text-shadow">Categorias encontradas em {ano}: </h2>
            <ul class="w3-ul w3-deep-orange w3-mobile w3-hoverable">''')

        for (categoria, elementosCategoria) in resultadosCategorias.items():
            createHTMLPages(ano, categoria, elementosCategoria)
            nrElementos = sum(len(values) for key, values in elementosCategoria.items())
            pathFicheiro = 'pages/'+ano.lower()+'/'+categoria.lower()+'.html'
            ficheiro.write(f'''
                <a href="{ano.lower()+'/'+categoria.lower()+'.html'}">
                    <li class="w3-bar w3-mobile w3-hover-orange">
                        <span class="categoria w3-bar-item w3-mobile">{categoria}</span>
                        <span class="nrElementos w3-bar-item w3-right w3-mobile">{nrElementos} elementos</span>
                    </li>
                </a>''')
            if categoriaNr != nrCategorias:
                ficheiro.write('''
                <hr>''')
            categoriaNr += 1

        ficheiro.write(f'''
            </ul>
        </section>
    </body>
</html>
''')

#Função que cria o HTML da página principal do Projeto onde podemos aceder às várias outras categorias
def createHTML(resultadosAnos) :
    nrAnos = len(resultadosAnos)
    AnoNr = 1

    with open ("index.html", 'w', encoding="utf-8") as ficheiro:

        ficheiro.write(f'''<!DOCTYPE html>
<html>
   <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=2">
        <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css ">
        <link rel="stylesheet" href="css/style.css">
        <title>Trabalho TP1 PL - Enunciado 3</title>
    </head>
    <body>

        <div class="w3-bar w3-black w3-top">
            <span class="marca w3-bar-item w3-mobile">Processamento de Linguagens <b>(Grupo 29)</b></span>
        </div>
        <p style="padding: 10px; margin: 10px">
        <section class="showcase">
            <div class="w3-container w3-center">
                <h1 class="w3-text-shadow w3-animate-zoom">Trabalho TP1 PL - Enunciado 3</h1>
                <h2 class="w3-text-shadow w3-animate-zoom">Grupo 29</h2>
                <hr class="w3-animate-zoom">
                <p class="w3-animate-zoom wr-center">Hoje em dia, a área de Machine Learning está na moda e as suas metodologias e
                tecnologias são usadas em muitas áreas. A maior parte dos algoritmos de Machine Learning têm de ser treinados com um
                dataset especialmente anotado à mão e depois testados sobre outro dataset anotado para ver se o que a máquina
                descobre é o mesmo que um ser humano faria à mão.</p>
                <p class="w3-animate-zoom wr-center">Neste problema, programamos a extração de várias categorias e
                elementos informativos de um dataset, concebendo um Website para a visualização dos mesmos.</p>
            </div>
        </section>

        <section class="listagemCategorias w3-animate-zoom">
            <h2 class="w3-center w3-text-shadow">Anos encontradas: </h2>
            <ul class="w3-ul w3-deep-orange w3-mobile w3-hoverable">''')

        for (ano, categoriasAno) in resultadosAnos.items():
            createYearHTML(ano, categoriasAno)
            pathFicheiro = 'pages/'+ano.lower()+'.html'
            ficheiro.write(f'''
                <a href="{pathFicheiro}">
                    <li class="w3-bar w3-mobile w3-hover-orange">
                        <span class="categoria w3-bar-item w3-mobile">{ano}</span>
                    </li>
                </a>''')
            if AnoNr != nrAnos:
                ficheiro.write('''
                <hr>''')
            AnoNr += 1

        ficheiro.write(f'''
            </ul>
        </section>
    </body>
</html>
''')