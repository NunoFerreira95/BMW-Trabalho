
from datetime import datetime

d1 =input('Indique a data inicial da reserva no formato DD-MM-AAAA')
d2=input('Indique a data final da reserva no formato DD-MM-AAAA')

# Data inicial
di = datetime.strptime(d1, "%d-%m-%Y")

# Data final
df = datetime.strptime(d2, "%d-%m-%Y")

# Calculo da quantidade de dias da reserva
quantidade_dias = abs((df - di).days)

print("A quantidade de dias da reserva é ", quantidade_dias)

while quantidade_dias>4:
    print("A reservada é anulada. Os dias da reserva não podem ser mais de 4.")
    d1 =input('Indique a data inicial da reserva no formato DD-MM-AAAA')
    d2=input('Indique a data final da reserva no formato DD-MM-AAAA')
    di = datetime.strptime(d1, "%d-%m-%Y")
    df = datetime.strptime(d2, "%d-%m-%Y")
    quantidade_dias = abs((df - di).days)
    print("A quantidade de dias da reserva é ", quantidade_dias)

print("A reserva foi efetuada")

