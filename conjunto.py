print("trabalho feito por Lucas Ferraz")
"""
ENUNCIADO
Para obter os pontos relativos a este trabalho, você deverá criar um programa, utilizando a
linguagem Python, C, ou C++. Este programa, quando executado, irá apresentar os resultados de
operações que serão realizadas entre dois conjuntos de dados.
O programa que você desenvolverá irá receber como entrada um arquivo de texto (.txt)
contendo vários conjuntos de dados e várias operações. Estas operações e dados estarão representadas
em um arquivo de textos contendo apenas os dados referentes as operações que devem ser realizadas
segundo a seguinte regra fixa: a primeira linha do arquivo de texto de entrada conterá o número de
operações que estão descritas no arquivo, este número de operações será um inteiro; as linhas
seguintes seguirão sempre o mesmo padrão de três linhas: a primeira linha apresenta o código da
operação (U para união, I para interseção, D para diferença e C produto cartesiano), a segunda e
terceira linhas conterão os elementos dos conjuntos separados por virgulas. A seguir está um exemplo
das linhas que podem existir em um arquivo de testes para o programa que você irá desenvolver:
4
U
3, 5, 67, 7
1, 2, 3, 4
I
1, 2, 3, 4, 5
4, 5
D
1, A, C, 34
A, C, D, 23
C
3, 4, 5, 5, A, B, R
1, B, C, D, 1
Neste exemplo temos 4 operações uma união (U), uma interseção (I), um diferença (D) e um
produto cartesiano (C). A união, definida por U, deverá ser executada sobre os conjuntos {𝟑, 𝟓, 𝟔𝟕, 𝟕} e
{𝟏, 𝟐, 𝟑, 𝟒}, cujos elementos estão explicitados nas linhas posteriores a definição da operção (U).
A resposta do seu programa deverá conter a operação realizada, descrita por extenso, os dados
dos conjuntos identificados, e o resultado da operação. No caso da união a linha de saída deverá conter
a informação e a formatação mostrada a seguir:
União: conjunto 1 {3, 5, 67, 7}, conjunto 2 {1, 2, 3, 4}. Resultado: {3, 5, 67, 7, 1, 2, 4}
Seu programa deverá mostrar a saída no terminal, ou em um arquivo de textos. Em qualquer
um dos casos, a saída será composta por uma linha de saída para cada operação constante no arquivo
de textos de entrada formatada segundo o exemplo de saída acima. Observe as letras maiúsculas e
minúsculas, e os pontos utilizados na formatação da linha de saída apresenta acima.
No caso do texto de exemplo, teremos 4 linhas, e apenas 4 linhas de saída, formatadas e
pontuadas conforme o exemplo de saída acima. O uso de linhas extras na saída, ou erros de formatação,
implicam em perda de pontos como pode ser visto na rubrica de avaliação constante neste documento.
"""

#esse código faz quantas operações vc quiser pois ela lê linha por linha atras da letra que se refere a cada operação ent so use a letra de operação correta.

#vale lembrar que esse codigo que eu fiz suporta apenas 2 conjuntos de dados, e precisa que se digite os numeros dos conjuntos embaixo da letra do operador(U,I,D,C), alem de precisar dividir o conjunto A e B por linhas sendo o conjunto A a primeira linha apos a letra de operação e o B a segunda linha após a letra.


def ler(arquivo):  #aqui
      with open(
          'arquivo.txt', 'r'
      ) as arquivo:  #professor quando  for testar os outros arquivos mude a numeração desse arquivo.txt e do arquivo.txt da def main.
            linha = arquivo.readlines()

      return linha


def união(conjunto1união, conjunto2união):

      conjunto1união = set(conjunto1união.strip().split(','))

      conjunto2união = set(conjunto2união.strip().split(','))

      uniao = conjunto1união.union(conjunto2união)

      print("U")

      print("conjunto U A:", conjunto1união)

      print("conjunto U B:", conjunto2união)

      print("União: conjunto 1", conjunto1união, "conjunto 2", conjunto2união,
            "resultado:", uniao)


def intersec(conjunto1inter, conjunto2inter):

      conjunto1inter = set(conjunto1inter.strip().split(','))

      conjunto2inter = set(conjunto2inter.strip().split(','))

      interseção = conjunto1inter.intersection(conjunto2inter)

      print("I")

      print("conjunto I A:", conjunto1inter)

      print("conjunto I B:", conjunto2inter)

      print("Interseção: conjunto 1", conjunto1inter, "conjunto 2",
            conjunto2inter, "resultado:", interseção)


def diff(conjunto1dife, conjunto2dife):

      conjunto1dife = set(conjunto1dife.strip().split(','))

      conjunto2dife = set(conjunto2dife.strip().split(','))

      diferença = conjunto1dife - conjunto2dife

      print("D")

      print("conjunto D A:", conjunto1dife)

      print("conjunto D B:", conjunto2dife)

      print("Diferença: conjunto 1", conjunto1dife, "conjunto 2",
            conjunto2dife, "resultado:", diferença)


def carte(conjunto1cartesiano, conjunto2cartesiano):

      conjunto1cartesiano = set(conjunto1cartesiano.strip().split(','))

      conjunto2cartesiano = set(conjunto2cartesiano.strip().split(','))

      cartesiano = []

      for a in conjunto1cartesiano:
            for b in conjunto2cartesiano:
                  cartesiano.append((a, b))

      print("C")

      print("conjunto C A:", conjunto1cartesiano)

      print("conjunto C B:", conjunto2cartesiano)

      print("Produto Cartesiano: conjunto 1", conjunto1cartesiano,
            "conjunto 2", conjunto2cartesiano, "resultado:", cartesiano)


def main():
      arquivo = "arquivo.txt"  #e aqui tambem
      linha = ler(arquivo)

      l = 0
      while l < len(linha):
            linhaatt = linha[l].strip()

            if linhaatt == "U":
                  if l + 2 < len(linha):
                        união(linha[l + 1], linha[l + 2])
                        l += 3
                  else:
                        print("falta conjuntos para fazer a operação")
                        break
            elif linhaatt == "I":
                  if l + 2 < len(linha):
                        intersec(linha[l + 1], linha[l + 2])
                        l += 3
                  else:
                        print("falta conjuntos para fazer a operação")
                        break
            elif linhaatt == "D":
                  if l + 2 < len(linha):
                        diff(linha[l + 1], linha[l + 2])
                        l += 3
                  else:
                        print("falta conjuntos para fazer a operação")
                        break
            elif linhaatt == "C":
                  if l + 2 < len(linha):
                        carte(linha[l + 1], linha[l + 2])
                        l += 3
                  else:
                        print("falta conjuntos para fazer a operação")
                        break
            else:
                  print("")
                  l += 1


main()
