import pandas as pd
import os

print("Iniciando camada Bronze...")

arquivos = {
    "clientes": "data/raw/clientes.csv",
    "transacoes": "data/raw/transacoes.csv",
    "campanhas": "data/raw/campanhas.csv",
    "respostas": "data/raw/respostas.csv"
}

for tabela, caminho in arquivos.items():

    print(f"Lendo {tabela}")

    df = pd.read_csv(caminho)

    os.makedirs(f"data/bronze/{tabela}", exist_ok=True)

    df.to_parquet(
        f"data/bronze/{tabela}/{tabela}.parquet",
        index=False
    )

    print(f"{tabela} convertido para parquet")

print("Bronze finalizada com sucesso!")