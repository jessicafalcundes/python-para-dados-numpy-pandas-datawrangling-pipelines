# sintaxe

# print("29 pearls in your kiss \n a singing smile \n coffee smell and lilac skin \n your flame in me")

# operadores matemáticos
'''
# soma
1+2+3

# subtração
1-2-3 

# multiplicação
1*2*3

# exponenciação
2**3

# divisão
1/2/3

# resto da divisão
3%4

# divisão de chão
3//2

# priorização
(2+2)*5
'''

# variáveis - contêineres para armazenar valores de dados.
# uma variável é criada no momento em que você atribui um valor a ela
# não colocar espaço no nome da variável, mas sim _

#musica_mais_ouvida = 'everybody here wants you'

#musica_mais_ouvida

'''
# variáveis de texto
var_texto_01 = 'anything - test \n'
var_texto_02 = str('anything') #nomeado valor como texto

print(var_texto_01, var_texto_02)


# variaveis numéricas
var_inteiro_01 = 100
var_inteiro_02 = int(200)

print(var_inteiro_01, var_inteiro_02)

# variáveis flutuantes
var_flutuante_01 = 10.90
var_flutuante_02 = float(11.50)

print(var_flutuante_01, var_flutuante_02)
'''
'''
# variáveis booleanas - condições
var_booleano_01 = True
var_booleano_02 = False
print(var_booleano_01, var_booleano_02)

# sistema (paga, não) --> paga -->VIP / não -->Not VIP
'''


#tipos de dados
# listas - são criadas usando []
# tuplas - são criadas usando ()
# dicionários - são criados usando {}
# esses dados podem receber quaisquer tipos de informações, inclusive operações aritméticas

# listas
'''lista_exemplo_01 = [1, 2, 3, 4, 5, 6, 7, 8]

lista_exemplo_02 = ['nome', 'sobrenome', 'idade']

lista_exemplo_03 = [1, 'texto', True, [1, 2, 3]]'''

'''melhor_atriz_oscar = ["Fernanda Torres", "Demi Moore", "Anora"]
melhor_atriz_oscar.append("Mikey Madison")  # adicionando um item
print(melhor_atriz_oscar)'''  # saída: ['Fernanda Torres', 'Demi Moore', 'Anora', 'Mikey Madison']

# tuplas - são imutáveis
'''tupla_exemplo_01 = (1, 2, 3)
tupla_exemplo_02 = ('nome', 'sobrenome', 'idade')'''

'''cores = ("vermelho", "azul", "verde")
# cores.append("amarelo")  # erro! tuplas não podem ser alteradas
print(cores)  # saída: ('vermelho', 'azul', 'verde')'''


# dicionário - estrutura de dados que armazena pares chave-valor, diferente de listas e tuplas, que armazenam apenas valores individuais.
'''dicionário = {
    'index' : 'valor',
    'id' : 1,
    'id' : 2,
    'nome': 'fernanda torres'
}'''

# criando um dicionário
'''aluno = {
    "nome": "jessica",
    "idade": 27,
    "curso": "cibersegurança"
}'''

# acessando valores
#print(aluno["nome"])  # saída: jessica

# adicionando uma nova chave-valor
'''aluno["nota"] = 9.5
print(aluno)'''  # {'nome': 'ana', 'idade': 22, 'curso': 'cibersegurança', 'nota': 9.5}

# alterando um valor
'''aluno["idade"] = 28
print(aluno)'''

# removendo um item
'''del aluno["curso"]
print(aluno)'''  # {'nome': 'ana', 'idade': 23, 'nota': 9.5}


# nomeação de variáveis
'''permitido: usar letras (a-z, A-Z), números (0-9) e underline (_).
começar sempre com uma letra ou underscore (_).'''

'''não permitido:
começar com número (ex: 1variavel → erro).
usar espaços (ex: minha variavel → erro, use minha_variavel).
usar símbolos especiais (@, $, %, !, - etc.).
usar palavras reservadas de python (ex: def, class, if, else etc.).'''

# convenções que deixam o código mais legível:
# nomes descritivos
"""nome_completo = "laura palmer"
quantidade_de_produtos = 10"""


'''use snake_case para variáveis e funções
python segue o padrão snake_case (palavras separadas por _).
evite camelCase (usado em outras linguagens como JavaScript).'''
"""nome_usuario = "samuel"
quantidade_itens = 5"""


'''use UPPER_CASE para constantes
variáveis que não devem ser alteradas (constantes) usam letras maiúsculas.'''
"""PI = 3.1415
TAXA_JUROS = 0.05"""

