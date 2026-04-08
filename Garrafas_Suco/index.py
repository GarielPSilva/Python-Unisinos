salario_inicial = float(input("Digite o salário inicial: "))
salario_com_aumento = salario_inicial * 0.15
imposto = salario_com_aumento * 0.08
garrafa_suco_330ml = int(input("Digite a quantidade de garrafas de 330ml: "))
garrafa_suco_700ml = int(input("Digite a quantidade de garrafas de 700ml: "))
garrafa_suco_1_3L = int(input("Digite a quantidade de garrafas de 1.3L: "))

salario_final = salario_com_aumento - imposto

print(f"Salário inicial: R$ {salario_inicial:.2f}")
print(f"Salário com aumento: R$ {salario_com_aumento:.2f}")
print(f"Salário final após desconto de impostos: R$ {salario_final:.2f}")
total_ml = (garrafa_suco_330ml * 0.33) + (garrafa_suco_700ml * 0.7) + (garrafa_suco_1_3L * 1.3)
print(f"A quantidade total de litros é: {total_ml:.2f} litros")