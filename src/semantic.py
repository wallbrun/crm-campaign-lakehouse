import duckdb

conn = duckdb.connect(
    "analytics.db"
)

# Clientes

conn.execute("""

CREATE OR REPLACE TABLE customer_metrics AS

SELECT *

FROM read_parquet(
'data/gold/customer_metrics/customer_metrics.parquet'
)

""")

# Campanhas

conn.execute("""

CREATE OR REPLACE TABLE campaign_metrics AS

SELECT *

FROM read_parquet(
'data/gold/campaign_metrics/campaign_metrics.parquet'
)

""")

print("Tabelas criadas!")

conn.close()