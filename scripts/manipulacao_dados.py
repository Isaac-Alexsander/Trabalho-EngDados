from pyspark.sql import SparkSession
from delta import configure_spark_with_delta_pip
from delta.tables import DeltaTable
import os

# Configuração para carregar os jars necessários
builder = SparkSession.builder \
    .appName("ManipulacaoDeltaIceberg") \
    .config("spark.jars.packages", "org.apache.iceberg:iceberg-spark-runtime-3.5_2.12:1.5.0,io.delta:delta-spark_2.12:3.0.0") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension,org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.iceberg.spark.SparkSessionCatalog") \
    .config("spark.sql.catalog.local", "org.apache.iceberg.spark.SparkCatalog") \
    .config("spark.sql.catalog.local.type", "hadoop") \
    .config("spark.sql.catalog.local.warehouse", "warehouse")

spark = configure_spark_with_delta_pip(builder).getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

print("\n--- 🛠️ Iniciando Manipulação de Dados ---")

# --- OPERAÇÕES NO DELTA LAKE ---
print("\n[Delta Lake] Executando Update e Delete...")
deltaTable = DeltaTable.forPath(spark, "warehouse/tabela_vendas_delta")

# Update: Laptop (ID 1) agora custa 5000
deltaTable.update(
    condition = "id = 1",
    set = { "preco": "5000.0" }
)

# Delete: Remover Cabo HDMI (ID 5)
deltaTable.delete(condition = "id = 5")

print("✅ Delta Lake atualizado:")
deltaTable.toDF().show()

# --- OPERAÇÕES NO APACHE ICEBERG ---
print("\n[Apache Iceberg] Executando Update e Delete...")
# No Iceberg usamos SQL para facilitar
spark.sql("UPDATE local.tabela_vendas_iceberg SET preco = 5000.0 WHERE id = 1")
spark.sql("DELETE FROM local.tabela_vendas_iceberg WHERE id = 5")

print("✅ Apache Iceberg atualizado:")
spark.table("local.tabela_vendas_iceberg").show()

# --- TIME TRAVEL (VOLTA NO TEMPO) NO DELTA ---
print("\n[Delta Lake] 🕒 Recuperando dados da Versão 0 (Antes das alterações)...")
df_passado = spark.read.format("delta").option("versionAsOf", 0).load("warehouse/tabela_vendas_delta")
df_passado.show()

spark.stop()
