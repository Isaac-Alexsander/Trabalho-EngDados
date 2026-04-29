import pandas as pd
import os

# Garante que a pasta data existe
os.makedirs("data", exist_ok=True)

data = {
    "id": [1, 2, 3, 4, 5],
    "produto": ["Laptop", "Mouse", "Teclado", "Monitor", "Cabo HDMI"],
    "preco": [4500.0, 150.0, 200.0, 1200.0, 50.0],
    "estoque": [10, 50, 30, 15, 100]
}

df = pd.DataFrame(data)
df.to_csv("data/vendas_inicial.csv", index=False)
print("✅ Arquivo data/vendas_inicial.csv criado com sucesso!")
