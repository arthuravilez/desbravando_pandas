# %%
import pandas as pd

# pode dar erro pois não tem a biblioteca do openpyxl
# pip install openpyxl
df = pd.read_excel("../data/transactions.xlsx")
df

# %%
df.shape

# %%
df.head()

# %%
df.tail()

# %%

colunas = ['UUID',
           "Points",
           'IdCustomer',
           "DtTransaction"]

df = df[colunas]
df

# %%
df.info(memory_usage='deep')
# %%
