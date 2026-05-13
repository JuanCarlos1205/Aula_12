import pandas as pd 

print('Listas do Python e Series do Pandas')
produtos = ['Notebooks', 'Smartphone', 'Tablet', 'Smartwach', 'Camera']
quantidade_estoque = [15, 30, 20, 10, 25]
print(produtos)
print(quantidade_estoque)

series = pd.Series(produtos)
print(series)


# Indice personalizado
estoque = pd.Series(quantidade_estoque, index=produtos)
print(estoque)


# type diz de que tipo e o objeto
#print(type(series))
#print(type(quantidade_estoque))


