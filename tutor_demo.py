"""
Projeto: Tutor Inteligente - protótipo demonstrativo
Integrante: Guilherme Dores
Descrição: demonstra um fluxo simples de tutoria por regras e conteúdo previamente cadastrado.
Observação: não utiliza API, LLM ou geração automática de respostas.
Histórico:
- 17/11/2026 - criação do protótipo demonstrativo em terminal.
"""

CONTEUDOS = {
    "Frações": {
        "explicacao": "Uma fração representa partes de um todo. Em 3/4, o número 3 é o numerador (partes consideradas) e 4 é o denominador (partes iguais do todo).",
        "pergunta": "Qual fração representa 2 partes de um total de 5 partes iguais?",
        "resposta": "2/5",
        "dica": "O numerador indica quantas partes foram consideradas; o denominador indica o total de partes iguais."
    },
    "Multiplicação": {
        "explicacao": "Multiplicar é somar parcelas iguais. Por exemplo, 4 × 3 significa 4 grupos de 3, ou 3 + 3 + 3 + 3 = 12.",
        "pergunta": "Quanto é 7 × 6?",
        "resposta": "42",
        "dica": "Você pode pensar em 7 grupos de 6 ou somar 6 sete vezes."
    },
    "Divisão": {
        "explicacao": "Dividir é repartir uma quantidade em partes iguais ou descobrir quantas vezes um número cabe em outro.",
        "pergunta": "Quanto é 24 ÷ 6?",
        "resposta": "4",
        "dica": "Pense: qual número multiplicado por 6 resulta em 24?"
    },
    "Sistema Solar": {
        "explicacao": "O Sistema Solar é formado pelo Sol e pelos corpos celestes que orbitam ao seu redor, incluindo oito planetas.",
        "pergunta": "Qual é a estrela que fica no centro do Sistema Solar?",
        "resposta": "sol",
        "dica": "É a estrela que fornece luz e calor à Terra."
    },
    "Ortografia": {
        "explicacao": "Ortografia é o conjunto de regras que orienta a escrita correta das palavras. O contexto ajuda a distinguir palavras com sons parecidos.",
        "pergunta": "Na frase 'Quero ___ estudar', complete com 'mas' ou 'mais'.",
        "resposta": "mais",
        "dica": "'Mais' indica quantidade ou intensidade; 'mas' expressa oposição."
    },
    "Gramática - Concordância": {
        "explicacao": "Na concordância verbal, o verbo deve concordar em número e pessoa com o sujeito. Exemplo: 'Os meninos estudam'.",
        "pergunta": "Complete: 'As crianças ___ no parque' (brinca/brincam).",
        "resposta": "brincam",
        "dica": "O sujeito está no plural; o verbo também deve ficar no plural."
    },
    "Geometria - Ângulos": {
        "explicacao": "Ângulo é a abertura entre duas semirretas com a mesma origem. Agudo é menor que 90°, reto mede 90° e obtuso é maior que 90° e menor que 180°.",
        "pergunta": "Um ângulo de 120° é agudo, reto ou obtuso?",
        "resposta": "obtuso",
        "dica": "Compare 120° com 90° e 180°."
    },
    "Interpretação de Texto": {
        "explicacao": "A ideia principal é a informação mais importante do texto ou parágrafo. Para encontrá-la, observe o assunto e o que o autor quer comunicar.",
        "pergunta": "Para identificar a ideia principal, devemos procurar a informação mais ___ do trecho.",
        "resposta": "importante",
        "dica": "Não se prenda a um detalhe: pense no que resume o trecho inteiro."
    }
}

def normalizar(texto):
    return " ".join(texto.strip().lower().split())

def executar():
    print("=" * 54)
    print("TUTOR INTELIGENTE - PROTÓTIPO DEMONSTRATIVO")
    print("Conteúdo educativo predefinido; sem conexão com LLM/API.")
    print("=" * 54)
    topicos = list(CONTEUDOS)
    for i, topico in enumerate(topicos, 1):
        print(f"{i}. {topico}")
    escolha = input("\nEscolha um tópico pelo número (ou 0 para sair): ").strip()
    if escolha == "0":
        print("Até mais!")
        return
    if not escolha.isdigit() or not 1 <= int(escolha) <= len(topicos):
        print("Opção inválida. Execute novamente e escolha um número da lista.")
        return

    topico = topicos[int(escolha) - 1]
    conteudo = CONTEUDOS[topico]
    print(f"\nTópico: {topico}\n")
    print("Explicação:")
    print(conteudo["explicacao"])
    print("\nExercício:")
    print(conteudo["pergunta"])
    resposta = input("\nSua resposta: ")
    if normalizar(resposta) == normalizar(conteudo["resposta"]):
        print("\nMuito bem! Resposta correta.")
    else:
        print("\nVamos revisar. A resposta esperada é:", conteudo["resposta"])
        print("Dica:", conteudo["dica"])
    print("\nEste protótipo é uma demonstração baseada em regras e respostas cadastradas.")

if __name__ == "__main__":
    executar()
