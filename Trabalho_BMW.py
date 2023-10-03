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

from tkinter import*

janela = Tk()
janela.title("Click search button")
janela.geometry('250x250')

botao = Button(janela, text="Shows empty list")
botao.grid(column=0, row=0)

botao2 = Button(janela, text="Shows reservations list")
botao2.grid(column=1, row=0)

janela.mainloop()

# Depois de se ter o botão da coluna 1, escolhe-se a marca da reserva
marca=[]
m =input('Selecione uma marca')
if m has on stock:
    print('Reservada concluída')
else:
    print('Stock cheio. Escolha outra marca')
    m=input('Selecione uma marca')

h1 =input('Indique a hora inicial da reserva no formato hh:mm')
h2=input('Indique a hora final da reserva no formato hh:mm')
# Hora final
hf = datetime.strptime(h2, '%H:%M')

# Hora inicial
hi = datetime.strptime(h1, '%H:%M')

numero_horas=h_f-h_i
print("O número de horas durante o aluguer do veículo é ", numero_horas)

              





