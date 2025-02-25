# Python para Dados - Desafio Final

# Considerando a base de dados de saude_do_sono_estilo_vida.csv responda as questões abaixo.

"""Você é uma pesquisadora que está tentando entender melhor qual o impacto do estilo de vida de uma pessoa na sua qualidade de sono, 
por isso fez a coleta dos dados de sobre 373 pessoas, onde foram recolhidas 12 características para cada uma delas. 
Por competência a sua pesquisa foi bem controlada e você não tem dados faltosos na sua base. Chegou o momento de você fazer sua
análise e responder algumas perguntas."""

"""1. Ao visualizar a base você percebeu que seria melhor alterar o nome de algumas colunas. 
Mude o ‘ID’ para ‘Identificador’, corrija o nome da coluna que indica a pressão sanguínea, mude a coluna ‘Ocupação’ para ‘Profissão’,
a coluna ‘Categoria BMI’ está em parte em inglês, substitua para ‘Categoria IMC’."""

import pandas as pd

# Carregando o arquivo CSV
df = pd.read_csv('desafio-individual/saude_do_sono_estilo_vida.csv')

# Alterando o nome das colunas
df.rename(columns={
    'ID': 'Identificador',
    'Pressão sanguíneaaaa': 'Pressão sanguínea',
    'Ocupação': 'Profissão',
    'Categoria BMI': 'Categoria IMC'
}, inplace=True)

# Exibindo as primeiras linhas para verificar as mudanças
print(df.head())





"""2. Qual é a média, a moda e a mediana de horas de sono para cada uma das profissões? [‘mean’, np.median, pd.Series.mode]"""

# Agrupando por profissão e calculando a média, mediana e moda da duração do sono
estatisticas_sono = df.groupby('Profissão')['Duração do sono'].agg(['mean', 'median', pd.Series.mode])

# Exibindo o resultado
print(estatisticas_sono)





"""3. Das pessoas que atuam com engenharia de software qual a porcentagem de obesos?"""

# Filtrando apenas os engenheiros de software
eng_software = df[df['Profissão'] == 'Eng. de Software']

# Calculando a porcentagem de obesos
porcentagem_obesos = (eng_software['Categoria IMC'] == 'Obesidade').mean() * 100

# Exibindo o resultado
print(f"Porcentagem de obesos entre engenheiros de software: {porcentagem_obesos:.2f}%")





"""4. De acordo com os dados, advogar ou ser representante de vendas faz você dormir menos? (Use o método ‘isin’, considere a média)"""

# Filtrando advogados e representantes de vendas
profissoes = ['Advogado(a)', 'Representante de Vendas']
filtro = df[df['Profissão'].isin(profissoes)]

# Calculando a média de horas de sono para cada profissão
media_sono = filtro.groupby('Profissão')['Duração do sono'].mean()

# Exibindo o resultado
print(media_sono)





"""5. Entre quem fez enfermagem e quem fez medicina, quem tem menos horas de sono? (Use o método ‘isin’, considere a média)"""

# Filtrando enfermeiros e médicos
profissoes = ['Enfermeiro(a)', 'Médico(a)']
filtro = df[df['Profissão'].isin(profissoes)]

# Calculando a média de horas de sono para cada profissão
media_sono = filtro.groupby('Profissão')['Duração do sono'].mean()

# Exibindo o resultado
print(media_sono)





"""6. Faça um subconjunto com as colunas Identificador, Gênero, Idade, Pressão sanguínea e Frequência cardíaca."""

# Criando um subconjunto com as colunas desejadas
subconjunto = df[['Identificador', 'Gênero', 'Idade', 'Pressão sanguínea', 'Frequência cardíaca']]

# Exibindo as primeiras linhas do subconjunto
print(subconjunto.head())





"""7. Descubra qual a profissão menos frequente no conjunto. (Use value_counts)"""

# Contando a frequência de cada profissão
frequencia_profissoes = df['Profissão'].value_counts()

# Encontrando a profissão menos frequente
profissao_menos_frequente = frequencia_profissoes.idxmin()

# Exibindo o resultado
print(f"A profissão menos frequente é: {profissao_menos_frequente}")





"""8. Quem tem maior pressão sanguínea média, homens ou mulheres? (Considere a média)"""

# Remover espaços e extrair apenas o primeiro valor da pressão sistólica antes da barra
df['Pressão sanguínea'] = df['Pressão sanguínea'].str.split('/').str[0].astype(float)

# Verificando a coluna depois de converter para numérico
print(df['Pressão sanguínea'].head())

# Calculando a média da pressão sanguínea por gênero
media_pressao = df.groupby('Gênero')['Pressão sanguínea'].mean()

# Exibindo o resultado
print(media_pressao)

# Verificando quem tem maior pressão sanguínea média
if not media_pressao.isna().all():
    maior_pressao = media_pressao.idxmax()  # Gênero com maior média
    maior_pressao_valor = media_pressao.max()  # Valor da maior média
    print(f'O gênero com maior pressão sanguínea média é {maior_pressao} com {maior_pressao_valor:.2f} mmHg.')
else:
    print("Não foi possível calcular a média devido a valores inválidos ou ausentes.")





"""9. É predominante entre os participantes dormir 8 horas por dia (considere usar Moda como medida)?"""

# Calculando a moda da duração do sono
moda_sono = df['Duração do sono'].mode()

# Verificando se 8 horas está na lista de modas
predominante = 8 in moda_sono.values

# Exibindo o resultado
if predominante:
    print("É predominante dormir 8 horas por dia? Sim")
else:
    print("É predominante dormir 8 horas por dia? Não")





"""10. Pessoas com frequências cardíacas acima de 70 dão mais passos que pessoas com frequência cardíaca menor ou igual a 70? (Use a média)"""

# Dividindo os dados em dois grupos: frequência cardíaca acima de 70 e menor ou igual a 70
grupo_acima_70 = df[df['Frequência cardíaca'] > 70]
grupo_ate_70 = df[df['Frequência cardíaca'] <= 70]

# Calculando a média de passos para cada grupo
media_passos_acima_70 = grupo_acima_70['Passos diários'].mean()
media_passos_ate_70 = grupo_ate_70['Passos diários'].mean()

# Exibindo o resultado
print(f"Média de passos para frequência cardíaca acima de 70: {media_passos_acima_70:.2f}")
print(f"Média de passos para frequência cardíaca menor ou igual a 70: {media_passos_ate_70:.2f}")




