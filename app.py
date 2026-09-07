#Entrada
nome = input("digite o nome do eletrodoméstico: ")
potencia = float(input("digite a potência do eletrodoméstico (W): "))
horasDia = float(input("tempo médio de uso(em horas): "))
#Processamento
consumomensal = (potencia * horasDia * 30) / 1000
custoPorKWh = 0.75
custoestimado = consumomensal * custoPorKWh
#Saída
print (f"\nNome do eletrodoméstico: {nome}")
print (f"Consumo mensal: {consumomensal:.2f} em kWh")
print (f"Custo estimado: {custoestimado:.2f} em R$")
