"""
1. Desenvolva uma calculadora em Python que realize as quatro operações básicas
(adição, subtração, multiplicação e divisão) entre dois números.
A calculadora deve ser capaz de lidar com diversos tipos de erros de entrada e operação
"""

while True:
	try:
		num1 = float(input("Digite o primeiro número: "))
		num2 = float(input("Digite o segundo número: "))
		operacao = input("Digite a operação (+, -, * ou /): ")
		#operacao = input("Digite a operação (+, -, * ou /): ").strip()

		if operacao == "+":
			resultado = num1 + num2
		elif operacao == "-":
			resultado = num1 - num2
		elif operacao == "*":
			resultado = num1 * num2
		elif operacao == "/":
			try:
				resultado = num1 / num2
			except ZeroDivisionError:
				print("Erro: divisão por zero não é permitida. Tente novamente.")
				continue
		else:
				print("Erro: Operação Inválida, utilize apenas +, -, * ou /.")
				continue

	except ValueError as e:
			print(f"Erro {e}. Favor, tente novamente com valores numéricos.")
			continue

	print(f"Resultado: {resultado}")
	break