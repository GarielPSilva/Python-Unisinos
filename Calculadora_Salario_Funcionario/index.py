peso_gramas = float(input("Digite o peso em gramas: "))
peso_kg = peso_gramas / 1000
preço_kg = float(input("Digite o preço por kg: "))
valor_a_pagar = peso_kg * preço_kg
print(f"O preço a pagar é: R$ {valor_a_pagar:.2f}")
salario_inicial = float(input("Digite o salário inicial: "))
salario_com_aumento = salario_inicial * 0.15
imposto = salario_com_aumento * 0.08

salario_final = salario_com_aumento - imposto

print(f"Salário inicial: R$ {salario_inicial:.2f}")
print(f"Salário com aumento: R$ {salario_com_aumento:.2f}")
print(f"Salário final após desconto de impostos: R$ {salario_final:.2f}")