#info tomada de https://www.frankfurter.app/
import requests
import json
import pandas as pd

#requests
url = 'https://www.frankfurter.app/latest'
r = requests.get(url)
j = r.json()
# Desgloso el JSON en columnas utilizando Pandas
df1 = pd.DataFrame(j['rates'].items(), columns=['Currency', 'Rate'])
# Pivoteo el DataFrame para tener las monedas como columnas y las tasas como datos
df1 = df1.pivot_table(index=None, columns='Currency', values='Rate', aggfunc='first')
#eliminamos el indice para que coincida con el indice del otro DF
df1 = df1.reset_index(drop=True)
#Creo un nuevo DataFrame con los valores de 'amount', 'base' y 'date'
data = {
    'amount': [j['amount']],
    'base': [j['base']],
    'date': [j['date']]
}
df2 = pd.DataFrame(data)
df_new = df2.reset_index(drop=True)
#concatenamos ambos df
df_final = pd.concat([df2, df1], axis=1)

print("las filas del df_final son:  ",df_final.shape)
print(df_final)
print(df_final.columns)