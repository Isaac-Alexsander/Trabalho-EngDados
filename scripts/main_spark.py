from pyspark.sql import SparkSession
from delta import *
import os

# Definindo versões dos pacotes para evitar conflitos
# Estamos adicionando o pacote do Iceberg explicitamente aqui
ICEBERG_VERSION = "1.5.0"
DEPENDENCIES = f"org.apache.iceberg:iceberg-spark-runtime-3.5_2.12:{ICEBERG_VERSION}"

builder = SparkSession.builder \
    .appName("ProjetoDeltaIceberg") \
    .config("spark.jars.packages", DEPENDENCIES) \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension,org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.iceberg.spark.SparkSessionCatalog") \
    .config("spark.sql.catalog.spark_catalog.type", "hive") \
    .config("spark.sql.catalog.local", "org.apache.iceberg.spark.SparkCatalog") \
    .config("spark.sql.catalog.local.type", "hadoop") \
    .config("spark.sql.catalog.local.warehouse", "warehouse")

# Inicializa a sessão com suporte a Delta
spark = configure_spark_with_delta_pip(builder).getOrCreate()

# CORREÇÃO: O comando correto é sparkContext (sem underline)
spark.sparkContext.setLogLevel("ERROR")

print("🚀 Spark Session iniciada com Delta e Iceberg!")

# 1. Leitura do CSV
df_bronze = spark.read.csv("data/vendas_inicial.csv", header=True, inferSchema=True)

# 2. Escrita em formato Delta
df_bronze.write.format("delta").mode("overwrite").save("warehouse/tabela_vendas_delta")
print("✅ Tabela Delta criada com sucesso!")

# 3. Escrita em formato Iceberg
# Criamos o banco 'local' se não existir e salvamos a tabela
spark.sql("CREATE NAMESPACE IF NOT EXISTS local")
df_bronze.writeTo("local.tabela_vendas_iceberg").createOrReplace()
print("✅ Tabela Iceberg criada com sucesso!")

# Mostra os dados para confirmar
print("\n--- Dados na Tabela Iceberg ---")
spark.table("local.tabela_vendas_iceberg").show()

spark.stop()
