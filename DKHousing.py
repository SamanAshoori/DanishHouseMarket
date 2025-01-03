import pyarrow.parquet as pq
import pandas as pd

df = pq.read_table(source="Data/Danish/archive/DKHousingPrices.parquet").to_pandas()
print(df.iloc[0])
