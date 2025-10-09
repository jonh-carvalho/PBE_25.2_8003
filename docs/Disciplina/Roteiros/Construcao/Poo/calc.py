### 1. Programação Procedural

def calcular_area(base, altura):
    """Calcula a área de um retângulo.

    Args:
        base (float): A base do retângulo.
        altura (float): A altura do retângulo.

    Returns:
        float: A área do retângulo.
    """

    area = base * altura
    return area

# Obtendo os dados do usuário
base = float(input("Digite a base do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))

# Calculando a área
resultado = calcular_area(base, altura)

# Imprimindo o resultado
print("A área do retângulo é:", resultado)