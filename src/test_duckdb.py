import duckdb

conn = duckdb.connect(
    "analytics.db"
)

df = conn.execute("""

SELECT *

FROM customer_metrics

LIMIT 10

""").fetchdf()

print(df)

conn.close()