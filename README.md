## semana 5 e 6: python para dados - **numpy, pandas, data wrangling, e pipelines**

### Conceitos Principais do NumPy

1. #### **Arrays**
Um array é uma estrutura de dados que armazena elementos (dados) de um mesmo tipo (por exemplo, inteiros ou floats) em uma estrutura matricial. Em outras palavras, é uma sequência de elementos organizados de maneira eficiente.

Os arrays do NumPy são mais poderosos e rápidos que as listas tradicionais do Python, pois são otimizados para operar em grandes volumes de dados e oferecem uma série de funcionalidades matemáticas.

Existem diferentes tipos de arrays no NumPy:
* **Array Unidimensional (1D)**: Como uma lista simples em Python.

`arr = np.array([1, 2, 3, 4, 5])`

* **Array Bidimensional (2D)**: Como uma matriz (linha e coluna).

`arr_2d = np.array([[1, 2, 3], [4, 5, 6]])`

* **Array Multidimensional (ND)**: Arrays com mais de duas dimensões (como tensores em aprendizado de máquina).

`arr_nd = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])`



2. #### **Atributos dos Arrays**
Os arrays no NumPy possuem alguns atributos importantes:

* **shape**: Retorna a forma (dimensões) do array.

`arr.shape`

* **ndim**: Retorna o número de dimensões do array.

`arr.ndim`

* **size**: Retorna o número total de elementos no array.

`arr.size`

* **dtype**: Retorna o tipo de dados do array (ex: int64, float32).

`arr.dtype`



3. #### **Operações em Arrays**
O NumPy permite realizar operações matemáticas em arrays de maneira eficiente. Essas operações podem ser feitas elemento por elemento ou em toda a estrutura do array de forma vetorizada (sem usar loops explicitos, o que torna o código mais rápido).

* **Soma e subtração**

```
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print(arr1 + arr2)  # Soma elemento por elemento
print(arr1 - arr2)  # Subtração
```

* **Multiplicação por um escalar**

```
arr = np.array([1, 2, 3])
print(arr * 2)  # Multiplicação de todos os elementos por 2
```

* **Multiplicação entre arrays (produto ponto a ponto)**

`print(arr1 * arr2)`


4. #### **Indexação e Slicing**
NumPy permite acessar os elementos de um array com uma sintaxe semelhante à de listas em Python, mas com recursos adicionais para trabalhar com arrays multidimensionais.

* **Acessar um único elemento**

```
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_2d[0, 2])  # Acessa o elemento na linha 0, coluna 2
```

* **Slicing (fatiamento) Você pode pegar um pedaço do array:**

```
print(arr_2d[0, :])  # Acessa todos os elementos da primeira linha
print(arr_2d[:, 1])  # Acessa todos os elementos da segunda coluna
```



5. #### **Funções do NumPy**
NumPy também oferece uma série de funções para realizar operações matemáticas, estatísticas e transformações de dados.

* **Funções Matemáticas**
    * **Soma dos elementos:**
    
    `print(np.sum(arr))  # Soma todos os elementos do array`

    * **Média:**
    
    `print(np.mean(arr))  # Média dos elementos`

    * **Desvio Padrão:**
    
    `print(np.std(arr))  # Desvio padrão`

* **Funções de Manipulação**
    * **Transposição de Matrizes:**
    
    `arr_2d.T  # Transpõe a matriz`

    * **Redimensionamento de Arrays:**
    
    `arr_2d.reshape(3, 2)  # Altera a forma para 3 linhas e 2 colunas`


#### **Por que Usar o NumPy?**
* **Eficiência**: Arrays do NumPy são mais rápidos e ocupam menos memória em comparação com listas em Python.
* **Vetorizar operações**: Permite aplicar operações matemáticas em todo o array sem usar loops, o que acelera o código.
* **Biblioteca com muitos recursos**: Oferece várias funções para manipulação de dados, cálculo e álgebra linear, tornando-se essencial para tarefas de análise de dados e aprendizado de máquina.