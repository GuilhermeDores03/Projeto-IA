"""
Projeto: Tutor Inteligente
Integrante: Guilherme Dores
Descrição: análise exploratória e preparação do dataset demonstrativo de interações.
Histórico:
- 17/11/2026 - revisão dos caminhos, tratamento de ausentes e geração de indicadores/gráficos.
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent
ARQUIVO = BASE_DIR / "dataset" / "interacoes_tutor.csv"
PASTA_RESULTADOS = BASE_DIR / "resultados"
PASTA_RESULTADOS.mkdir(exist_ok=True)

df = pd.read_csv(ARQUIVO)

# Conversão e tratamento de tipos
df["data_interacao"] = pd.to_datetime(df["data_interacao"], errors="coerce")
df["tempo_resposta_seg"] = pd.to_numeric(df["tempo_resposta_seg"], errors="coerce")
df["acertou_exercicio"] = pd.to_numeric(df["acertou_exercicio"], errors="coerce")

# Imputa tempos ausentes pela mediana do respectivo nível; fallback para mediana geral.
faltantes_tempo = int(df["tempo_resposta_seg"].isna().sum())
medianas = df.groupby("nivel_dificuldade")["tempo_resposta_seg"].transform("median")
df["tempo_resposta_seg"] = df["tempo_resposta_seg"].fillna(medianas)
df["tempo_resposta_seg"] = df["tempo_resposta_seg"].fillna(df["tempo_resposta_seg"].median())

# Indicadores descritivos
total = len(df)
acertos = int(df["acertou_exercicio"].eq(1).sum())
erros = int(df["acertou_exercicio"].eq(0).sum())
taxa_geral = df["acertou_exercicio"].mean()
resumo = [
    f"Total de registros: {total}",
    f"Alunos/IDs distintos: {df['aluno_id'].nunique()}",
    f"Tópicos distintos: {df['topico'].nunique()}",
    f"Registros com acerto: {acertos}",
    f"Registros com erro: {erros}",
    f"Taxa de acerto global: {taxa_geral:.1%}",
    f"Tempos ausentes antes do tratamento: {faltantes_tempo}",
    f"Tempo médio (s), após tratamento: {df['tempo_resposta_seg'].mean():.2f}",
    "",
    "Distribuição por tópico:",
    df.groupby("topico").agg(
        interacoes=("interacao_id", "count"),
        taxa_acerto=("acertou_exercicio", "mean"),
        tempo_medio_seg=("tempo_resposta_seg", "mean"),
    ).sort_values("interacoes", ascending=False).to_string(),
    "",
    "Distribuição por dificuldade:",
    df.groupby("nivel_dificuldade").agg(
        interacoes=("interacao_id", "count"),
        taxa_acerto=("acertou_exercicio", "mean"),
        tempo_medio_seg=("tempo_resposta_seg", "mean"),
    ).to_string(),
    "",
    "Limitação: o README original classifica o arquivo como exemplo/placeholder. "
    "Os resultados descrevem somente esse arquivo e não comprovam desempenho real de alunos."
]
(PASTA_RESULTADOS / "resumo_analise.txt").write_text("\n".join(resumo), encoding="utf-8")

# Gráficos
por_topico = df.groupby("topico")["acertou_exercicio"].mean().sort_values(ascending=False)
plt.figure(figsize=(10, 5))
por_topico.plot(kind="bar")
plt.ylabel("Taxa de acerto")
plt.ylim(0, 1)
plt.title("Taxa de acerto por tópico (dataset demonstrativo)")
plt.xticks(rotation=35, ha="right")
plt.tight_layout()
plt.savefig(PASTA_RESULTADOS / "taxa_acerto_topico.png", dpi=150)
plt.close()

tempo = df.groupby("nivel_dificuldade")["tempo_resposta_seg"].mean().reindex(["fácil", "médio", "difícil"])
plt.figure(figsize=(7, 4))
tempo.plot(kind="bar")
plt.ylabel("Tempo médio (segundos)")
plt.title("Tempo médio por nível de dificuldade")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(PASTA_RESULTADOS / "tempo_por_dificuldade.png", dpi=150)
plt.close()

freq = df["topico"].value_counts()
plt.figure(figsize=(10, 5))
freq.plot(kind="bar")
plt.ylabel("Número de registros")
plt.title("Quantidade de interações por tópico")
plt.xticks(rotation=35, ha="right")
plt.tight_layout()
plt.savefig(PASTA_RESULTADOS / "frequencia_topicos.png", dpi=150)
plt.close()

print("\n".join(resumo))
print(f"\nGráficos e resumo salvos em: {PASTA_RESULTADOS}")
