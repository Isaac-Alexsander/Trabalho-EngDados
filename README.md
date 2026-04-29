# Projeto: Implementação de Tabelas Transacionais (Delta Lake & Apache Iceberg)

**Instituição:** SATC (Associação Beneficente da Indústria Carbonífera de Santa Catarina) 
**Curso:** Engenharia de Software
**Disciplina:** Engenharia de Dados
**Professor:** Jorge Luiz Silva
**Acadêmico:** Isaac Alexsander Pereira Pessoa

---

## 📋 Descrição do Projeto
Este projeto demonstra a implementação e manipulação de tabelas transacionais utilizando o **Apache Spark**. O foco principal é explorar os formatos de armazenamento **Delta Lake** e **Apache Iceberg**, evidenciando as propriedades **ACID** (Atomicidade, Consistência, Isolamento e Durabilidade) por meio de operações de `INSERT`, `UPDATE` e `DELETE`.

---

## 🛠️ Tecnologias e Ambiente
Para garantir a reprodutibilidade e a organização profissional do projeto, foram utilizadas as seguintes ferramentas:

* **Sistema Operacional:** WSL2 (Ubuntu)
* **Gerenciador de Projetos:** UV (Gerenciador de pacotes e ambientes Python em Rust)
* **Engine de Processamento:** Apache Spark 3.5+ (PySpark)
* **Formatos de Tabela:** Delta Lake 3.1.0 e Apache Iceberg 1.5.0
* **Documentação:** MkDocs com Material Theme
* **Ambiente de Desenvolvimento:** Visual Studio Code com Extensão Jupyter

---

## 🚀 Como Reproduzir o Ambiente

Siga os passos abaixo para configurar e rodar o projeto localmente no seu ambiente Linux/WSL:

### 1. Requisitos Prévios
Certifique-se de possuir instalado em sua máquina:
* **Python 3.12+**
* **Java JRE/JDK 17** ou superior
* **Gerenciador UV:**
  curl -LsSf https://astral.sh/uv/install.sh | sh

### 2. Instalação e Configuração
Clone o repositório e acesse a pasta do projeto:
  git clone https://github.com/Isaac-Alexsander/Trabalho-EngDados.git
  cd Trabalho-EngDados

Sincronize as dependências e crie o ambiente virtual automaticamente com o comando:
  uv sync

### 3. Execução dos Notebooks
1. Inicie o editor: code .
2. Abra o arquivo desejado (ex: vendas_analytics.ipynb).
3. No canto superior direito do VS Code, selecione o Kernel: Python 3.12.3 (.venv).
4. Execute as células sequencialmente para observar as transformações de dados.

---

## 🌐 Documentação do Projeto (MkDocs)
A documentação completa, com explicações teóricas detalhadas e evidências visuais das operações, está publicada em:

👉 **[Site Oficial do Projeto - Isaac Alexsander](https://Isaac-Alexsander.github.io/Trabalho-EngDados/)**

### Comandos de Documentação:
* **Visualização Local:** uv run mkdocs serve
* **Publicação (Deploy):** uv run mkdocs gh-deploy

---

## 📚 Referências e Materiais de Pesquisa
As tecnologias e conceitos aplicados neste projeto foram baseados nas seguintes documentações e fontes exigidas:

* **Delta Lake:** [Documentação Oficial (docs.delta.io)](https://docs.delta.io/)
* **Apache Iceberg:** [Documentação Oficial (iceberg.apache.org)](https://iceberg.apache.org/)
* **Gerenciador UV:** [Guia de Instalação e Uso (astral.sh)](https://docs.astral.sh/uv/)
* **Canal DataWay BR:** [Vídeos e Tutoriais sobre Engenharia de Dados](https://www.youtube.com/@DataWayBR)
* **Repositórios de Referência:** [Spark-Delta](https://github.com/jlsilva01/spark-delta) e [Spark-Iceberg](https://github.com/jlsilva01/spark-iceberg)