peso_gramas = float(input("Digite o peso em gramas: "))
peso_kg = peso_gramas / 1000
preço_kg = float(input("Digite o preço por kg: "))
valor_a_pagar = peso_kg * preço_kg
print(f"O preço a pagar é: R$ {valor_a_pagar:.2f}")