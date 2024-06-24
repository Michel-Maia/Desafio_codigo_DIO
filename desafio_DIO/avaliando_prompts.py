# Entrada do usuário
prompt_usuario = input()

# Função para avaliar se o prompt está adequado
def avaliar_prompt(prompt):
    # Verifica se o prompt contém palavras-chave relevantes
    palavras_chave = ["inteligência artificial", "sistemas de recomendação online", "exemplos de conversação", "explique conceitos", "dicas de tecnologia" ]
    
    for palavra in palavras_chave:
        if palavra in prompt.lower():
            return "O prompt está adequado."
    
    return "O prompt não está adequado. Inclua palavras-chave relevantes."
    

feedback_usuario = avaliar_prompt(prompt_usuario)
print(feedback_usuario)