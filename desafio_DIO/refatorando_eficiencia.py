def identificar_funcoes(texto):
    return "Separe funções em unidades coesas e com responsabilidades únicas."

def entrada_de_dados(texto):
    return "Valide e normalize as entradas para evitar inconsistências."

def nomenclatura_significativa(texto):
    return "Use nomes descritivos para variáveis e funções."

def processar_entrada(texto):
    # Dicionário mapeando textos para funções
    opcoes = {
        "Dica de boas práticas de refatoração de código, nas funções.": identificar_funcoes,
        "Dica de boas práticas de refatoração de código, nas entrada de dados.": entrada_de_dados,
        "Dica de boas práticas de refatoração de código, nomenclaturas.": nomenclatura_significativa
    }

    # Verifica se o texto está presente nas opções
    if texto in opcoes:
        # Chama a função correspondente ao texto e retorna o resultado
        return opcoes[texto](texto)
    else:
        return "Opção inválida"

def desafio():
    # Solicita uma entrada do usuário
    entrada = input()
    # Processa a entrada e obtém a saída
    saida = processar_entrada(entrada)
    # Exibe a saída
    print(saida)

desafio()
