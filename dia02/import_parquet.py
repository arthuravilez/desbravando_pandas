# %%

import pandas as pd

# Se der erro pode ser que tenha que instalar essa biblioteca
# pip install --upgrade pyarrow fastparquet
df = pd.read_parquet("../data/transactions_cart.parquet")
df
# %%
