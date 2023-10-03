from tkinter import*

janela = Tk()
janela.title("Click search button")
janela.geometry('250x250')

botao = Button(janela, text="Shows empty list")
botao.grid(column=0, row=0)

botao2 = Button(janela, text="Shows reservations list")
botao2.grid(column=1, row=0)

janela.mainloop()
