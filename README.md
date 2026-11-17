# Tutor Inteligente — Projeto de Inteligência Artificial

**Tema:** assistente demonstrativo de apoio ao estudo no Ensino Fundamental.

Este repositório contém:
- um dataset demonstrativo de interações (`dataset/interacoes_tutor.csv`);
- um script de análise exploratória em Python (`analise_exploratoria.py`);
- um protótipo simples em terminal (`tutor_demo.py`), com explicações e exercícios previamente cadastrados;
- gráficos e resumo gerados pela análise (`resultados/`).

## Importante sobre o escopo

O arquivo CSV do projeto foi identificado no README anterior como **exemplo/placeholder até a coleta real**. Portanto, os 150 registros devem ser tratados como dados demonstrativos. Não representam uma pesquisa validada com alunos voluntários e não permitem afirmar que a ferramenta melhorou a aprendizagem.

O protótipo atual **não está integrado à API do ChatGPT nem a outro LLM**. Ele apresenta um fluxo de tutoria com conteúdo e respostas predefinidos. A integração com LLM permanece como possibilidade de trabalho futuro.

## Como executar

Requisitos: Python 3.9 ou superior.

Instale as bibliotecas da análise:

```bash
python -m pip install pandas matplotlib
```

Na pasta raiz do projeto, execute a análise:

```bash
python analise_exploratoria.py
```

Os gráficos e o arquivo `resumo_analise.txt` serão salvos na pasta `resultados/`.

Para testar o protótipo:

```bash
python tutor_demo.py
```

O protótipo funciona no terminal e não exige chave de API ou cadastro em serviço externo.

## Estrutura

```text
Projeto-IA/
├── dataset/
│   └── interacoes_tutor.csv
├── resultados/
├── analise_exploratoria.py
├── tutor_demo.py
└── README.md
```

## Integrante

Guilherme Dores — dados de identificação devem ser conferidos antes da entrega.

## Próximas melhorias possíveis

- substituir o dataset demonstrativo por dados coletados com autorização e anonimização adequadas;
- ampliar a variedade de exercícios e níveis escolares;
- avaliar o protótipo com acompanhamento docente;
- integrar um modelo de linguagem em uma etapa futura, com salvaguardas para público infantojuvenil.
