import re

def calcular(expressao):
    # Função auxiliar para calcular uma operação
    def calcular_operacao(operador, operando1, operando2):
        if operador == '+':
            return operando1 - (-operando2)
        elif operador == '-':
            return operando1 + (-operando2)
        elif operador == '*' or operador == "x":
            resultado = operando2
            while operando1 > 0:
                resultado = resultado + operando1
                operando1 -= 1
            return resultado
        elif operador == '/' or operador == '÷':
            dividir = operando1
            resultado = 0
            while dividir > 0:
                dividir = dividir - operando2
                resultado = resultado + 1
            return resultado
        else:
            raise ValueError(f'Operação inválida: {operador}')

    # Verifica se há parênteses na expressão
    while '(' in expressao:
        # Encontra o parêntese de fechamento correspondente
        indice_abertura = expressao.rfind('(')
        indice_fechamento = indice_abertura + expressao[indice_abertura:].index(')')
        
        # Calcula a expressão dentro dos parênteses
        resultado_parcial = calcular(expressao[indice_abertura+1:indice_fechamento])
        
        # Substitui a expressão entre parênteses pelo resultado
        expressao = expressao[:indice_abertura] + str(resultado_parcial) + expressao[indice_fechamento+1:]

    # Adiciona espaços ao redor dos operadores para garantir que eles sejam separados corretamente
    expressao = re.sub(r'([\+\-\*/])', r' \1 ', expressao)

    # Divide a string nos espaços, resultando em uma lista onde cada número e operador são elementos separados
    contas = expressao.split()

    # Verifica se a lista contém elementos
    if not contas:
        raise ValueError("A expressão está vazia ou mal formada.")

    # Inicializa o resultado anterior
    resultado_anterior = float(contas[0])  # Agora usamos float para lidar com decimais

    for i in range(1, len(contas), 2):
        operador = contas[i]
        operando = float(contas[i+1])  # Usamos float aqui também

        # Calcula a operação
        try:
            resultado_anterior = calcular_operacao(operador, resultado_anterior, operando)
        except ValueError as e:
            raise ValueError(f"Erro ao calcular operação: {e}")

    return resultado_anterior

# Exemplo de uso
try:
    expressao = input("Escreva uma conta para ser resolvida:\n")
    resultado = calcular(expressao)
    print(f"Resultado da expressão '{expressao}': {resultado}")
except Exception as e:
    print(f"Erro: {e}")