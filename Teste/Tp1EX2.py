# Converter minutos para horas e minutos
minutos = int(input("Coloque determinado tempo em minutos: "))

horas = minutos // 60
minutos_restantes = minutos % 60

print("Esses minutos são equivalentes a", horas, "horas e", minutos_restantes, "minutos.")

# Converter horas e minutos de volta para minutos totais
horas_input = int(input("Coloque o número de horas: "))
minutos_input = int(input("Coloque o número de minutos: "))

total_minutos = (horas_input * 60) + minutos_input
print("O total de minutos é:", total_minutos)