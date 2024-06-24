n = int(input())
matrices = []

# Entrada das matrizes de confusão
for _ in range(n):
    matrix = input()
    matrices.append(list(map(int, matrix.split(','))))
    
# Função para calcular acurácia e precisão
def calculate_metrics(matrix):
    tp, fp, fn, tn = matrix
    accuracy = (tp + tn) / (tp + fp + fn + tn)
    precision = tp / (tp + fp) if (tp + fp) != 0 else 0  
    return accuracy, precision

# Função para encontrar o índice da matriz com melhor desempenho
def best_performance(matrices):
    best_index = 0
    best_accuracy = 0
    best_precision = 0
    
    for index, matrix in enumerate(matrices):
        tp, fp, fn, tn = matrix
        
        # Calcular acurácia e precisão
        accuracy, precision = calculate_metrics(matrix)
        
        # Atualizar os melhores índices se os novos valores forem superiores
        if (accuracy > best_accuracy) or (accuracy == best_accuracy and precision > best_precision):
            best_index = index
            best_accuracy = accuracy
            best_precision = precision
    
    return best_index, best_accuracy, best_precision
        
# Função para formatar as métricas conforme necessário
def format_metric(value):
	decimal_int = [0.1 ,0.2 ,0.3 ,0.4 ,0.5 ,0.6 ,0.7 ,0.8 ,0.9]	
	if value == 1 or value == 0:
		return f"{value:.1f}"
	elif value in decimal_int:
		return f"{value:.1f}"
	return f"{value:.2f}" 

# Encontrar o melhor desempenho
best_index, best_accuracy, best_precision = best_performance(matrices)


print(f"Índice: {best_index + 1}")  
print(f"Acurácia: {format_metric(best_accuracy)}")
print(f"Precisão: {format_metric(best_precision)}")
