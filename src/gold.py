import pandas as pd
import os

print("Iniciando camada Gold...")

# ==========================
# CLIENTES
# ==========================

clientes = pd.read_parquet(
    "data/silver/clientes/clientes.parquet"
)

# ==========================
# TRANSACOES
# ==========================

transacoes = pd.read_parquet(
    "data/silver/transacoes/transacoes.parquet"
)

# Garantir tipo data

transacoes["data"] = pd.to_datetime(
    transacoes["data"]
)

# ==========================
# MÉTRICAS
# ==========================

gold = transacoes.groupby(
    "cliente_id"
).agg(
    receita_total=("valor", "sum"),
    ticket_medio=("valor", "mean"),
    qtd_compras=("valor", "count"),
    ultima_compra=("data", "max")
).reset_index()

# ==========================
# JOIN CLIENTES
# ==========================

gold = gold.merge(
    clientes,
    on="cliente_id",
    how="left"
)

# ==========================
# SEGMENTAÇÃO
# ==========================

def segmentar(valor):

    if valor > 20000:
        return "PREMIUM"

    elif valor > 10000:
        return "GOLD"

    else:
        return "STANDARD"

gold["segmento"] = (
    gold["receita_total"]
    .apply(segmentar)
)

# ==========================
# SALVAR
# ==========================

os.makedirs(
    "data/gold/customer_metrics",
    exist_ok=True
)

gold.to_parquet(
    "data/gold/customer_metrics/customer_metrics.parquet",
    index=False
)

print("Gold finalizada com sucesso!")