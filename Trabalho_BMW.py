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

h1 =input('Indique a hora inicial da reserva no formato hh:mm')
h2=input('Indique a hora final da reserva no formato hh:mm')
# Hora final
hf = datetime.strptime(h2, '%H:%M')

# Hora inicial
hi = datetime.strptime(h1, '%H:%M')

if quantidade_dias==0:
    while numero_horas <1:
        print("Reseva anulada. O número mínimo de horas é 1 e a sua reserva está com", numero_horas, "horas")
        h1 =input('Indique a hora inicial da reserva no formato hh:mm')
        h2=input('Indique a hora final da reserva no formato hh:mm')
        numero_horas = (datetime.strptime(h2, '%H:%M') - datetime.strptime(h1, '%H:%M')).seconds / 3600
    print("A reserva foi efetuada e durou ", numero_horas)
    
# Quando não são 0 dias e está fora do ciclo while, ou seja, quando a reserva não tem mais de 4 dias
print("A reserva foi efetuada e durou", quantidade_dias, "dias e ", numero_horas, "horas")

from tkinter import*

janela = Tk()
janela.title("Trabalho BMW")
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

       
