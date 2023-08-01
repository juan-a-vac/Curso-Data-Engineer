#info tomada de https://www.frankfurter.app/
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
df_final.to_sql('comparacion_divisas', engine, if_exists='replace', index=False)
df_a = pd.read_sql_table('comparacion_divisas',engine)



