class Retangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

# Obtendo os dados do usuário
base = float(input("Digite a base do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))

# Criando um objeto Retangulo
retangulo = Retangulo(base, altura)

# Calculando a área
resultado = retangulo.calcular_area()

# Imprimindo o resultado
print("A área do retângulo é:", resultado)