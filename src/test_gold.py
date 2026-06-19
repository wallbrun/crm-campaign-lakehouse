import pandas as pd

df = pd.read_parquet(
    "data/gold/customer_metrics/customer_metrics.parquet"
)

print(df.head())

print()

print(df["segmento"].value_counts())