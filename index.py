garrafa_suco_330ml = int(input("Digite a quantidade de garrafas de 330ml: "))
garrafa_suco_700ml = int(input("Digite a quantidade de garrafas de 700ml: "))
garrafa_suco_1_3L = int(input("Digite a quantidade de garrafas de 1.3L: "))

total_ml = (garrafa_suco_330ml * 0.33) + (garrafa_suco_700ml * 0.7) + (garrafa_suco_1_3L * 1.3)
print(f"A quantidade total de litros é: {total_ml:.2f} litros")