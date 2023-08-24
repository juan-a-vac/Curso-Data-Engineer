#info tomada de https://www.frankfurter.app/
#
import requests
import json
import pandas as pd
from sqlalchemy import create_engine
import psycopg2
import sqlalchemy
from sqlalchemy.engine.url import URL

hostname= 'data-engineer-cluster.cyhh5bfevlmn.us-east-1.redshift.amazonaws.com'
database= 'data-engineer-database'
username= 'juan_a_vaca_11_coderhouse'
pwd='laJ7b0x4v5'
port_id= 5439
engine= create_engine("postgresql://juan_a_vaca_11_coderhouse:laJ7b0x4v5@data-engineer-cluster.cyhh5bfevlmn.us-east-1.redshift.amazonaws.com:5439/data-engineer-database")

#engine= conn = create_engine('postgresql://username:password@yoururl.com:5439/yourdatabase')
#cargamos datos desde el primero de enero de 2020

url1 = 'https://www.frankfurter.app/2021-02-02..2023-08-15'
r1 = requests.get(url1)
j1 = r1.json()
j2 = pd.read_json(j1)

date = pd.DataFrame(j1['rates'])
date = date.T                                       #   traspongo la matriz
date.reset_index(inplace = True)
date.rename(columns={date.columns[0]:'Fecha'},inplace=True)

print(date)
# hasta aca obtenemos el DF principal historico
# Necesitamos una PK compuesta
date['PK_Compuesta'] = date.index.astype(str) + '_' + date[date.columns[0]].astype(str)
date['Fecha'] = pd.to_datetime(date['Fecha'])
#agregamos los datos a la tabla de redshift
date.to_sql('comparacion_divisas', engine, if_exists='replace', index=False)#reemplazamos ya que esta linea solo se ejecuta una vez

#agregado final de datos masivos
'''
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
df_final['date'] = pd.to_datetime(df_final['date'])

#agregamos los datos a la tabla de redshift
df_final.to_sql('comparacion_divisas', engine, if_exists='append', index=False)
df_a = pd.read_sql_table('comparacion_divisas',engine)
'''
