from datetime import datetime

d1 =input('Indique a data inicial da reserva no formato DD-MM-AAAA')
d2=input('Indique a data final da reserva no formato DD-MM-AAAA')


# Data final
df = datetime.strptime('d1', ‘%d/%m/%Y %H:%M’)


# Data inicial
di = datetime.strptime('d1', ‘%d/%m/%Y %H:%M’)

# Calculo da quantidade de dias da reserva
quantidade_dias = abs((d2 - d1).days)

if quantidade_dias>4:
    print('reservada anuluda')
else:
    print('reserva válida)
    marca=[]
    m=input('Selecione uma marca')
    if m has on stock:
          print('Reservada concluída')
    else:
        print('Stock cheio. Escolha outra marca)
        m=input('Selecione uma marca')

h1 =input('Indique a hora inicial da reserva no formato hh:mm')
h2=input('Indique a hora final da reserva no formato hh:mm')
# Hora final
hf = datetime.strptime('h2', '%H:%M')

# Hora inicial
hi = datetime.strptime('h1', '%H:%M')

numero_horas=h_f-h_i
print("O número de horas durante o aluguer do veículo é ", numero_horas)
              





