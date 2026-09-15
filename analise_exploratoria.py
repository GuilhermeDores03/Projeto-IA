import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../dataset/interacoes_tutor.csv")
print(df.head())

print(df.info())
print(df.describe(include="all"))

print(df.isna().sum())

df["tempo_resposta_seg"] = pd.to_numeric(df["tempo_resposta_seg"], errors="coerce")
medianas_por_dificuldade = df.groupby("nivel_dificuldade")["tempo_resposta_seg"].transform("median")
df["tempo_resposta_seg"] = df["tempo_resposta_seg"].fillna(medianas_por_dificuldade)

print(df.isna().sum())

colunas_sensiveis = ["nome", "email", "escola", "cpf", "endereco"]
presentes = [c for c in colunas_sensiveis if c in df.columns]
print(presentes if presentes else "Nenhuma — dataset anonimizado.")

acertos_por_topico = df.groupby("topico")["acertou_exercicio"].mean().sort_values(ascending=False)

plt.figure(figsize=(8, 5))
acertos_por_topico.plot(kind="bar")
plt.ylabel("Taxa de acerto")
plt.title("Taxa de acerto por tópico")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("acertos_por_topico.png")
plt.show()

tempo_por_dificuldade = df.groupby("nivel_dificuldade")["tempo_resposta_seg"].mean().reindex(["fácil", "médio", "difícil"])

plt.figure(figsize=(6, 4))
tempo_por_dificuldade.plot(kind="bar", color="orange")
plt.ylabel("Tempo médio de resposta (s)")
plt.title("Tempo médio de resposta por nível de dificuldade")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("tempo_por_dificuldade.png")
plt.show()

frequencia_topicos = df["topico"].value_counts()

plt.figure(figsize=(8, 5))
frequencia_topicos.plot(kind="bar", color="green")
plt.ylabel("Número de interações")
plt.title("Frequência de dúvidas registradas por tópico")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("frequencia_topicos.png")
plt.show()