'''evite usar a letra "l" minúscula e "O" maiúscula como variáveis
podem ser confundidas com 1 (um) e 0 (zero).'''
"""l = 10  # parece com '1'
O = 50  # parece com '0'"""

# nomeando

"""Cinema, Show, Teatro = 1, 2, 3
print(Cinema, Show, Teatro)"""

"""Cinema = Show = Teatro = 'Lazer'
print(Cinema, Show, Teatro)"""

# nomear com listas
"""lista_carros = ['Uno', 'Fusca', 'Brasília']
marca_01, marca_02, marca_03 = lista_carros
print(marca_01, marca_02, marca_03)"""

# combinar variáveis
"""nome = 'Laura '
sobrenome = 'Palmer'
nome_completo = nome + sobrenome
print(nome_completo)"""


# tipos da informação
# tipos básicos
# exemplos de tipos básicos
"""
idade = 27       # int
altura = 1.60    # float
nome = "jessica" # str
ativo = True     # bool

print(int(idade))   # <class 'int'>
print(float(altura))  # <class 'float'>
print(str(nome))    # <class 'str'>
print(bool(ativo))   # <class 'bool'>
"""

# tipos estruturados (coleções)
'''
list: lista (mutável e ordenada) - ex: frutas = ["maçã", "banana"]
tuple: tupla (imutável e ordenada) - ex: cores = ("azul", "vermelho")
dict: dicionário (chave-valor) - ex: aluno = {"nome": "ana", "idade": 22}
set: conjunto (sem ordem e sem valores repetidos) - ex: numeros = {1, 2, 3, 4}'
'''

# exemplos de coleções
"""
frutas = ["amora", "morango", "cereja"]  # lista
cores = ("preto", "branco", "cinza")   # tupla
aluno = {"nome": "jessica", "idade": 27}    # dicionário
numeros = {1, 2, 3, 4}                  # conjunto

print(list(frutas))  # <class 'list'>
print(tuple(cores))   # <class 'tuple'>
print(dict(aluno))   # <class 'dict'>
print(set(numeros)) # <class 'set'>
"""

# tipos especiais
'''
NoneType: representa ausência de valor - ex: vazio = None
complex: números complexos - ex: z = 2 + 3j
bytes: sequência de bytes - ex: dados = b"abc"
'''

# exemplos de tipos especiais
"""
vazio = None
z = 2 + 3j
dados = b"abc"

print(type(vazio))  # <class 'NoneType'>
print(complex(z))      # <class 'complex'>
print(bytes(dados))  # <class 'bytes'>
"""

# conversão de tipos (casting)
"""
x = "10"
y = int(x)  # converte string para inteiro
print(y, type(y))  # 10 <class 'int'>

z = float(y)  # converte inteiro para float
print(z, type(z))  # 10.0 <class 'float'>

n = str(z)  # converte float para string
print(n, type(n))  # "10.0" <class 'str'>
"""

# resumo
# tipos básicos: int, float, str, bool
# coleções: list, tuple, dict, set
# especiais: NoneType, complex, bytes
# é possível converter tipos com int(), float(), str() etc.

"""
String = str('hello world')
Inteiro = int(10)
Flutuante = float(100.5)
Complexo = complex(1j)
Lista = list( ('livros', 'cds', 'discos'))
Tupla = tuple(('A', 'B',))
Range = range(6)
Dicionario = dict(nome='jessica', age=27)
Set = set(('A', 'B', 'C'))
Fronzet = frozenset(('A', 'B', 'C'))
Boleano = bool(5)
Bytes = bytes(5)
ByteArray = bytearray(5)
Memoryview = memoryview(bytes(5))

from datetime import datetime
Data = datetime.today().date()

type(Data)
"""

# comando round
# o comando round() em python é usado para arredondar números decimais (float) para um número específico de casas decimais.

'''round(numero, ndigits)'''

# numero: o número que você quer arredondar.

# ndigits (opcional): o número de casas decimais desejadas.
# se não for informado, o padrão é 0, ou seja, ele arredonda para o inteiro mais próximo.

