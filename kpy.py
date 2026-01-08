# Desafio: Calculo de Bonus com Entrada do Usuario
#
# Escreva um programa em Python que solicita ao usuario para digitar seu nome,
# o valor do seu salario mensal e o valor do bonus que recebeu. O programa deve,
# entao, imprimir uma mensagem saudando o usuario pelo nome e informando o valor
# do salario em comparacao com o bonus recebido.
#
# 1. O programa deve comecar solicitando ao usuario que insira seu nome.
nome = input("Digite seu nome: ")

# 2. Em seguida, o programa deve pedir ao usuario para inserir o valor do seu salario.
#    Considere que este valor pode ser um numero decimal.
salario = float(input("Digite o valor do seu salario mensal: "))

# 3. Depois, o programa deve solicitar ao usuario que insira o percentual do bonus,
#    por exemplo, 1.5 para 1.5%.
bonus_percentual = float(input("Digite o percentual do bonus recebido: "))
bonus = bonus_percentual / 100

# 4. O calculo do KPI do bonus de 2026 e de 1000 + salario * bonus
kpi_bonus = 1000 + salario * bonus

# 5. Finalmente, o programa deve imprimir uma mensagem no seguinte formato:
#    "Ola [nome], o seu valor bonus foi de 5000".
def brl(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

print(
    f"Ola {nome}, seu salario e {brl(salario)}, "
    f"o bonus foi {bonus_percentual:.1f}% e o KPI foi {brl(kpi_bonus)}"
)
