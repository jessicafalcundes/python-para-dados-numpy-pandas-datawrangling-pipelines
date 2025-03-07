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
aluno = {
    "nome": "jessica",
    "idade": 27,
    "curso": "cibersegurança"
}

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