"""
print(round(3.14159))       # saída: 3  (arredonda para o inteiro mais próximo)
print(round(3.14159, 2))    # saída: 3.14  (duas casas decimais)
print(round(3.14159, 4))    # saída: 3.1416  (quatro casas decimais)
print(round(3.5))           # saída: 4  (arredonda para cima)
print(round(2.5))           # saída: 2  (arredonda para o número par mais próximo)
"""
"""
regras de arredondamento em python
python segue a regra do arredondamento para o par mais próximo (também chamada de round half to even), 
que evita viés estatístico.

números terminados em .5 são arredondados para o número par mais próximo.
"""
"""
print(round(1.5))  # saída: 2  (1.5 -> arredonda para 2)
print(round(2.5))  # saída: 2  (2.5 -> arredonda para 2, pois 2 é par)
print(round(3.5))  # saída: 4  (3.5 -> arredonda para 4)
print(round(4.5))  # saída: 4  (4.5 -> arredonda para 4, pois 4 é par)
"""
"""
arredondando números negativos
o round() funciona da mesma forma para números negativos:
"""
"""
print(round(-3.14159, 2))  # saída: -3.14
print(round(-2.5))         # saída: -2  (arredonda para o número par mais próximo)
print(round(-3.5))         # saída: -4  (arredonda para baixo)
"""

# arredondando números grandes
"""
quando ndigits é negativo, ele arredonda para múltiplos de 10:
round(1234.5678, -1) → 1230.0 (arredonda para a dezena mais próxima)
round(1234.5678, -2) → 1200.0 (arredonda para a centena mais próxima)
"""
"""
print(round(1234.5678, 2))  # saída: 1234.57
print(round(1234.5678, -2)) # saída: 1200.0  (arredonda para centenas)
"""

# comando len
# o comando len() em python é usado para contar o número de elementos em uma sequência (como listas, strings, tuplas, dicionários, etc.)

# len(objeto)

# objeto: pode ser uma string, lista, tupla, dicionário, conjunto, entre outros.

# exemplos

# contar caracteres em uma string
'''texto = "python"
print(len(texto))'''  # saída: 6 (conta os caracteres da string)

# contar elementos em uma lista
'''numeros = [10, 20, 30, 40]
print(len(numeros))'''  # saída: 4 (quantidade de elementos na lista)

# contar elementos em uma tupla
'''tupla = (1, 2, 3, 4, 5)
print(len(tupla))'''  # saída: 5

# contar chaves em um dicionário
'''dados = {"nome": "Ana", "idade": 25, "cidade": "São Paulo"}
print(len(dados))'''  # saída: 3 (conta quantas chaves existem no dicionário)

# contar elementos em um conjunto (set)
'''conjunto = {1, 2, 3, 4, 5}
print(len(conjunto))'''  # saída: 5



# casos especiais
# len() em uma string vazia
'''print(len(""))'''  # saída: 0


# len() em uma lista vazia
'''print(len([]))'''  # saída: 0

# len() em um dicionário vazio
'''print(len({}))'''  # saída: 0


"""
len("python") # conta os caracteres da string
len([10, 20, 30]) # conta os elementos da lista
len((1, 2, 3, 4)) # conta os elementos da tupla
len({"a": 1, "b": 2}) # conta as chaves do dicionário
len(set([1, 2, 3])) # conta os elementos do conjunto
"""

# fatiamento de strings
# o fatiamento de strings em python permite acessar partes específicas de uma string usando índices.

# string[início:fim:passo]
"""
início: índice onde o fatiamento começa (opcional, padrão é 0).
fim: índice onde o fatiamento termina (não inclui esse índice).
passo: define o salto entre caracteres (opcional, padrão é 1).
"""

# exemplos práticos
# acessando um intervalo de caracteres


# texto = "jessica"

'''print(texto[0:4])  # saída: "pyth" (pega do índice 0 ao 3)
print(texto[2:6])'''  # saída: "thon" (pega do índice 2 ao 5)


# omitindo início ou fim
'''print(texto[:4])   # saída: "pyth" (do início até o índice 3)
print(texto[2:])   # saída: "thon" (do índice 2 até o final)
print(texto[:]) '''   # saída: "python" (toda a string)


# usando passo para pular caracteres
'''print(texto[::2])  # saída: "pto" (pega de 2 em 2)
print(texto[1::2])''' # saída: "yhn" (começa do índice 1 e vai pulando de 2 em 2)

# fatiamento com índices negativos - índices negativos contam de trás para frente:
'''print(texto[-4:])  # saída: "thon" (pega os últimos 4 caracteres)
print(texto[:-2])'''  # saída: "pyth" (remove os últimos 2 caracteres)

# invertendo uma string
'''print(texto[::-1])'''  # saída: "nohtyp" (string ao contrário)


'''texto[0:4]	"pyth"	pega do índice 0 ao 3
texto[:4]	"pyth"	do início ao índice 3
texto[2:]	"thon"	do índice 2 ao final
texto[::2]	"pto"	pula de 2 em 2
texto[::-1]	"nohtyp"	inverte a string '''

