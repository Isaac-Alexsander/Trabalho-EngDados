# Projeto: Implementação de Tabelas Transacionais (Delta Lake & Apache Iceberg)

**Instituição:** SATC (Associação Beneficente da Indústria Carbonífera de Santa Catarina)  
**Curso:** Engenharia de Software  
**Disciplina:** Engenharia de Dados  
**Professor:** Jorge Luiz Silva  
**Acadêmico:** Isaac Alexsander Pereira Pessoa  

---

## 📋 Descrição do Projeto
Este projeto demonstra a implementação e manipulação de tabelas transacionais utilizando **Apache Spark**, com foco nos formatos de armazenamento **Delta Lake** e **Apache Iceberg**. O objetivo é evidenciar as propriedades ACID (Atomicidade, Consistência, Isolamento e Durabilidade) através de operações de `INSERT`, `UPDATE` e `DELETE`.

---

## 🛠️ Tecnologias e Ambiente
Para garantir a reprodutibilidade e organização profissional do projeto, foram utilizadas as seguintes ferramentas:

* **SO:** WSL2 (Ubuntu)
* **Gerenciador de Pacotes:** [UV](https://github.com/astral-sh/uv) (Escolha exclusiva conforme requisito)
* **Engine:** Apache Spark 3.5+ (PySpark)
* **Formatos:** Delta Lake 3.1.0 & Apache Iceberg 1.5.0
* **Documentação:** MkDocs com tema Material
* **IDE:** Visual Studio Code (Extensão Jupyter)

---

## 🚀 Como Reproduzir o Ambiente

Siga os passos abaixo para rodar o projeto localmente no seu ambiente Linux/WSL:

### 1. Requisitos Prévios
Certifique-se de ter instalado:
* Python 3.12+
* Java JRE/JDK 17 ou superior
* Gerenciador UV (`curl -LsSf https://astral.sh/uv/install.sh | sh`)

### 2. Instalação
Clone o repositório e navegue até a pasta:
```bash
git clone https://github.com/Isaac-Alexsander/Trabalho-EngDados.git
cd trabdados

Sincronize as dependências e o ambiente virtual automaticamente com o UV:

Bash
uv sync

3### 3. Execução do Notebook
Abra o VS Code: code .

Abra o arquivo vendas_analytics.ipynb.

No canto superior direito, selecione o Kernel: Python 3.12.3 (.venv) localizado em ./venv/bin/python.

Execute as células sequencialmente

🌐 Documentação (MkDocs)
A documentação detalhada, incluindo explicações teóricas e evidências das operações, está publicada em:
👉 [INSIRA https://Isaac-Alexsander.github.io/Trabalho-EngDados/]

Comandos MkDocs:
Testar localmente: uv run mkdocs serve

Publicar: uv run mkdocs gh-deploy

---
