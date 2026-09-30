#Entrada
nome = input("digite o nome do eletrodoméstico: ")
potencia = float(input("digite a potência do eletrodoméstico (W): "))
horas_dia = float(input("tempo médio de uso(em horas): "))
#validação
if potencia <= 0:
    print("A potência deve ser maior que zero.")
elif horas_dia <= 0 or horas_dia > 24:
    print("O tempo de uso deve ser maior que zero e no máximo 24 horas.")
else:
#Processamento
    consumo_mensal = (potencia * horas_dia * 30) / 1000
    custo_por_KWh = 0.75
    custo_estimado = consumo_mensal * custo_por_KWh
#Saída
    print (f"\nNome do eletrodoméstico: {nome}")
    print (f"Consumo mensal: {consumo_mensal:.2f} em kWh")
    print (f"Custo estimado: {custo_estimado:.2f} em R$")
