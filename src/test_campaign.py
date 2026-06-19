import duckdb

conn = duckdb.connect(
    "analytics.db"
)

df = conn.execute("""

SELECT *

FROM campaign_metrics

""").fetchdf()

print(df)

conn.close()