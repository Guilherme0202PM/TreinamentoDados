# Projeto C – Controle de Finanças Pessoais

Este projeto faz parte do **Projeto 1 (Semanas 4 e 5)** do treinamento LIPAI e tem como objetivo a construção de um sistema em Python para **registro e leitura de transações financeiras pessoais**, utilizando leitura de arquivos, modularização e Programação Orientada a Objetos (POO).

Atualmente, o projeto está focado na **leitura de dados a partir de um arquivo CSV** e na **transformação dessas informações em objetos Python**.

---

## Estrutura do Projeto

```
Projeto 1/
├── main.py
├── models.py
├── repositorio_transacoes.py
├── relatorio.py
└── data/
    └── transacoes_projeto1lipai.csv
```
## Organização dos Arquivos

main.py
Arquivo principal do projeto.
Responsável por:
- Definir o caminho do arquivo CSV
- Localizar o arquivo de forma segura usando o caminho relativo ao próprio script
- Chamar a função de carregamento de transações
- Exibir as transações carregadas no terminal

models.py
Contém a definição da classe principal do projeto:
Classe Transacao
Representa uma transação financeira (receita ou despesa), com os seguintes atributos:
- id
- tipo (receita ou despesa)
- categoria
- descricao
- data (no padrão ISO 8601 – YYYY-MM-DD)
- valor
Essa classe é responsável apenas por modelar os dados, sem conter lógica de leitura de arquivos ou regras de negócio.

repositorio_transacoes.py
Responsável pela leitura do arquivo CSV e pela conversão dos dados em objetos Transacao.
Função implementada:
carregar_transacoes(caminho_csv):
- Abre o arquivo CSV
- Lê os dados utilizando csv.DictReader
- Cria objetos Transacao para cada linha do arquivo
- Retorna uma lista de transações carregadas

relatorio.py
Arquivo criado para centralizar funções de relatório e cálculos futuros.
Atualmente, encontra-se vazio, aguardando a implementação das funcionalidades de resumo e análise.

## Arquivo de Dados
data/transacoes_projeto1lipai.csv
Arquivo CSV utilizado para persistência das transações financeiras.
Cada linha do arquivo representa uma transação, contendo as colunas:
id,tipo,categoria,descricao,data,valor
O arquivo é lido diretamente pelo sistema e transformado em objetos Python.

## Tecnologias Utilizadas
- Python 3
- Leitura de arquivos CSV (csv)
- Programação Orientada a Objetos (POO)
- Organização modular do código

## Estado Atual do Projeto
Até o momento, o projeto:
- Localiza corretamente o arquivo CSV
- Realiza a leitura dos dados
- Converte cada linha do arquivo em um objeto Transacao
- Exibe as transações carregadas no terminal
O código está organizado de forma modular, respeitando a separação de responsabilidades entre entrada, modelo de dados e persistência.
