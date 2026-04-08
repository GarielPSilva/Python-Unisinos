salario_inicial = float(input("Digite o salário inicial: "))
salario_com_aumento = salario_inicial * 0.15
imposto = salario_com_aumento * 0.08

salario_final = salario_com_aumento - imposto

print(f"Salário inicial: R$ {salario_inicial:.2f}")
print(f"Salário com aumento: R$ {salario_com_aumento:.2f}")
print(f"Salário final após desconto de impostos: R$ {salario_final:.2f}")