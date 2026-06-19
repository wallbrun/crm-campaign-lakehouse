import pandas as pd
import os

print("Iniciando camada Silver...")

# ==========================
# CLIENTES
# ==========================

clientes = pd.read_parquet(
    "data/bronze/clientes/clientes.parquet"
)

clientes = clientes.dropna()

clientes["cidade"] = (
    clientes["cidade"]
    .str.upper()
    .str.strip()
)

clientes["faixa_renda"] = pd.cut(
    clientes["renda"],
    bins=[0, 5000, 10000, 20000, 999999],
    labels=[
        "BAIXA",
        "MEDIA",
        "ALTA",
        "PREMIUM"
    ]
)

os.makedirs(
    "data/silver/clientes",
    exist_ok=True
)

clientes.to_parquet(
    "data/silver/clientes/clientes.parquet",
    index=False
)

# ==========================
# TRANSACOES
# ==========================

transacoes = pd.read_parquet(
    "data/bronze/transacoes/transacoes.parquet"
)

transacoes = transacoes[
    transacoes["valor"] > 0
]

transacoes["data"] = pd.to_datetime(
    transacoes["data"]
)

os.makedirs(
    "data/silver/transacoes",
    exist_ok=True
)

transacoes.to_parquet(
    "data/silver/transacoes/transacoes.parquet",
    index=False
)

# ==========================
# RESPOSTAS
# ==========================

respostas = pd.read_parquet(
    "data/bronze/respostas/respostas.parquet"
)

os.makedirs(
    "data/silver/respostas",
    exist_ok=True
)

respostas.to_parquet(
    "data/silver/respostas/respostas.parquet",
    index=False
)

print("Silver finalizada com sucesso!")

# ==========================
# CAMPANHAS
# ==========================

campanhas = pd.read_parquet(
    "data/bronze/campanhas/campanhas.parquet"
)

os.makedirs(
    "data/silver/campanhas",
    exist_ok=True
)

campanhas.to_parquet(
    "data/silver/campanhas/campanhas.parquet",
    index=False
)