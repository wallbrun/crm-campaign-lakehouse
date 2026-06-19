import pandas as pd
import os

print("Criando métricas de campanha...")

respostas = pd.read_parquet(
    "data/silver/respostas/respostas.parquet"
)

campanhas = pd.read_parquet(
    "data/silver/campanhas/campanhas.parquet"
)

metricas = respostas.groupby(
    "campanha_id"
).agg(
    clientes_impactados=("cliente_id", "count"),
    aberturas=("abriu_email", "sum"),
    cliques=("clicou", "sum"),
    conversoes=("converteu", "sum")
).reset_index()

metricas["taxa_abertura"] = (
    metricas["aberturas"]
    / metricas["clientes_impactados"]
)

metricas["ctr"] = (
    metricas["cliques"]
    / metricas["aberturas"]
)

metricas["taxa_conversao"] = (
    metricas["conversoes"]
    / metricas["clientes_impactados"]
)

metricas = metricas.merge(
    campanhas,
    on="campanha_id",
    how="left"
)

os.makedirs(
    "data/gold/campaign_metrics",
    exist_ok=True
)

metricas.to_parquet(
    "data/gold/campaign_metrics/campaign_metrics.parquet",
    index=False
)

print("Métricas de campanha criadas!")