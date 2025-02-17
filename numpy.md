### **NumPy
O Numpy é uma biblioteca essencial para computação científica e manipulação de dados em Python. Ele oferece uma estrutura de dados chamada `array`, que é mais eficiente do que listas tradicionais em Python, principalmente para grandes volumes de dados.

1. ##### **Instalando o Numpy**
Se você ainda não tem o Numpy instalado, pode fazer isso com o seguinte comando:

`pip install numpy`


2. ##### **Importando o Numpy**
Para usar o Numpy, basta importá-lo:

`import numpy as np`


3. ##### **Criando Arrays**
Você pode criar arrays a partir de listas Python:

`import numpy as np`

```
# Criando um array 1D
arr = np.array([1, 2, 3, 4, 5])
print(arr)
```

4. ##### **Tipos de Dados no Numpy**
Você pode especificar o tipo de dados ao criar um array. Por exemplo:

```
arr_int = np.array([1, 2, 3], dtype=int)
arr_float = np.array([1.1, 2.2, 3.3], dtype=float)
```

5. ##### **Arrays Multidimensionais**
Numpy também suporta arrays multidimensionais, como matrizes:

```
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_2d)
```

6. ##### **Acessando e Modificando Elementos**
Você pode acessar elementos de um array como se fosse uma lista:

```
# Acessando o elemento na posição (0, 2)
print(arr_2d[0, 2])
```

```
# Modificando o valor do elemento
arr_2d[0, 2] = 10
print(arr_2d)
```

7. ##### **Operações Básicas**
Você pode fazer operações matemáticas diretamente em arrays:

```
arr = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
```

```
# Soma
print(arr + arr2)
```

```
# Multiplicação por um escalar
print(arr * 2)
```