'''minha_string = "mas vc adora um se"

print(type(minha_string))
print(len(minha_string))

print(minha_string[-1])'''

'''CPF = 'CPF: 46164286898'
print(CPF[-11:])'''



# manipulação de strings
# envolve várias funções e métodos úteis para modificar, formatar e trabalhar com textos.

# convertendo para maiúsculas e minúsculas
# texto = "Python é incrível"

'''print(texto.upper())   # saída: "PYTHON É INCRÍVEL"
print(texto.lower())   # saída: "python é incrível"
print(texto.title())   # saída: "Python É Incrível" (primeira letra de cada palavra maiúscula)
print(texto.capitalize())'''  # saída: "Python é incrível" (só a primeira maiúscula)


# removendo espaços extras
'''espacos = "   python   "

print(espacos.strip())  # saída: "python" (remove espaços das pontas)
print(espacos.lstrip()) # saída: "python   " (remove da esquerda)
print(espacos.rstrip())''' # saída: "   python" (remove da direita)



# substituindo partes da string
'''frase = "eu gosto de java"

print(frase.replace("java", "python"))'''  # saída: "eu gosto de python"


# separando e unindo strings
'''dados = "jessica,guilherme,helena"

lista = dados.split(",")  # separa pelo delimitador ","
print(lista)  # saída: ['ana', 'joão', 'maria']

unido = "-".join(lista)  # junta com "-"
print(unido)'''  # saída: "ana-joão-maria"



# verificando conteúdo
'''frase = "estudando python"

print(frase.startswith("estudando"))  # saída: True (verifica se começa com "estudando")
print(frase.endswith("java"))         # saída: False (não termina com "java")
print("python" in frase)              # saída: True (verifica se contém "python")
print("java" not in frase)'''            # saída: True (não contém "java")


# alinhando texto
'''palavra = "python"

print(palavra.center(10, "-"))  # saída: "--python--" (centraliza com "-")
print(palavra.ljust(10, "."))   # saída: "python...." (alinha à esquerda)
print(palavra.rjust(10, "."))'''   # saída: "....python" (alinha à direita)


# contagem e localização de palavras
'''texto = "história, literatura, história, sociologia, filosofia"

print(texto.count("história"))  # saída: 2 (quantas vezes "história" aparece)
print(texto.find("literatura"))     # saída: 8 (posição onde "literatura" começa)
print(texto.rfind("filosofia"))'''  # saída: 15 (última ocorrência de "filosofia")

'''
upper() / lower() # maiúsculas/minúsculas
strip() / lstrip() / rstrip() # remove espaços
replace("a", "b")	# substitui texto
split(",")	# divide string em lista
join(lista)	# junta elementos com separador
startswith("x") / endswith("y")	# verifica início/fim
count("x")	# conta ocorrências
find("x") / rfind("x")	# encontra posição
'''
'''
replace()
startswith()
endswith()
count()
capitalize()
isdigit()
isalnum()
upper()
lower()
find ()
strip()
split()
'''

# Imprimindo uma string.
String = 'Olá Mundão!'
print( String )

# Tipo de uma string.
print( type( String ) )

# Tamanho de uma string.
print( len( String ) )

# Concatenação
print( String + ' Estou aprendendo Python...' )

# Substitui uma substring por alguma outra coisa.
Substituir = String.replace('Mundão', 'Mundo Louco :X')
print( Substituir )

# A string s começa com "Olá"?
print( String.startswith('Olá') )

# A string termina com "mundo"?
print( String.endswith('mundo') )

# Quantas ocorrências da palavra "a" a string possui?
print( String.count('M') )

# Capitalize - Transformar a primeira letra da primeira palavra em maiúscula.
String_02 = 'odemir depieri'
print( String_02.capitalize() )

# Verificar se uma string só possui números.
String_03 = '123456789'
String_04 = '123456789ABC'
print( String_03.isdigit() )
print( String_04.isdigit() )

# Verificar se uma string é alfanumérica (só possui letras e números).
print( '12345abc'.isalnum() )

# Transformar tudo em Maiusculo
print( String.upper() )

# Transformar tudo em Minúsculo
print( String.lower() )

# Procurar algo na string
print( String.find('!') )

# Removendo espaçoes antes e fim da palavra
String_05 =' Olá Mundão! '
print( String_05.strip() )

# Removendo espaçoes antes e fim da palavra
String_06 ='Loja 1 vendou 10, Loja 2 vendou 20, Loja 3 vendou 30 '
print( String_06.split(',') )
