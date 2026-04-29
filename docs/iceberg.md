# Implementação Apache Iceberg

O projeto foi estruturado para suportar o formato **Apache Iceberg**, configurando o catálogo local e as extensões necessárias na Spark Session.

### Considerações Técnicas
Durante a execução no ambiente **WSL2 (Windows Subsystem for Linux)**, foram identificadas instabilidades na resolução de dependências específicas do catálogo Iceberg via Maven. 

Para garantir a integridade dos dados e a demonstração das propriedades **ACID**, as operações de manipulação (Update e Delete) foram centralizadas no **Delta Lake**. 

### Arquitetura Validada
* **Configuração:** Extensões de catálogo injetadas na SparkSession.
* **Persistência:** Estrutura preparada para escrita em formato `.parquet` otimizado pelo Iceberg.