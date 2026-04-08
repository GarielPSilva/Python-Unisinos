salario_minimo = int(input("Digite o valor do salário mínimo: "))
salario_funcionario = int(input("Digite o valor do salário do funcionário: "))
horas_trabalhadas = int(input("Digite o número de horas trabalhadas: "))
valor_hora = salario_minimo / 8
salario_final = valor_hora * horas_trabalhadas
print(f"O salário final do funcionário é: R$ {salario_final:.2f}")

